# Foreca CLI

foreca.weather.forecast.cli is a Python 3.5+ command line interface for Foreca weather forecast


## Installation

Use the package manager [pip](https://pip.pypa.io/en/stable/) to install foreca.weather.forecast.cli

`$ pip install --user git+https://github.com/evicekcz/foreca-weather-forecast.git`

**Note:** After installation, it may be necessary to add the directory with scripts into the PATH environment variable


## Usage

### Simple usage

```
$ foreca-cli [OPTIONS]
```

Options:
```
--city <TEXT>  Weather in specified city. (Try '--city help' to display all possibilities)  [required]
--date <TEXT>  Forecast for specified day in format DD.MM.YYYY. (Without this parameter, the current weather will be displayed)
--help         Show this message and exit.
```

## Contributing

Pull requests are welcome.


## License

[MIT](https://choosealicense.com/licenses/mit/)
