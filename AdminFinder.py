import requests
import argparse
import threading
def logo():
    print("""

     _       _           _       _____ _           _           
    / \   __| |_ __ ___ (_)_ __ |  ___(_)_ __   __| | ___ _ __ 
   / _ \ / _` | '_ ` _ \| | '_ \| |_  | | '_ \ / _` |/ _ \ '__|
  / ___ \ (_| | | | | | | | | | |  _| | | | | | (_| |  __/ |   
 /_/   \_\__,_|_| |_| |_|_|_| |_|_|   |_|_| |_|\__,_|\___|_|   
                                                               

    
""")
wordlist = open("list.txt","r")
def findPanel(url):
    for words in wordlist:
        words = words.strip()
        req = requests.get(url+"/"+words)
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
    for i in range(50):
        t = threading.Thread(target=findPanel,args=(url,))
        t.start()
else:
    logo()
