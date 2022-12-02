from flask import Blueprint, render_template

blueprint = Blueprint('auth', __name__, url_prefix='/auth')


@blueprint.route('/login')
def login():
    return render_template('about.html')


@blueprint.route('/')
def index():
    return render_template('about.html')
