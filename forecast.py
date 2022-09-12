from flask import Flask, redirect, request, url_for, render_template
from flask.views import MethodView
from model_pylist import model
import requests
import json

model = model()

# @app.route('/forecast', methods=['GET', 'POST']) 
class forecast(MethodView):
    def get(self):
        url = "https://community-open-weather-map.p.rapidapi.com/climate/month"
        querystring = {"q":model.forecast}
        headers = {
            'x-rapidapi-host': "community-open-weather-map.p.rapidapi.com",
            'x-rapidapi-key': "13a0705f21mshe0dcec1f888d790p1e8866jsn8230eeedde2e"
        }
        response = requests.request("GET", url, headers=headers, params=querystring)
        print("hello")
        print(response.text)
        res = json.loads(response.text)
        if('city' in res):
            a = res['city']['name']
            b = res['city']['coord']['lon']
            c = res['city']['coord']['lat']
            
        
        entries = []
        if(len(response.text) > 0) :
            res = json.loads(response.text)
            if ('list' in res):
                arr = res['list']
                entries = [
                    dict(date=row['dt'], humidity=row['humidity'], pressure=row['pressure'], average_temp=row['temp']['average'], average_temp_max=row['temp']['average_max'], 
                    average_temp_min=row['temp']['average_min'], average_temp_recordmax=row['temp']['record_max'], average_temp_recordmin=row['temp']['record_min'], 
                    wind_speed=row['wind_speed'], name=a, lon=b, lat=c) for row
                    in
                    arr]
        return render_template('forecast.html', entries=entries, name=model.forecast )
    #get(self="abc"); 
    def post(self):
        print(request.form['forecast'])
        model.insertforecast(request.form['forecast'])
        return redirect(url_for('forecast'))       