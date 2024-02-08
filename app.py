from flask import Flask, render_template, url_for

app = Flask(__name__)

'''
# Routing for your application.
# Put your routes below this comment
'''
@app.route('/')
def home():
    return 'My home page'

@app.route('/about')
def about():
    #image_url = url_for('static', filename='myPic.jpg')
    return render_template('about.html')

@app.errorhandler(404)
def page_not_found(error):
    """Custom 404 page."""
    return render_template('404.html'), 404
