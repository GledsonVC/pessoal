from flask import Flask, render_template, request, redirect, url_for, jsonify
from src.crud_logic import get_persons, add_person, update_person, delete_person, search_person, create_empty_json
import os

def create_app():
    app = Flask(__name__)

    @app.route('/')
    def index():
        persons = get_persons()
        return render_template('index.html', persons=persons)

    @app.route('/add', methods=['POST'])
    def add():
        name = request.form['name']
        phone = request.form['phone']
        email = request.form['email']
        add_person(name, phone, email)
        return redirect(url_for('index'))

    @app.route('/update', methods=['POST'])
    def update():
        person_id = int(request.form['id'])
        name = request.form['name']
        phone = request.form['phone']
        email = request.form['email']
        update_person(person_id, name, phone, email)
        return redirect(url_for('index'))

    @app.route('/delete/<int:person_id>', methods=['POST'])
    def delete(person_id):
        delete_person(person_id)
        return redirect(url_for('index'))

    @app.route('/search', methods=['GET'])
    def search():
        query = request.args.get('query')
        persons = search_person(query)
        return render_template('index.html', persons=persons)

    return app
