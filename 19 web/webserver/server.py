from flask import Flask, render_template, request

app = Flask(__name__)
print(__name__)

@app.route('/')
def my_index():
    return render_template('index.html')

@app.route('/blog')
def blog():
    return 'My blogpost!'

@app.route('/<slug>')
def works(slug):
    return render_template(f'{slug}')


@app.route('/submit_form', methods=['POST', 'GET'])
def submit_form():
    if request.method == "POST":
        data = request.form.to_dict()
        print(data)
        return "Data submted"
    else:
        return "Some error occur"
    

# @app.route('/works')
# def works():
#     return render_template('works.html')

# @app.route('/work')
# def work():
#     return render_template('work.html')

# @app.route('/about')
# def about():
#     return render_template('about.html')

# @app.route('/contact')
# def contact():
#     return render_template('contact.html')

# @app.route('/components')
# def components():
#     return render_template('components.html')


if __name__ == '__main__':
    # in olser version use debug=true for debug mode on
    app.run()