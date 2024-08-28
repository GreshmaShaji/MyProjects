
def display_weather(data):

    city = data['name']
    temp = data['main']['temp']
    description = data['weather'][0]['description']
    humidity = data['main']['humidity']

    print(f"Weather in {city}")
    print(f"Temperature: {temp}")
    print(f"Condition: {description}")
    print(f"Humidity: {humidity}")