from flask import Flask, render_template
import os
from bson.objectid import ObjectId
from pymongo import MongoClient
from flask import Flask, render_template, request, redirect, url_for
from datetime import datetime

host = os.environ.get('MONGODB_URI', 'mongodb://localhost:27017/Therapy')
client = MongoClient(host=f'{host}?retryWrites=false')
db = client.get_default_database()
therapists = db.therapists

app = Flask(__name__)

@app.route('/')
def home():
    """Home Page."""
    return render_template('home.html')

@app.route('/therapists')
def index():
    """Show all therapists."""
    return render_template('therapist_index.html', therapists=therapists.find())

@app.route('/therapists/add')
def therapists_add():
    """Add a new therapist."""
    return render_template('therapists_add.html', therapist={}, title='New Therapist')

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
    therapist_id = therapists.insert_one(therapist).inserted_id
    return redirect(url_for('therapist_show',therapist_id = therapist_id))
         
@app.route('/therapists/<therapist_id>')
def therapist_show(therapist_id):
    """Show a single therapist."""
    therapist = therapists.find_one({'_id': ObjectId(therapist_id)})
    return render_template('therapist_show.html', therapist=therapist)

@app.route('/therapists/<therapist_id>/edit')
def therapists_edit(therapist_id):
    """Show the edit form for a therapist."""
    therapist = therapists.find_one({'_id': ObjectId(therapist_id)})
    return render_template('therapists_edit.html', therapist=therapist, title='Edit Therapist')

@app.route('/therapists/<therapist_id>', methods=['POST'])
def therapists_update(therapist_id):
    """Submit an edited therapist."""
    updated_therapist = {
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
        'language': request.form.get('language'),
        'profession': request.form.get('profession'),
        'approach': request.form.get('approach'),
        'issues': request.form.get('issues'),
    }
    therapists.update_one(
        {'_id': ObjectId(therapist_id)},
        {'$set': updated_therapist})
    return redirect(url_for('index', therapist_id=therapist_id))

@app.route('/therapists/<therapist_id>/delete', methods=['POST'])
def therapists_delete(therapist_id):
    """Delete one therapist."""
    therapists.delete_one({'_id': ObjectId(therapist_id)})
    return render_template('therapist_index.html', therapists=therapists.find())




if __name__ == '__main__':
    app.run(debug=True)