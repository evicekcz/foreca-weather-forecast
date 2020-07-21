import json
import re

import demjson
import requests
import click


class Forecast:
    def __init__(self, config_path: str, input_city: str, timeout: int = 60):
        self.config = self._get_config(config_path)

        url = None
        for region in self.config:
            for city in self.config[region]:
                if input_city == city:
                    url = self.config[region][city]

        if input_city == "help":
            click.secho("Available cities are:", fg="green")
            for region in self.config:
                click.secho(region, fg="yellow")
                for city in self.config[region]:
                    click.echo(f"  {city}")
            exit()

        if not url:
            click.secho(f"The specified city '{input_city}' does not exist.", fg="red")
            exit()

        response = requests.get(url, timeout=timeout)
        response.raise_for_status()

        self.html_content = response.text

    def _get_config(self, config_path: str) -> dict:
        json_file = open(config_path, "r")
        data = json.load(json_file)

        return data

    def get_actual_weather(self) -> dict:

        temperature_result = re.search(
            r"<span>Pocitová&nbsp;teplota</span></div><div class=\"right\">(\+\d+)", self.html_content, re.IGNORECASE,
        )
        humidity_result = re.search(
            r"<span>Vlhkost</span></div><div class=\"right\">(\d\d.\d%)</div>", self.html_content, re.IGNORECASE,
        )

        output = {}
        if temperature_result:
            output["temperature"] = temperature_result.group(1)
        else:
            output["temperature"] = "N/A"

        if humidity_result:
            output["humidity"] = humidity_result.group(1)
        else:
            output["humidity"] = "N/A"

        return output

    def get_ten_days_forecast(self) -> dict:
        result = re.search(r"var daily_data =  ([^;]+)", self.html_content, re.IGNORECASE)
        if not result:
            return "N/A"

        output = {}
        forecast_result = demjson.decode(result.group(1))
        for timestamp in forecast_result["10d"]:
            day = forecast_result["10d"][timestamp]["du"]
            output[day] = {}

            output[day]["tmax"] = forecast_result["10d"][timestamp]["tmax"]
            output[day]["tmin"] = forecast_result["10d"][timestamp]["tmin"]
            output[day]["description"] = forecast_result["10d"][timestamp]["wx"]
            output[day]["day_of_week"] = forecast_result["10d"][timestamp]["ds"]

        return output
