"""
Python list model
"""
from model import Model

class model(Model):
    def __init__(self):
        self.current_weather = ""
        self.forecast = ""

    def returncurrent_weather(self):
        """
        Returns current_weather entered by the user
        :return: current wether
        """
        return self.current_weather

    def returnforecast(self):
        """
        Returns forecast entered by the user
        :return: forecast
        """
        return self.forecast

    def insertcurrent_weather(self, current_weather):
        """
        Stores current weather
        :return: True
        """
        self.current_weather = current_weather
        return True

    def insertforecast(self, forecast):
        """
        Stores forecast
        :return: True
        """
        self.forecast = forecast
        return True
