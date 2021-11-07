from app import app
import urllib.request, json
from .models import news
from urllib.request import Request, urlopen

News = news.News

# Getting api key
api_key = app.config['NEWS_API_KEY']
base_url_news = app.config['NEWS_API_BASE_URL']
base_url_articles = app.config['NEWS_API_ARTICLES_URL']

def get_news():
    '''
    Function that gets the json response to url request
    '''
    # get_movies_url = base_url.format(category,api_key)              #new
    get_news_url= 'https://newsapi.org/v2/news?apiKey=0de28d09fb894c7bbc3d053f21fdbc4f'
    
    # print(get_news_url)
    with urllib.request.urlopen(get_news_url) as url:
        get_news_data = url.read()
        get_news_response = json.loads(get_news_data)
        news_results = None
        if get_news_response['news']:
            news_results_list = get_news_response['news']
            news_results = process_results(news_results_list)
    return news_results

def process_results(news_list):
    '''
    function to process results and transform them to a list of objects
    Args:
        news_list:dictionary cotaining news details
    Returns:
        news_results: A list of news objects
    '''
    news_results = []
    for news_item in news_list:
        id = news_item.get('id')
        name = news_item.get('name')
        description = news_item.get('description')
        url = news_item.get('url')
        category=news_item.get('category')
        if id:
            news_object = news(id,name,description,url,category)
            news_results.append(news_object)
    return news_results





