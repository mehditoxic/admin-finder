import colorama
import requests,sys
from colorama import Fore,Style
url=input("enter yor url (http:// or https://): ")
if not (url.startswith("http://"))|(url.startswith("https://")) :
    print("The url format is not correct.......")
    sys.exit("Try Again")
data=open("page.txt","r").read()

for i in data.split("\n"):
    target=url+i
    req=requests.get(target)
    if req.status_code==200:
        print(Fore.GREEN,"page found>>>>>>>>>>>",target,Style.RESET_ALL)
        

