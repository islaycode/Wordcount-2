from django.http import HttpResponse
from django.shortcuts import render
import operator

def homepage(request):
    return render(request,'home.html')

def contact(request):
    return HttpResponse("<h1>This is contact page<h1>")   

def count(request):
    data = request.GET['fulltextarea']
    word_list=data.split()
    list_length=len(word_list)
    
    worddictionary = {}

    for word in word_list:
        if word in worddictionary:
            #Increase
            worddictionary[word] += 1
        else:
            #add to the dictionary
            worddictionary[word] = 1

    sortedwords = sorted(worddictionary.items(), key=operator.itemgetter(1), reverse=True)

    return render(request, 'count.html',{'fulltext':data,'words':list_length,'dict':sortedwords})
