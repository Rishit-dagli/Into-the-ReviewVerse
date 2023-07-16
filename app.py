from flask import Flask, render_template, request
from scrapper import scrap
from model.inference import inference
 
app = Flask(__name__, template_folder='templates', static_folder='static')
 
 
@app.route('/search', methods=['POST'])
def search():
    url = request.form['searchInput']
    # Process the URL as needed
    # You can perform further actions or return a response
    try:
        title, store, review_nums, reviews = scrap(url)
        infer = []
        for val in ['pros', 'cons']:
            out = inference(reviews, val)
            infer.append(out)
        pros = infer[0]
        n = len(pros)
        if n >= 1:
            pro1 = pros[0]
        else:
            pro1 = ''
        if n >= 2:
            pro2 = pros[1]
        else:
            pro2 = ''
        if n >= 3:
            pro3 = pros[2]
        else:
            pro3 = ''
        if n >= 4:
            pro4 = pros[3]
        else:
            pro4 = ''
        if n >= 5:
            pro5 = pros[4]
        else:
            pro5 = ''
        if n >= 6:
            pro6 = pros[5]
        else:
            pro6 = ''

        cons = infer[1]
        n = len(cons)
        if n >= 1:
            con1 = cons[0]
        else:
            con1 = ''
        if n >= 2:
            con2 = cons[1]
        else:
            con2 = ''
        if n >= 3:
            con3 = cons[2]
        else:
            con3 = ''
        if n >= 4:
            con4 = cons[3]
        else:
            con4 = ''
        if n >= 5:
            con5 = cons[4]
        else:
            con5 = ''
        if n >= 6:
            con6 = cons[5]
        else:
            con6 = ''


            infer.append(inference(reviews, val))
        return render_template('task.html', product=title+' - ', store = store, review_nums=str(review_nums), pro1=pro1, pro2=pro2, pro3=pro3, pro4=pro4, pro5=pro5, pro6=pro6, con1=con1, con2=con2, con3=con3, con4=con4, con5=con5, con6=con6)
    except: 
        title = 'try again'
        store = 'try agian'
        review_nums = 'try again'
        reviews = ['try again', 'try again', 'try again', 'try again']
        return render_template('task.html', product=title, store = store, review_nums=str(review_nums), pro1='try again', pro2='try again', pro3='try again', pro4='try again', pro5='try again', pro6='try again', con1='try again', con2='try again', con3='try again', con4='try again', con5='try again', con6='try again')

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