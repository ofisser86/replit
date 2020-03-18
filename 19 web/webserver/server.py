from flask import Flask, render_template

app = Flask(__name__)
print(__name__)

@app.route('/<username>/<int:post_id>')
def hello_world(username, post_id):
    return render_template('index.html', username='dmytro', post_id=3132416545)

@app.route('/blog')
def blog():
    return 'My blogpost!'

@app.route('/about')
def about():
    return render_template('about.html')


if __name__ == '__main__':
    # in olser version use debug=true for debug mode on
    app.run()