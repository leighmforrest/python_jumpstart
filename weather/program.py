import bs4
import requests
import collections


WeatherReport = collections.namedtuple('WeatherReport', 'location, temp, condition')


def main():
    # print the header
    print_header()
    # get zip code from user
    zip_code = input('What zipcode do you want the weather for (19125)? ')
    zip_code = zip_code or '19125'
    # get html from the web
    html = get_html_from_web(zip_code)
    # parse the html
    forecast = get_weather_from_html(html)
    # display for the forecast
    print(f"The temperature is {forecast.temp} in {forecast.location}, and the condition is {forecast.condition}.")


def print_header():
    print('--------------------------------------------------')
    print("                   WEATHER APP")
    print('--------------------------------------------------')
    print()


def get_html_from_web(zipcode):
    url= f'http://www.wunderground.com/weather-forecast/{zipcode}'
    response = requests.get(url)
    return response.text


def get_weather_from_html(html):
    soup = bs4.BeautifulSoup(html, 'html.parser')
    location = soup.find('h1').get_text()
    temperature = soup.find('span', attrs={"class":"wu-value"}).get_text()
    condition = soup.find('div', attrs={"class":"conditions-extra"}).find('p').get_text()

    # cleanup values
    location = cleanup_text(location)
    temperature = cleanup_text(temperature) + '\u00B0F'
    condition = cleanup_text(condition)

    report = WeatherReport(location=location, temp=temperature, condition=condition)
    return report


def cleanup_text(text):
    if not text:
        return text
    text = text.strip()
    return text


if __name__ == '__main__':
    main()