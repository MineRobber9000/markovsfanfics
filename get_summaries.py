import requests, time, config
DELAY = 1 # at least 1
from bs4 import BeautifulSoup

def get_story(id):
	try:
		time.sleep(DELAY)
		r = requests.get("https://fanfiction.net/s/"+str(id))
		r.raise_for_status()
		soup = BeautifulSoup(r.text,"html.parser")
		return soup.find("div",{"class":"xcontrast_txt"}).text
	except:
		return None

stories = [get_story(id) for id in config.IDS]
stories = filter(lambda x: x!=None,stories)

with open("summary_corpus.txt","w") as f: f.write("\n".join(stories))
