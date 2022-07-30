import bs4
import urllib.request as url

path = "https://www.flipkart.com/search?q=iphone+12+pro&as=on&as-show=on&otracker=AS_Query_HistoryAutoSuggest_1_1_na_na_na&otracker1=AS_Query_HistoryAutoSuggest_1_1_na_na_na&as-pos=1&as-type=HISTORY&suggestionId=iphone+12+pro&requestId=e58be88f-0bb0-484c-a5ef-70163cc256bc&as-backfill=on" 
response = url.urlopen(path)
page = bs4.BeautifulSoup(response)
title = page.find('div', {'class' : '_4rR01T'})
print("Product Title :",title.text)
price = page.find('div', {'class' : '_30jeq3 _1_WHN1'})
print("Price :",price.text)
