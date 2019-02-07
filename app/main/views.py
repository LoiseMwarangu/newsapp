from flask import render_template,request,redirect,url_for
from . import main
from  ..request import get_news

# Views
@main.route('/')
def index():
    '''
    View root page function that returns the page and and its data
    '''

    # Getting breaking news source

    health = get_news('gb','health')
    business = get_news('au' ,'business')
    entertainment = get_news('za','entertainment')
    science = get_news('lv','science')
    sports = get_news('gb','sports')
    technology = get_news ('us','technology')


    title = "Updates for today"
    return render_template('index.html', title = title, technology = technology, sports=sports,science=science,health=health,business=business,entertainment=entertainment)