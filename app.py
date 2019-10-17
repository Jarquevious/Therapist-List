from flask import Flask, render_template
import os
from bson.objectid import ObjectId
from pymongo import MongoClient
from flask import Flask, render_template, request, redirect, url_for
from datetime import datetime

host = os.environ.get('MONGODB_URI', 'mongodb://localhost:27017/Therapy')
client = MongoClient(host=host)
db = client.Therapy
therapists = db.therapists

app = Flask(__name__)



@app.route('/')
def home():
    """Home Page."""
    return render_template('home.html')

@app.route('/therapists')
def index():
    """Show all therapists."""
    return render_template('index.html', therapists=therapists.find())

@app.route('/therapists/add')
def therapists_add():
    """Add a new therapist."""
    return render_template('therapists_add.html')


@app.route('/therapists', methods=['POST'])
def therapist_submit():
    """Submit a new therapist."""
    therapist = {
        'name': request.form.get('name'),
        'phone': request.form.get('phone'),
        'email': request.form.get('email'),
        'street': request.form.get('street'),
        'city': request.form.get('city'),
        'state': request.form.get('state'),
        'zip': request.form.get('zip'),
        'status': request.form.get('status'),
        'billing': request.form.get('billing'),
        'services': request.form.get('services'),
        'ages': request.form.get('ages'),
        'languages': request.form.get('languages'),
        'profession': request.form.get('profession'),
        'phone': request.form.get('phone'),
        'approach': request.form.get('approach'),
        'issues': request.form.get('issues')
        
        
        
         }
    therapists.insert_one(therapist)
    return redirect(url_for('index'))







if __name__ == '__main__':
    app.run(debug=True)