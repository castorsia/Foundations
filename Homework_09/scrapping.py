
# coding: utf-8

# In[69]:


from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support.ui import WebDriverWait
import requests

import pandas as pd


# In[40]:


url = "https://www.reuters.com/"
driver = webdriver.Chrome()
driver.get(url)


# In[41]:


headlines = driver.find_elements_by_class_name('story-title')
#titles = driver.find_elements_by_class_name(class = 'headline small normal-style text-align-inherit')
for headline in headlines:
    print(headline.text)
len(headlines)


# In[44]:


stories = driver.find_elements_by_class_name('story')


# In[45]:


newslist = driver.find_elements_by_class_name('story')
#newslist.text

for url in newslist:
    url = url.find_element_by_tag_name('a').get_attribute('href')
    print(url)
#urls = newslist.find_element_by_tag_name('a').get_attribute('href')

for title in newslist:
    title = title.text
    print(title)
    
for summary in newslist:
    summary = summary.find_element_by_class_name('story-content').text
    print(summary)
    
for timestamp in newslist:
    timestamp = timestamp.find_element_by_class_name("timestamp").text
    print(timestamp)


# In[46]:


datapoints = []

newslist = driver.find_elements_by_class_name('story')
for story in newslist:
#     print("---------")
    datapoint = {}
    
    
    title = story.text
    datapoint['title'] = title
    datapoint['url'] = story.find_element_by_tag_name('a').get_attribute('href')
    datapoint['summary'] = story.find_element_by_class_name('story-content').text
    datapoint['timestamp'] = story.find_element_by_class_name("timestamp").text
#     print(datapoint)
    datapoints.append(datapoint)
    
datapoints


# In[53]:


df = pd.DataFrame(datapoints)


# In[54]:


pd.set_option('display.max_colwidth', -1)


# In[55]:


df


# In[57]:


import datetime
right_now = datetime.datetime.now()
right_now
#time = str(right_now.strftime("%Y-%m-%d-%H-%M")

#name = "briefing-"+str(right_now.strftime("%Y-%m-%d-%H-%M"))
#name
df.to_csv("briefing.csv", index=False)


# In[70]:


response = requests.post(
        "https://api.mailgun.net/v3/sandboxc4d2a1094a8d414fa2b50867663d5394.mailgun.org/messages",
        auth=("api", "c9028651bc11b5b66748bbb223f8ab16-0470a1f7-df132c8b"),
        files=[("briefing.csv", open("briefing.csv"))],
        data={"from": "Mailgun Sandbox <postmaster@sandboxc4d2a1094a8d414fa2b50867663d5394.mailgun.org>",
              "to": "Ilias Stathatos <is2594@columbia.edu>",
              "subject": "YOUR BRIEFING AT " + str(right_now.strftime("%H-%M")),
              "text": "NEWS"})
response.text

