import requests
from bs4 import BeautifulSoup as Soup
import argparse
from dataclasses import dataclass
import re
import time
from pprint import pprint

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


def main(link:str, delay:int,store_number:int):
    i = 0
    while True:
        print(F"Iteration {i}")
        try:
            response = requests.get(link, cookies={"storeSelected":str(store_number)})
            if response.ok:

                html_doc = response.text
                soup = Soup(html_doc,'html.parser')

                stock_text = soup.select_one(Selectors.order[0]).text.strip()


                stock_result = get_stock_result(stock_text)

                pprint(stock_result)
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
    parser.add_argument("--delay",type=int,default=3600,help="The time between updates (in seconds). Default:1800")
    parser.add_argument("--store",type=int,default=100,help="The store number, found in cookies in browser")
    args : Args = parser.parse_args()
    
    
    main(args.link,args.delay,args.store)