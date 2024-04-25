import google.generativeai as genai
import os

# Replace 'YOUR_API_KEY' with your actual API key obtained from Google Cloud Platform
api_key = os.environ["AIzaSyDKN20GfR93SRXToC-DdI6I2A6a9FHP82w"]


# Configure the library with your API key
genai.configure(api_key=api_key)

# Now you can use various functions from the library
model = genai.GenerativeModel('gemini-pro')
response = model.generate_content('suggest names for a stock analyzer bot')
print(response.text)
