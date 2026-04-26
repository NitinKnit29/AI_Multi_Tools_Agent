from pydantic import BaseModel, Field
import os
import requests
from langchain.tools import tool
from langchain_community.tools import DuckDuckGoSearchRun
from langchain_community.utilities import DuckDuckGoSearchAPIWrapper

# ── Tools defined at module level (outside cache) ────────
search_wrapper = DuckDuckGoSearchAPIWrapper()
search = DuckDuckGoSearchRun(api_wrapper=search_wrapper)

class WebSearchArgs(BaseModel):
    query: str = Field(description="The search query string. Example: 'who won IPL 2019'")

@tool(args_schema=WebSearchArgs)
def web_search(query: str) -> str:
    """Search the internet for current events, facts, or up-to-date information.
    Input: query (string) - the search query.
    Output: search results as text."""
    return search.run(query)

class CalculatorArgs(BaseModel):
    expression: str = Field(description="A valid Python math expression. Example: '2+2' or '100*0.15'")

@tool(args_schema=CalculatorArgs)
def calculator(expression: str) -> str:
    """Perform mathematical calculations.
    Input: expression (string) - a valid Python math expression.
    Output: the result of the calculation."""
    try:
        return str(eval(expression))
    except Exception as e:
        return f"Error: {e}"

class WeatherArgs(BaseModel):
    city: str = Field(description="Name of the city. Example: 'Delhi', 'Mumbai', 'London'")

@tool(args_schema=WeatherArgs)
def get_weather(city: str) -> str:
    """Get the current weather for a city.
    Input: city (string) - the name of the city.
    Output: weather information including temperature, humidity, etc."""
    api_key = os.getenv('OPENWEATHER_API_KEY')
    if not api_key:
        return "Error: OpenWeatherMap API key not found."
    url = "https://api.openweathermap.org/data/2.5/weather"
    params = {"q": city, "appid": api_key, "units": "metric"}
    try:
        response = requests.get(url, params=params)
        data = response.json()
        if response.status_code != 200:
            return f"Error: {data.get('message', 'Unknown error')}"
        weather = data["weather"][0]["description"]
        temp = data["main"]["temp"]
        feels_like = data["main"]["feels_like"]
        humidity = data["main"]["humidity"]
        wind_speed = data["wind"]["speed"]
        return (
            f"Weather in {data['name']}, {data['sys']['country']}: "
            f"{weather.capitalize()}, {temp}°C (feels like {feels_like}°C), "
            f"humidity {humidity}%, wind {wind_speed} m/s."
        )
    except Exception as e:
        return f"Error fetching weather: {e}"
