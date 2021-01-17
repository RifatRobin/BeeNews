from django.shortcuts import render
from django.http import HttpResponse
from newsapi.newsapi_client import NewsApiClient
import http.client
import urllib.parse
# Create your views here.


def home(request):
    # newsMS = NewsApiClient(api_key="731959001da70cef83c56d8402da34de") #mediastack
    newsapis = NewsApiClient(
        api_key="9a52ccb1d31d4517ac61e3c57862b030")  # newapi website
    headlines = newsapis.get_top_headlines(
        sources='bbc-news', language='en')
    articles = headlines['articles']
    des = []
    news = []
    img = []
    con = []
    for i in range(len(articles)):
        newarticles = articles[i]
        news.append(newarticles['title'])
        des.append(newarticles['description'])
        img.append(newarticles['urlToImage'])
        con.append(newarticles['content'])
    newlist = zip(news, des, img, con)
    context = {"newlist": newlist}
    return render(request, 'index.html', context)


def abc(request):
    # newsMS = NewsApiClient(api_key="731959001da70cef83c56d8402da34de") #mediastack
    newsapis = NewsApiClient(
        api_key="9a52ccb1d31d4517ac61e3c57862b030")  # newapi website
    headlines = newsapis.get_top_headlines(
        sources='abc-news', language='en')
    articles = headlines['articles']
    des = []
    news = []
    img = []
    con = []
    for i in range(len(articles)):
        newarticles = articles[i]
        news.append(newarticles['title'])
        des.append(newarticles['description'])
        img.append(newarticles['urlToImage'])
        con.append(newarticles['content'])
    newlist = zip(news, des, img, con)
    context = {"newlist": newlist}
    return render(request, 'index.html', context)


def cnn(request):
    # newsMS = NewsApiClient(api_key="731959001da70cef83c56d8402da34de") #mediastack
    newsapis = NewsApiClient(
        api_key="9a52ccb1d31d4517ac61e3c57862b030")  # newapi website
    headlines = newsapis.get_top_headlines(
        sources='cnn', language='en')
    articles = headlines['articles']
    des = []
    news = []
    img = []
    con = []
    for i in range(len(articles)):
        newarticles = articles[i]
        news.append(newarticles['title'])
        des.append(newarticles['description'])
        img.append(newarticles['urlToImage'])
        con.append(newarticles['content'])
    newlist = zip(news, des, img, con)
    context = {"newlist": newlist}
    return render(request, 'index.html', context)


def espn(request):
    # newsMS = NewsApiClient(api_key="731959001da70cef83c56d8402da34de") #mediastack
    newsapis = NewsApiClient(
        api_key="9a52ccb1d31d4517ac61e3c57862b030")  # newapi website
    headlines = newsapis.get_top_headlines(
        sources='espn', language='en')
    articles = headlines['articles']
    des = []
    news = []
    img = []
    con = []
    for i in range(len(articles)):
        newarticles = articles[i]
        news.append(newarticles['title'])
        des.append(newarticles['description'])
        img.append(newarticles['urlToImage'])
        con.append(newarticles['content'])
    newlist = zip(news, des, img, con)
    context = {"newlist": newlist}
    return render(request, 'index.html', context)


def espnCrick(request):
    # newsMS = NewsApiClient(api_key="731959001da70cef83c56d8402da34de") #mediastack
    newsapis = NewsApiClient(
        api_key="9a52ccb1d31d4517ac61e3c57862b030")  # newapi website
    headlines = newsapis.get_top_headlines(
        sources='espn-cric-info', language='en')
    articles = headlines['articles']
    des = []
    news = []
    img = []
    con = []
    for i in range(len(articles)):
        newarticles = articles[i]
        news.append(newarticles['title'])
        des.append(newarticles['description'])
        img.append(newarticles['urlToImage'])
        con.append(newarticles['content'])
    newlist = zip(news, des, img, con)
    context = {"newlist": newlist}
    return render(request, 'index.html', context)


def gnews(request):
    # newsMS = NewsApiClient(api_key="731959001da70cef83c56d8402da34de") #mediastack
    newsapis = NewsApiClient(
        api_key="9a52ccb1d31d4517ac61e3c57862b030")  # newapi website
    headlines = newsapis.get_top_headlines(
        sources='google-news', language='en')
    articles = headlines['articles']
    des = []
    news = []
    img = []
    con = []
    for i in range(len(articles)):
        newarticles = articles[i]
        news.append(newarticles['title'])
        des.append(newarticles['description'])
        img.append(newarticles['urlToImage'])
        con.append(newarticles['content'])
    newlist = zip(news, des, img, con)
    context = {"newlist": newlist}
    return render(request, 'index.html', context)
