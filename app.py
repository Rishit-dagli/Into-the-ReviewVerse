from flask import Flask, render_template, request
from scrapper import scrap
 
app = Flask(__name__, template_folder='templates', static_folder='static')
 
 
@app.route('/search', methods=['POST'])
def search():
    url = request.form['searchInput']
    # Process the URL as needed
    # You can perform further actions or return a response
    try:
        title, store, review_nums, reviews = scrap(url)
        return render_template('task.html', product=title, store = store, pros=reviews[0], cons=reviews[2], review_nums=str(review_nums))
    except: 
        title = 'try again'
        store = 'try agian'
        review_nums = 'try again'
        reviews = ['try again', 'try again', 'try again', 'try again']
        return render_template('task.html', product=title, store = store, pros=reviews[0], cons=reviews[2], review_nums=str(review_nums))

@app.route('/')
def index():
    return render_template('index.html')
 
@app.route('/about/')
def about():
    return render_template('about.html')

@app.route('/task/')
def task():
    return render_template('task.html')

if __name__=='__main__':
    app.run(debug = True)