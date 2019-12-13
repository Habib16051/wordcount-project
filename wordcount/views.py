from django.http import HttpResponse
from django.shortcuts import render
import operator
def homepage(request):

    return render(request, 'love.html')

def about(request):

    return render(request, 'about.html')
def count(request):
    fulltext = request.GET['fulltext']
    wordlist = fulltext.split()
   
    dictionary = {}

    for word in wordlist:
        if word in dictionary:
            #increase
            dictionary[word] += 1
        else:
            #addtothedictionary
            dictionary[word] = 1

    sortedwords =sorted (dictionary.items(), key = operator.itemgetter(1), reverse = True)

    return render(request, 'count.html',{'fulltext':fulltext, 'count':len(wordlist), 'sortedwords':sortedwords})
