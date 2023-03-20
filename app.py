from flask import Flask , request , render_template
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI']='sqlite:///registration.db'
db=SQLAlchemy(app)
class Registration(db.Model):
    _tableName_='registration'
    id=db.Column(db.Integer , primary_key=True)
    firstName= db.Column(db.String(120))
    lastName= db.Column(db.String(120))
    dob= db.Column(db.Date)
    fatherName = db.Column(db.String(120))
    MotherName = db.Column(db.String(120))
    Rollno = db.Column(db.String(100), unique=True)
    email = db.Column(db.String(40), unique=True)
    phno = db.Column(db.Integer)
    gender = db.Column(db.String(100))
    branch = db.Column(db.String(100))
    year = db.Column(db.Integer)
    clgcode = db.Column(db.String(100))


    def _init_(self,firstName ,lastName , dob , fatherName , MotherName , rollno , email , phno , gender , branch , year ,clgcode):
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
    def _str_(self):
        return f'{self.firstName} - {self.lastName} - {self.Rollno}'
with app.app_context():
    db.create_all()
with app.app_context():
    Registration=Registration.query.all()

@app.route('/')
def home():
    return render_template('index.html')
@app.route('/create',methods=['GET', 'POST'])
def db():
    if request.method == 'POST':
        firstName = request.form['Firstname']
        lastName = request.form['lastname']
        dob= request.form['Dob']
        fatherName = request.form['father']
        MotherName = request.form['mother']
        Rollno = request.form['Rollno']
        email = request.form['email']
        phno = request.form['phno']
        gender = request.form['gender']
        branch = request.form['branch']
        year = request.form['year']
        clgcode = request.form['clgcode']
        register= Registration(firstName,lastName,dob,fatherName,MotherName,Rollno,email,phno,gender,branch,year,clgcode,register)
        db.session.add(register)
        db.session.commit()
        return render_template('thankyou.html')

if __name__ =='_main_':
    app.run(debug=True)