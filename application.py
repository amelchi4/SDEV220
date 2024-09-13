from flask import Flask

app = Flask(__name__)
from flask_sqlalchemy import SQLAlchemy

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///data.db'
db = SQLAlchemy(app)

class Book(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    book_name = db.Column(db.String, unique = True, nullable = False)
    author = db.Column(db.String)
    publisher = db.Column(db.String)

def __repr__(self):
    return f"{self.id} - {self.publisher}"

@app.route('/')
def index():
    return 'hello'

@app.route('/books')
def get_books():
    book = Book.query.all()
    output = []
    for book in Book:
        book_data = {'book_name': book.name, 'author': book.author}
    output.append(book_data)
    return {"Books": output}

@app.route('/books/<id>')
def get_book(id):
    book = Book.query.get_or_404(id)
    return {"Title":book.name, "Author": book.author, "Publisher": book.publisher}
