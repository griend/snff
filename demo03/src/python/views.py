from flask import Blueprint, render_template, request, redirect, url_for

views = Blueprint(__name__, 'views')

@views.route('/')
def index():
    return redirect(url_for('views.hello'))

@views.route('/home')
def home():
    return render_template('home.html')
 
@views.route('/hello')
def hello():
    args = request.args
    name = args.get('name', default='World')
    return render_template('hello.html', name=name)
