from flask import Flask, request
import json
import random
import requests

app = Flask(__name__)
app.debug = True

@app.route('/webhook',methods=['POST','GET'])
def index():
    #reply = '{"FulfillmentMessages": [ {"text": {"text": ["The Temperature is 21C"] } } ]}'

    body = request.json
    city=body['queryResult']['parameters']['geo-city']
    country= body['queryResult']['parameters']['geo-country']

    #temperature = str(random.randint(-20,35))

    #reply = '{"fulfillmentMessages": [ {"text": {"text": ["The temperature in'+city+","+country+'it is'+temperature+'"] } } ]}'
    api_url='https://api.openweathermap.org/data/2.5/weather?q='+city+'&units=metric&appid=b0443628d04890fd1a268ea5eaa0da40'
    headers = {'Content-Type': 'application/json'}
    response = request.get(api_url,headers=headers)
    r=response.json()
    print(api_url)
    weather = str(r["weather"][0]["description"])
    temp = str(int(r['main']['temp']))
    humidity = str(r["main"]["humidity"])
    pressure = str(r["main"]["pressure"])
    windspeed = str(r["Wind"]["speed"])
    windDirection = str(r["wind"]["deg"])
    country = str(r["sys"]["country"])

    reply = '{"fulfillmentMessages": [ {"text": {"text": ["The temperature in'+city+","+country+'it is'+temp+'"] } } ]}'

    return reply