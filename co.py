import markovify, time, random, textwrap

WORDS = 50*1000 # 50k words is considered a novel

PERC_NEW_PARAGRAPH = .35 # increase this to increase the amount of new paragraphs

with open("corpus.txt") as f: text=markovify.Text(f.read(),state_size=4)

sentence = lambda: text.make_sentence(tries=1000,max_overlap_ratio=0.8,max_overlap_total=(2**64))

out = ""
while len(out.split())<=WORDS:
	sent = sentence()
	while sent is None: sent = sentence()
	out+=sent
	if random.random()<=PERC_NEW_PARAGRAPH: # randomly start a new paragraph
		out+="\n\n"
	else:
		out+=" "

with open(time.strftime("%Y%m%d-%H.%M.%S.out.txt"),"w") as f:
	f.write(textwrap.fill(out,80)) # wrap to 80 chars
