import pandas as pd # type: ignore
import requests # type: ignore

def get_weather(city, api_key):
    url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric"
    response = requests.get(url)

    if response.status_code == 200:
        data = response.json()

        return{
            'City': city,
            'Temperature (C)': data['main']['temp'],
            'Weather': data['weather'][0]['description'],
            'Humidity (%)': data['main']['humidity'],
            'Wind Speed (m/s)': data['wind']['speed']
        }
    else:
        print(f"Error {response.status_code}: Unable to fetch data")
        return None


def main():
    api_key = '4feb4318ebeb1bfbd2af012e233ffbbf'

    cities = ['Kathmandu', 'London', 'New York']
    weather_data = []
    for city in cities:
        data = get_weather(city, api_key)
        if data:
            weather_data.append(data)


    df = pd.DataFrame(weather_data)
    df.to_csv('weather_data.csv', index=False)
    print("Weather data saved to a CSV File!!")

if __name__ == '__main__':
    main()
