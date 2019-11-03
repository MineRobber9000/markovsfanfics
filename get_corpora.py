import fanfiction
scraper = fanfiction.Scraper()

IDS = [
	12425824, # Terrifying Renegade (Steven Universe fanfic)
	12372218, # Come With Me (Steven Universe fanfic)
	13175755, # Steven Universe and The Shadows of Authority
	13423555, # Rejuvenated
	13404851, # Brotherhood of Glass: Episode One
	13420522, # With All My Heart
	13423219, # Crash
	13421588, # Found
	13222117, # How It Will End
	13365151, # What If? Steven Universe
	13422398, # QuartzSwap
	13391850, # A Jasper's Duty
	13414743, # - Ship of Friends -
	13373802, # Pearl plus au
	13394318, # The Oracle of Settlement B1C7
	13202136, # Whispers of the Unheard
	12951465, # This is Unusual!
	13421515, # Pun Fun!
	13356381, # A New Era
	13421441, # O' Spinny Mine
	13391291, # Spinels Return
	13107583, # The Beach City Conspiracy
	13399296, # An Ace's Journey Continues
	13421329, # Steven Universe Future (Fan Fiction)
	13380311, # Return of Red and Black Diamond
	13326123, # Alexandra Crystal Gem the adoptive sister of Steven Universe
	13398845, # The Art of Love and Friendship
	13412502, # Steven: The Regular Boy
	13387579, # Everyone-Needs-A-Friend
	13321479, # He Did It For Me: Steven's Legacy
	13395849, # Never Alone
	13414274, # Healing Tears
	13420579, # When Connie met Steven
	13420570, # Flares
	13420510, # A New Age Rewritten
	13420225, # The Great Diamond Authority
	13419458, # Spindle the Swindler
	13212617, # A Battle in the Mind
	13399620, # Bittersweet Memories
	13419881, # A Nightmarish Storm
	13178650, # When the past repeats itself
	13380008, # Amber
	13394195, # I don't need the world to see, I've been the best I can be
	11872183, # Burn Bright
	13391150, # Era 4: A New Gem
	13245084, # An easter to remember
	13419524, # Never the Same
	13419488, # Caught In The Grey (Oneshot)
	13390525, # The Diamond, the Pearl, and Spinel
	13332598, # A Diamond in the rough
	13386343, # Greg Universe of Pearl Stars
]

def get_story(id):
	try:
		return scraper.scrape_story(id)
	except:
		return None

stories = [get_story(id) for id in IDS]
stories = filter(lambda x: x!=None,stories)

text = ""
for story in stories:
	for chapter in story["chapters"]:
		text+=story["chapters"][chapter].decode("utf-8")

with open("corpus.txt","w") as f: f.write(text)
