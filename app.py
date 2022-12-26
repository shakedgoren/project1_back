import json
from flask import Flask, request
from flask_cors import CORS
from flask_sqlalchemy import SQLAlchemy
 
app = Flask(__name__)
CORS(app)
 
app.config['SQLALCHEMY_DATABASE_URI']='sqlite:///Library.qlite3'
app.config['SECRET_KEY']='random string'

db=SQLAlchemy(app)

class Books(db.Model):
    id = db.Column('Books_id',db.Integer, primary_key=True)
    book_name=db.Column(db.String(50))
    author=db.Column(db.String(50))
    published_year=db.Column(db.Integer)
    book_type=db.Column(db.Integer)

    loan_books = db.relationship('Loans', backref='books_d')
    def __init__(self,book_name,author,published_year,book_type):
        self.book_name=book_name
        self.author=author
        self.published_year=published_year
        self.book_type=book_type

class Customers(db.Model):
    id = db.Column('Customers_id',db.Integer, primary_key=True)
    customers_name=db.Column(db.String(50))
    age=db.Column(db.Integer)
    city=db.Column(db.String(50))

    loan_customers = db.relationship('Loans', backref='customers_d')
    def __init__(self,customers_name,age,city):
        self.customers_name=customers_name
        self.age=age
        self.city=city

class Loans(db.Model):
    id = db.Column('Loans_id',db.Integer, primary_key=True)
    Books_id = db.Column(db.Integer, db.ForeignKey('books.Books_id'))
    Customers_id = db.Column(db.Integer, db.ForeignKey('customers.Customers_id'))
    start=db.Column(db.Integer)
    end=db.Column(db.Integer)
    returned=db.Column(db.Boolean)

    def __init__(self,Customers_id,Books_id,start,end,returned):
        self.Books_id=Books_id
        self.Customers_id=Customers_id
        self.start=start
        self.end=end
        self.returned=returned
  
@app.route("/Books",methods=['GET','POST'])
@app.route("/Books/<id>",methods=['DELETE','PUT'])
def crud_b(id=-1):
    if request.method == 'POST': 
        request_data =request.get_json()
        book_name =request_data['book_name']
        author =request_data['author']
        published_year =request_data['published_year']
        book_type =request_data['book_type']
        newbook =Books(book_name,author,published_year,book_type)
        db.session.add(newbook)
        db.session.commit()
        return []
    if request.method == 'GET':
        response=[]
        for b in Books.query.all():
            response.append({'id':b.id,'book_name':b.book_name,'author':b.author,'published_year':b.published_year,'book_type':b.book_type})
        return(json.dumps(response))
    if request.method == 'PUT':
        put_book=Books.query.get(id)
        request_data=request.get_json()
        put_book.book_name=request_data['book_name']
        put_book.author=request_data['author']
        put_book.published_year=request_data['published_year']
        put_book.book_type=request_data['book_type']
        db.session.commit()
        return{}
    if request.method == 'DELETE':
        db.session.delete(Books.query.get(id))
        db.session.commit()
        return{}

@app.route("/Customers",methods=['GET','POST'])
@app.route("/Customers/<id>",methods=['DELETE','PUT'])
def crud_c(id=-1):
    if request.method == 'POST': 
        request_data=request.get_json()
        customers_name=request_data['customers_name']
        age=request_data['age']
        city=request_data['city']
        newbook=Customers(customers_name,age,city)
        db.session.add(newbook)
        db.session.commit()
        return []
    if request.method == 'GET':
        response=[]
        for c in Customers.query.all():
            response.append({'id':c.id,'customers_name':c.customers_name,'age':c.age,'city':c.city})
        return(json.dumps(response))
    if request.method == 'PUT':
        put_customers=Customers.query.get(id)
        request_data=request.get_json()
        put_customers.customers_name=request_data['customers_name']
        put_customers.age=request_data['age']
        put_customers.city=request_data['city']
        db.session.commit()
        return{}
    if request.method == 'DELETE':
        db.session.delete(Customers.query.get(id))
        db.session.commit()
        return{}

@app.route("/Loans",methods=['GET','POST'])
@app.route("/Loans/<id>",methods=['DELETE','PUT'])
def crud_l(id=-1):
    if request.method == 'POST': 
        request_data=request.get_json()
        Customers_id=request_data['Customers_id']
        Books_id=request_data['Books_id']
        start=request_data['start']
        end=request_data['end']
        returned=False
        print(Customers_id,Books_id,start,end)
        newbook=Loans(Customers_id,Books_id,start,end,returned)
        db.session.add(newbook)
        db.session.commit()
        return []
    if request.method == 'GET':
        response=[]
        for l in Loans.query.all():
            response.append({'loanid':l.id,'customer_name':l.Customers_id,'book_name':l.Books_id,'start':l.start,'end':l.end,'returned':l.returned ,'cusname':l.customers_d.customers_name,'bookname':l.books_d.book_name, 'booktype':l.books_d.book_type})
        return(json.dumps(response))
    if request.method == 'PUT':
        put_loan=Loans.query.get(id)
        request_data=request.get_json()
        put_loan.Customers_id=request_data['Customers_id']
        put_loan.Books_id=request_data['Books_id']
        put_loan.start=request_data['start']
        put_loan.end=request_data['end']
        db.session.commit()
        return{}
    if request.method == 'DELETE':
        db.session.delete(Loans.query.get(id))
        db.session.commit()
        return{}


@app.route("/Loans/returend/<id>",methods=['PUT'])
def crud_lr(id=-1):
    if request.method == 'PUT':
            put_loan=Loans.query.get(id)
            request_data=request.get_json()
            put_loan.returned=request_data['returned']
            db.session.commit()
            return{}

if __name__ == '__main__':
    with app.app_context():db.create_all()
    app.run(debug=True)


