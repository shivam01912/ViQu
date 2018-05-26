from summa import summarizer
from summa import keywords

text= raw_input("Enter text: ")

print "\n\n",summarizer.summarize(text,words=100)
print "\n\n",keywords.keywords(text,ratio=0.5)
print "\n\n",keywords.keywords(text,words=20)