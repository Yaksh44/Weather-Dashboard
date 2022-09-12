from flask import Flask, redirect, request, url_for, render_template
from flask.views import MethodView
from model_pylist import model
import requests
import json

model = model()
class current_weather(MethodView):
    def get(self):
        print("\n\n\nthis is the arguement\n\n\n")
        print(model.current_weather)
        url = "https://community-open-weather-map.p.rapidapi.com/weather"
        querystring = {"q":model.current_weather}
        headers = {
            'x-rapidapi-host': "community-open-weather-map.p.rapidapi.com",
            'x-rapidapi-key': "13a0705f21mshe0dcec1f888d790p1e8866jsn8230eeedde2e"
        }
        response = requests.request("GET", url, headers=headers, params=querystring)
        print("this is the response")
        print(response.text)
        entries = []
        if(len(response.text) > 0) :
            res = json.loads(response.text)
            print(res)
            if ('coord' in res):
                print(res)
                entries = [
                    dict(coordinates_long=res['coord']['lon'], coordinates_lat=res['coord']['lat'], weather=res['weather'][0]['main'],
                     weather_description=res['weather'][0]['description'], temprature=res['main']['temp'], feelslike=res['main']['feels_like'], 
                     temprature_min=res['main']['temp_min'], temprature_max=res['main']['temp_max'], pressure=res['main']['pressure'], 
                     humidity=res['main']['humidity'], visibility=res['visibility'], wind_speed=res['wind']['speed'], deg=res['wind']['deg'], 
                     gust=res['wind']['gust'], sunrise=res['sys']['sunrise'], sunset=res['sys']['sunset'] ) ]
        print(entries)
        return render_template('current_weather.html', entries=entries)
    
    
    def post(self):
        model.insertcurrent_weather(request.form['current_weather'])
        return redirect(url_for('current_weather'))