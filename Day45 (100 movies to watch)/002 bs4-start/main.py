from bs4 import BeautifulSoup
import requests
#Scraping from live website

response= requests.get("https://news.ycombinator.com/news")
yc_web_page= response.text

soup= BeautifulSoup(yc_web_page, "html.parser")
articles= soup.find_all(name= "a", class_= "storylink")
article_text= []
article_links= []
for article_tag in articles:
    text= article_tag.getText()
    link= article_tag.get("href")
    article_text.append(text)
    article_links.append(link)


article_upvote= [int(score.getText().split()[0]) for score in soup.find_all(name= "span", class_= "score")]
largest_number= max(article_upvote)
largest_index= article_upvote.index(largest_number)
print(article_upvote)
print(article_text)
print(article_links)














"""
with open("website.html", encoding="utf-8") as file:
    content = file.read()

soup = BeautifulSoup(content, "html.parser")
print(soup.title)

print(soup.title.string)


print(soup.a)

all_anchor_tags = soup.find_all(name= "a")


for tag in all_anchor_tags:
    # print(tag.getText())
    print(tag.get("href"))

#calling particular tag by id attribute
heading= soup.find(name= "h1", id= "name")
print(heading)

#calling particular tag by class attribute
section_heading= soup.find(name="h3",class_= "heading")
print(section_heading.getText())

#to call the enchor tag <a>
compnay_url= soup.select_one(selector= "p a")
print(compnay_url)

#we can also use class and ID in css selector
name= soup.select_one(selector= "#name")
print(name)

headings= soup.select(".heading")
print(headings)"""