from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
def hello_world():
    return render_template('index.html')


@app.route('/account')
def account():
    menu_point = {'type': 'account'}
    return render_template('account.html', context=menu_point)


@app.route('/account-info')
def account_info():
    menu_point = {'type': 'account'}
    return render_template('account.html', context=menu_point)


@app.route('/payments')
def payments():
    menu_point = {'type': 'payments'}
    return render_template('account.html', context=menu_point)


@app.route('/upload-file')
def upload_file():
    menu_point = {'type': 'upload'}
    return render_template('account.html', context=menu_point)


@app.route('/analytics')
def analytics():
    menu_point = {'type': 'analytics'}
    return render_template('account.html', context=menu_point)


@app.route('/faq')
def faq():
    menu_point = {'type': 'faq.html'}
    return render_template('account.html', context=menu_point)


if __name__ == '__main__':
    app.run(debug=True)
