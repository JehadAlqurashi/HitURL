import requests
import argparse
import concurrent.futures

def logo():
    print("""
    \033[95m 
    __  ___ __  __  ______  __ 
   / / / (_) /_/ / / / __ \/ / 
  / /_/ / / __/ / / / /_/ / /  
 / __  / / /_/ /_/ / _, _/ /___
/_/ /_/_/\__/\____/_/ |_/_____/
                               


    
""")
wordlist = open("list.txt","r")
def findPanel(url):
    for words in wordlist:
        words = words.strip()
        req = requests.get(url+"/"+words,allow_redirects=False )
        if req.status_code == 200 or req.status_code == 301:
            print(req.url," status_code :",req.status_code)
parser = argparse.ArgumentParser("""
python3 AdminFinder -t [url]
ex:python3 AdminFinder -t http://google.com
""")
parser.add_argument("-t","--t")
args = parser.parse_args()
url = args.t
if url !=None:
    with concurrent.futures.ThreadPoolExecutor(max_workers=30) as executor:
        executor.map(findPanel,[url]*100)
        executor.shutdown(wait=True)
       
else:
    logo()
