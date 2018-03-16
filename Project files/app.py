from flask import Flask, render_template
from data import lectures
app = Flask(__name__)
app.debug = True

Lectures = lectures()


@app.route('/')
def home():
    return render_template('home.html')


@app.route('/lectures')
def lectures():
    return render_template('lecturesPage.html', lectures = Lectures)


@app.route('/lecture/<string:id>/')
def lecture(id):
    return render_template('lecture.html', id = id)


@app.route('/lecture/<string:id>/discussion')
def discussion(id):
    return render_template('discuss.html', id = id)


if __name__ == '__main__':
    app.run()
