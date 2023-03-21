from flask import Flask , request , render_template
from flask_sqlalchemy import SQLAlchemy
import datetime as dt

f = open('userid.txt', 'w')
f.close()

def writeFile(string):
    f = open('userid.txt', 'w')
    f.write(string)
    f.close()

def readFile():
    f = open('userid.txt', 'r')
    v=f.readline()
    return v
def increment():
    f=open('userid.txt','r')
    v=f.readline()
    v=int(v)
    v=v+1
    f.close()
    f=open('userid.txt','w')
    writeFile(v)

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI']='sqlite:///registration.db'
db=SQLAlchemy(app)
class Registration(db.Model):
    __tableName__='registration'
    id=db.Column(db.Integer , primary_key=True)
    firstName= db.Column(db.String(120))
    lastName= db.Column(db.String(120))
    dob= db.Column(db.DateTime)
    fatherName = db.Column(db.String(120))
    MotherName = db.Column(db.String(120))
    Rollno = db.Column(db.String(100), unique=True)
    email = db.Column(db.String(40), unique=True)
    phno = db.Column(db.Integer)
    gender = db.Column(db.String(100))
    branch = db.Column(db.String(100))
    year = db.Column(db.Integer)
    clgcode = db.Column(db.String(100))


    def __init__(self,firstName ,lastName , dob , fatherName , MotherName , rollno , email , phno , gender , branch , year ,clgcode):
        self.firstName=firstName
        self.lastName = lastName
        self.branch = branch
        self.clgcode = clgcode
        self.dob = dob
        self.fatherName = fatherName
        self.MotherName=MotherName
        self.Rollno = rollno
        self.email = email
        self.phno = phno
        self.gender = gender
        self.year = year
    def __str__(self):
        return f'{self.firstName} - {self.lastName} - {self.Rollno}'
with app.app_context():
    db.create_all()
with app.app_context():
    Registrate=Registration.query.all()

@app.route('/')
def home():
    return render_template('index.html')
@app.route('/create',methods=['GET', 'POST'])
def Creation():
    if request.method == 'POST':
        firstName = request.form.get('Firstname')
        lastName = request.form.get('lastname')
        dob = dt.datetime.strptime(request.form['Dob'],'%Y-%m-%d')
        fatherName = request.form.get('father')
        MotherName = request.form.get('mother')
        Rollno = request.form.get('Rollno')
        email = request.form.get('email')
        phno = request.form.get('phno')
        gender = request.form.get('gender')
        branch = request.form.get('branch')
        year = request.form.get('year')
        clgcode = request.form.get('clgcode')
        register = Registration(firstName,lastName,dob,fatherName,MotherName,Rollno,email,phno,gender,branch,year,clgcode)
        db.session.add(register)
        db.session.commit()
        return render_template('thankyou.html')

if __name__ =='_main_':
    app.run(debug=True)