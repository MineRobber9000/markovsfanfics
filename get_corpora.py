import fanfiction, config
scraper = fanfiction.Scraper()

def get_story(id):
	try:
		return scraper.scrape_story(id)
	except:
		return None

stories = [get_story(id) for id in config.IDS]
stories = filter(lambda x: x!=None,stories)

titles = []
text = ""
for story in stories:
	titles.append(story["title"].strip(" -=~"))
	for chapter in story["chapters"]:
		text+=story["chapters"][chapter].decode("utf-8")

with open("corpus.txt","w") as f: f.write(text)
with open("titles.txt","w") as f: f.write("\n".join(titles))
