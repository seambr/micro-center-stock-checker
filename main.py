import requests
from bs4 import BeautifulSoup as Soup
import argparse
from dataclasses import dataclass

@dataclass
class Args:
    link:str
    delay:int



def main(link:str, delay:int):





    pass


if __name__ == "__main__":
    parser = argparse.ArgumentParser()

    parser.add_argument("link",type=str,help="The link to the MicroCenter product.")
    # parser.add_argument("-v","--verbose",action="store_true",help="More verbose output.")
    parser.add_argument("--delay",type=input,default=1800,help="The time between updates (in seconds). Default:1800")

    args : Args = parser.parse_args()
    
    
    main(args)