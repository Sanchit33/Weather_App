#importing BeautifulSoup Libary
from bs4 import BeautifulSoup
#import request module
import requests

#header user agent is the string that allow the server to identify the OS and application
headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)     AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3'}

#defining the the weather function
def weather(city):
    #replace the space with + operator
    city = city.replace("","+")
    #requesting the information from the provided URL and storing it in rq
    rq=requests.get(f'https://www.google.com/search?q={city}&oq={city}&aqs=chrome.0. i635i39l2j0l4j46j690.6128j1j7&sourceid=chrome&ie=UTF-8',headers=headers)
    #search the information from google
    print('Searching in Google\n')
    #navigate to that particular website extract and store into soup variable
    soup = BeautifulSoup(rq.text,'html.parser')
    #gets the information of location
    location = soup.select('#wob_loc')[0].getText().strip()
    #gets the informatin of the time
    time = soup.select('#wob_dts')[0].getText().strip()
    #gets the desired information
    info = soup.select('#wob_dc')[0].getText().strip()
    #gets the weather information
    weather = soup.select('#wob_tm')[0].getText().strip()

    #prints the location
    print(location)
    #print time
    print(time)
    #print information
    print(info)
    #prints the weather in degree celcius
    print(weather+"°C")

    #taking input from the user which the name of the city
print("Enter The City Name")
city= input("Enter The City Name:")

    #Concatenating the city name and weather
city = city+'weather'

    #passing the city object to weather function
weather(city) 

