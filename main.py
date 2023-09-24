import requests
from send_email import send_email
import os

# url = "https://finance.yahoo.com"

api_key = os.getenv("NEWS_API_KEY")
url = "https://newsapi.org/v2/everything?"\
    "q=tesla&sortBy=publishedAt&apiKey"\
        "="+api_key



request = requests.get(url)
content = request.json()
message = """\
Subject: News

"""
for index,article in enumerate(content['articles']):
    news = f"""{index+1}.{article["title"]}\n\
    {article["description"]}\n\n
"""
    message+=news
    # message+=article["title"]+"\n"+article["description"]+2*"\n"

message = message.encode("utf-8")
send_email(message)