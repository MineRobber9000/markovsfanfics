import markovify, time, random, textwrap
from nltk.tokenize import sent_tokenize

WORDS = 50*1000 # 50k words is considered a novel

CHAPTER_WORDS = 4*1000 # average fanfic chapter (for novel-length fanfics) is 4k words

PERC_NEW_PARAGRAPH = .35 # increase this to increase the amount of new paragraphs

with open("corpus.txt") as f: text=markovify.Text(f.read(),state_size=4)

sentence = lambda: text.make_sentence(tries=1000,max_overlap_ratio=0.8,max_overlap_total=(2**64))

out = ""
while len(out.split())<=WORDS:
	sent = sentence()
	while sent is None: sent = sentence()
	out+=sent+" "
out.strip()

sentences = sent_tokenize(out)
chapters = []
chapter = []
for sentence in sentences:
	if len(" ".join(chapter).split())>=CHAPTER_WORDS:
		print(chapter)
		chapters.append(" ".join(chapter))
		chapter = []
	chapter.append(sentence)
	if random.random()<=PERC_NEW_PARAGRAPH:
		chapter.append("\n") # start new paragraph
chapters.append(" ".join(chapter))

out = "\n\n".join(["Chapter {!s}\n\n{}".format(i,x) for i,x in enumerate(chapters,1)])

with open(time.strftime("%Y%m%d-%H.%M.%S.out.txt"),"w") as f:
	f.write(out)
