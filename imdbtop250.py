import requests
from bs4 import  BeautifulSoup

url = "https://www.imdb.com/chart/top/"
response = requests.get(url)

html_content = response.content

soup = BeautifulSoup(html_content,"html.parser");

titles = soup.findAll("td", {"class":"titleColumn"})
ratings = soup.findAll("td",{"class":"ratingColumn imdbRating"})


inp_rating = float(input("Lowest Rating? : "))


for title, rating in zip(titles,ratings):
    title = title.text
    rating = rating.text
    title = title.strip()
    title = title.replace("/n","")
    rating = rating.strip()
    rating = rating.replace("/n","")
    
    if(float(rating)>=inp_rating):
        print("Title: ", title)
        print("Rating: ", rating)