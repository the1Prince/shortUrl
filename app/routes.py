import json
from flask import url_for,render_template,request

from app import app
from app.forms import ShortenForm
from app.shorten import shorten


@app.route('/')
@app.route('/index', methods=['GET','POST'])
def index():
    form=ShortenForm()
    
    return render_template('index.html',title='Home',form=form)


@app.route('/v1/shorten', methods=['GET'])
def shortenUrl():
    '''this function calls on the shortener function in the shorten module to generate the short url.'''
    print('hu')
    #conv=str(request.json['url'])
    conv=request.args.get('url')
    print(conv)
    
    short=shorten.shortener(conv)
    return(short)
