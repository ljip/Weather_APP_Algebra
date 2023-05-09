from flask import Flask, render_template, request

from controllers.graph_controller import GraphController
from controllers.weather_api_controller import WeatherApiController


app = Flask(__name__)


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/today", methods=["POST"])
def weather_today():
    city = request.form["city"].capitalize()
    forecast_data = WeatherApiController.get_forecast_data_one_day(city)
    image_url = GraphController.get_graph_one_day(forecast_data)

    return render_template("today.html", city=city, image_url=image_url)


@app.route("/three-days", methods=["POST"])
def weather_three_days():
    city = request.form["city"].capitalize()
    forecast_data = WeatherApiController.get_forecast_data_three_days(city)
    image_url = GraphController.get_graph_multiple_days(forecast_data)
    
    return render_template("multiple-days.html", city=city, image_url=image_url)


@app.route("/seven-days", methods=["POST"])
def weather_seven_days():
    city = request.form["city"]
    forecast_data = WeatherApiController.get_forecast_data_seven_days(city)
    image_url = GraphController.get_graph_multiple_days(forecast_data)
    
    return render_template("multiple-days.html", city=city, image_url=image_url)

@app.route("/contact")
def contact():
    return render_template("contact.html")


if __name__ == "__main__":
    app.run(debug=True)
