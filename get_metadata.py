import markovify

def load(fn,cls=markovify.Text,*args,**kwargs):
	with open(fn) as f:
		return cls(f.read())

titles = load("titles.txt",markovify.NewlineText)
summaries = load("summary_corpus.txt")

print("Title: "+titles.make_sentence(tries=1000,max_overlap_ratio=0.9))
print("Summary: "+" ".join([summaries.make_sentence(tries=1000,max_overlap_ratio=0.9,max_overlap_total=(2**64)) for x in range(3)]))
