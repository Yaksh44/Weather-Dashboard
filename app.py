"""
It is an weather datd that tells the current data and forscast for next 30 days.
"""
import flask
from flask.views import MethodView
from index import Index
from current_weather import current_weather
from forecast import forecast

app = flask.Flask(__name__)       # our Flask app

"""
Landing page for the application
"""

app.add_url_rule('/',
                 view_func=Index.as_view('index'),
                 methods=["GET"])

"""
/name redirects to search airport by name
"""
app.add_url_rule('/current_weather',
                 view_func=current_weather.as_view('current_weather'),
                 methods=['GET', 'POST'])

"""
/name redirects to search airport by iata/icao code
"""
app.add_url_rule('/forecast',
                 view_func=forecast.as_view('forecast'),
                 methods=['GET', 'POST'])


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8000, debug=True)