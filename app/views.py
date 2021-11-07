from flask import render_template
from app import app
from .request import get_news
from .forms.forms import NewsSearchForm

# Views


@app.route('/')
def index():

    '''
    View root page function that returns the index page and its data
    '''
    newsform = NewsSearchForm()
   
    # Getting popular news
    # business_news = get_news()
    
    # print(business_news)
    title = 'Home - Welcome to The best News Review Website Online'
    return render_template('index.html', news_search_forms = newsform) #,business_news = business_news

@app.route('/search_news')
def search():
    return 'search'


@app.route('/news/<int:news_id>')
def news(news_id):

    '''
    View news page function that returns the news details page and its data
    '''
    news = 'News-Highlights'
    return render_template('news.html',id = news_id)

