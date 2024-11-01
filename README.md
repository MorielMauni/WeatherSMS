WeatherSMS

WeatherSMS is a Python-based application that fetches real-time weather information and sends it to your phone via SMS. This tool is perfect for staying updated on weather conditions, whether for daily planning or emergency preparedness.

Features
- Fetches current weather information for a specified location.
- Sends weather updates via SMS using a messaging API.
- Customizable weather alerts based on conditions like temperature, rain, or storms.
  
Installation
1. Clone this repository:
   ```
   git clone https://github.com/MorielMauni/WeatherSMS.git
   ```
2. Install the required packages:
   ```
   pip install -r requirements.txt
   ```

Setup
1. Obtain an API key from a weather service provider [OpenWeatherMap](https://openweathermap.org/api).
2. Get credentials from an SMS provider [twilio](https://www.twilio.com) for SMS functionality.
3. Configure your API keys in the project settings or environment variables.

Usage
Run the main script to receive SMS updates with the latest weather for your location:
   ```
   python weather_sms.py
   ```

Contact
For questions, feel free to contact me at [morielmauni@gmail.com].
