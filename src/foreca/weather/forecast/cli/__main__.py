import datetime
import os

import click

from foreca.weather.forecast.cli.foreca import Forecast


@click.command()
@click.option(
    "--city",
    "input_city",
    metavar="<TEXT>",
    required=True,
    help="Weather in specified city. (Try '--city help' to display all possibilities)",
)
@click.option(
    "--date",
    "input_date",
    metavar="<TEXT>",
    help="Forecast for specified day in format DD.MM.YYYY. (Without this parameter, the current weather will be displayed)",
)
def __main__(input_city, input_date):
    config_path = os.path.join(os.path.dirname(os.path.realpath(__file__)), "config.json")
    forecast = Forecast(config_path, input_city)

    if input_date:
        ten_days_forecast_result = forecast.get_ten_days_forecast()
        date_obj = datetime.datetime.strptime(input_date, "%d.%m.%Y")
        ftime = date_obj.strftime("%Y-%m-%d")

        if ftime in ten_days_forecast_result:
            click.echo(ten_days_forecast_result[ftime])
        else:
            click.secho("The specified day exceeded the 10-day forecast limit.", fg="red")
    else:
        actual_weather_result = forecast.get_actual_weather()
        click.echo(actual_weather_result)
