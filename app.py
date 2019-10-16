from flask import Flask, render_template
# import os
# from bson.objectid import ObjectId
# from pymongo import MongoClient
# from flask import Flask, render_template, request, redirect, url_for
# from datetime import datetime

# host = os.environ.get('MONGODB_URI', 'mongodb://localhost:27017/Therapy')
# client = MongoClient(host=host)
# db = client.Therapy
#therapists = db.therapists

app = Flask(__name__)
@app.route('/')
def index():
    """Return homepage."""
    return render_template('home.html', msg='Flask is Cool!!')

# therapists = [

#     {
#         'First name': ''
#         'Last name': ''
#         'Address': ''
#         'Zip code': ''
#         'State': ''
#         'Description': ''
#         'Specialty': ''
#     }
# ]




# @app.route('/home')
# def home():
#     therapists = db.therapists.find()
#     return render_template('home.html', therapsits=therapists)

# @app.route('/add')
# def add():
#     return render_template(therapist_list.html)


# @app.route('/therapist_list')
# def therapist_list():
#     #return render_template('/therpist_list.html')







if __name__ == '__main__':
    app.run(debug=True)