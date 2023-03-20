from flask import Flask , request , render_template
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')
@app.route('/update')
def db():
    return 'asdfadsfa'

if __name__ =='__main__':
    app.run(debug=True)