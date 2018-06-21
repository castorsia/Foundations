
# coding: utf-8

# In[6]:


import requests


# In[7]:


url = 'https://api.darksky.net/forecast/58a87e3dc181162cad1d8cdac799db33/40.7128,-74.0060'
response = requests.get(url)
newyork = response.json()


# In[8]:


print(newyork['timezone'])


# In[9]:


newyork['daily']['icon']


# In[21]:


url = 'https://api.darksky.net/forecast/58a87e3dc181162cad1d8cdac799db33/37.9841,23.728?units=si'
response = requests.get(url)
newyork = response.json()

newyork_daily = newyork['daily']
#print(newyork_daily['data'][0])
#print(newyork_daily.keys())
next_day = newyork_daily['data'][0]
#print(next_day)
#print(next_day.keys())
new_york_currently = newyork['currently']

temp_feel = ''
rain_warning = ''
if newyork['daily']['icon'] == 'rain':
    rain_warning = 'RAIN WARNING'

if newyork['daily']['data'][0]['temperatureMax'] > 25:
    temp_feel = 'hot'
elif newyork['daily']['data'][0]['temperatureMax'] > 15:
    temp_feel = 'mild'
else:
    temp_feel = 'cold'



weather = "Right now it is " + str(new_york_currently["temperature"]) + " degrees and today will be " + str.lower(next_day['summary'])+". Today will be " + temp_feel + " with a high of " + str(next_day['temperatureHigh']) + " and a low of " + str(next_day['temperatureLow']) + rain_warning
print(weather)


# In[30]:


import datetime
right_now = datetime.datetime.now()
right_now


response = requests.post(
        "https://api.mailgun.net/v3/sandboxc4d2a1094a8d414fa2b50867663d5394.mailgun.org/messages",
        auth=("api", "API"),
        data={"from": "Mailgun Sandbox <postmaster@sandboxc4d2a1094a8d414fa2b50867663d5394.mailgun.org>",
              "to": "Ilias Stathatos <is2594@columbia.edu>",
              "subject": "8AM Weather forecast: "+ str(right_now.strftime("%Y-%m-%d")),
              "text": weather}) 
response.text

