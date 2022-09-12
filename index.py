from flask import render_template
from flask.views import MethodView

class Index(MethodView):
    def get(self):
        """
        Returns index page when requested
        """
        return render_template('index.html')