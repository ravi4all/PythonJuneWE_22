import bs4
import urllib.request as url

path = "https://www.flipkart.com/search?q=iphone+12+pro&as=on&as-show=on&otracker=AS_Query_HistoryAutoSuggest_1_1_na_na_na&otracker1=AS_Query_HistoryAutoSuggest_1_1_na_na_na&as-pos=1&as-type=HISTORY&suggestionId=iphone+12+pro&requestId=e58be88f-0bb0-484c-a5ef-70163cc256bc&as-backfill=on" 
response = url.urlopen(path)
# lxml - library XML - Xtensible Markup Language
page = bs4.BeautifulSoup(response, 'lxml')
title = page.find_all('div', {'class' : '_4rR01T'})
price = page.find_all('div', {'class' : '_30jeq3 _1_WHN1'})

for i in range(len(title)):
    print("Title ::",title[i].text)
    print("Price ::",price[i].text)
    print("*" * 50)
