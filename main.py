import requests
from bs4 import BeautifulSoup as Soup
import argparse
from dataclasses import dataclass
import re
import time
from pprint import pprint
import os

@dataclass
class Args:
    link:str
    delay:int
    store:int


class Selectors:
    order = [
        "#pnlInventory div.inventory",
    ]

@dataclass
class StockResult:
    status: str|None
    in_stock: bool | None
    quantity: int | str | None
    location : int | None


def get_stock_result(stock_text) -> StockResult:
    result = StockResult(None,None,None,None)
    result.status = stock_text


    # Check if item is carried at this location
    if stock_text == "NOT CARRIED at Micro Center Store":
        return result

    # Check if in stock
    m : re.Match = re.match(r"(\d*)\+? (NEW IN STOCK) at (.*) Store",stock_text)
    if m:
        result.in_stock = True
        result.quantity = m.group(1)
        result.location = m.group(3)
        return result
    
    # Check if out of stock
    m : re.Match = re.match(r"(SOLD OUT) at (.*) Store",stock_text)
    if m:
        result.in_stock = False
        result.quantity = 0
        result.location = m.group(2)
        return result
    
    return result

def send_email(subject, body):
    import smtplib
    from email.mime.text import MIMEText
    # from dotenv import load_dotenv

    # load_dotenv()

    sender = os.getenv("SENDER") # Email to Send From
    password = os.getenv("APP_PASSWORD") # Google App Password
    recipient = os.getenv("RECIPIENT")

    
    msg = MIMEText(body)
    msg['Subject'] = subject
    msg['From'] = sender
    msg['To'] = recipient
    
    try:
        with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp_server:
            smtp_server.login(sender, password)
            smtp_server.sendmail(sender, recipient, msg.as_string())

        print("Email sent successfully!")

    except smtplib.SMTPAuthenticationError:
        print("SMTP Authentication Error: The server didn't accept the username/password combination.")
    except smtplib.SMTPServerDisconnected:
        print("SMTP Server Disconnected: The server unexpectedly disconnected.")
    except smtplib.SMTPException as e:
        print(f"SMTP error occurred: {str(e)}")
    except Exception as e:
        print(f"An error occurred: {str(e)}")
    
    

def main(link:str, delay:int,store_number:int):
    EMAIL_SUBJECT = "MicroCenter Stock Alert"
    i = 0
    while True:
        print(F"Iteration {i}")
        try:
            response = requests.get(link, cookies={"storeSelected":str(store_number)})
            if response.ok:

                html_doc = response.text
                soup = Soup(html_doc,'html.parser')

                item_name = soup.select_one("div.product-header").text.strip()
                img_src = soup.select_one("img.productImageZoom").get("src")
                stock_text = soup.select_one(Selectors.order[0]).text.strip()


                stock_result = get_stock_result(stock_text)
                
                if stock_result.in_stock:
                    send_email(EMAIL_SUBJECT,F"""{item_name} in stock @ {stock_result.location}
                               URL: {link}""")
                    break
            else:
                raise Exception("Non ok response.")
        except Exception as error:
            pprint(error)

        i+=1
        time.sleep(delay)
 





if __name__ == "__main__":
    parser = argparse.ArgumentParser()

    parser.add_argument("link",type=str,help="The link to the MicroCenter product.")
    # parser.add_argument("-v","--verbose",action="store_true",help="More verbose output.")
    parser.add_argument("--delay",type=int,default=3600,help="The time between updates (in seconds). Default:3600")
    parser.add_argument("--store",type=str,default=100,help="The store number, found in cookies in browser")
    args : Args = parser.parse_args()

    print(args.link)
    
    
    main(args.link,args.delay,args.store)