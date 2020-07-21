from setuptools import setup

setup(
    setup_requires=["setuptools >= 40", "wheel >= 0.32"],
    entry_points={"console_scripts": ["foreca-cli = foreca.weather.forecast.cli.__main__:__main__",]},
)
