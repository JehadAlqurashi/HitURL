import requests
import argparse
from concurrent.futures import ThreadPoolExecutor

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
        print(req.url)
        if req.status_code == 200:
            print(req.url)
parser = argparse.ArgumentParser("""
python3 AdminFinder -t [url]
ex:python3 AdminFinder -t http://google.com
""")
parser.add_argument("-t","--t")
args = parser.parse_args()
url = args.t
if url !=None:
    with ThreadPoolExecutor(max_workers=30) as executor:
        result = executor.map(findPanel,[url]*100)
        concurrent.futures.wait(results, timeout=10, return_when=concurrent.futures.FIRST_COMPLETED)
        for f in concurrent.futures.as_completed(results):
            f_success = f.result()
            if not f_success:
                executor.shutdown(wait=False, cancel_futures=True) # shutdown if one fails
else:
    logo()
