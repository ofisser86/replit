from flask import Flask, render_template

app = Flask(__name__)
print(__name__)

@app.route('/')
def hello_world():
    return render_template('index.html')

@app.route('/blog')
def blog():
    return 'My blogpost!'

@app.route('/about')
def about():
    return render_template('about.html')


if __name__ == '__main__':
    # in olser version use debug=true for debug mode on
    app.run()