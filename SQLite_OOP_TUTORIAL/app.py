from flask import Flask, jsonify, request
from repositories.urls import save, list_categories, list_urls

app = Flask(__name__)

@app.route('/add',methods= ['POST'])
def add():
    req = request.get_json()
    category = req['category']
    url = req['url']
    print(category, url)
    save(category, url)
    return {'Status':'Ok'}

@app.route('/categories')
def categories():
    category = list_categories()
    #return 'Here will be list of categories'
    return jsonify(category)

@app.route('/category/<name>')
def category(name: str):
    urls = list_urls(name)
    print(urls)

    #return f'Here will be content of category {name}'
    return jsonify(urls)