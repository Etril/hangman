import requests
from bs4 import BeautifulSoup

r=requests.get("https://forecast.weather.gov/MapClick.php?lon=-114.0380859375&lat=34.74161249883173#.YHPj7egzaUk")

soup=BeautifulSoup(r.content, "html.parser")

forecast=soup.find_all(class_="tombstone-container")

period= forecast[0].find(class_="period-name")
desc= forecast[0].find(class_="short-desc")
temp= forecast[0].find(class_="temp")

def weather_get(x):
    return ((forecast[x].find(class_="period-name").get_text(), (forecast[x].find(class_="short-desc").get_text())))

print (", ".join(weather_get(1)))
