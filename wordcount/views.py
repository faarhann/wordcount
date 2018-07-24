from django.http import HttpResponse
from django.shortcuts import render
import operator

def home(request):
	return render(request, "home.html")

def count(request):
	fulltext = request.GET["fulltext"]
	wordList = fulltext.split()
	worddictionary = {}
	for word in wordList:
		if word in worddictionary:
			worddictionary[word] += 1
		else:
			worddictionary[word] = 1

	sorted_words = sorted(worddictionary.items(), key=operator.itemgetter(1), reverse=True)



	return render(request, "count.html", {'fulltext':fulltext, 'count':len(wordList), 'sorted_words':sorted_words})