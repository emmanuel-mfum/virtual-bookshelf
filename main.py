from flask import Flask, render_template, request, redirect, url_for
import sqlite3
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)  # create Flask app

# CREATE DATABASE
app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:///new-books-collection.db"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)


class Book(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(250), unique=True, nullable=False)
    author = db.Column(db.String(250), nullable=False)
    rating = db.Column(db.Float, nullable=False)

    def __repr__(self):  # this will allow each book object to be identified by its title when printed.
        return '<Book %r>' % self.title

    def __init__(self, title, author, rating):
        self.title = title
        self.author = author
        self.rating = rating


db.create_all()

# book = Book("Harry Potter", "J. K. Rowling", 9.3)
# db.session.add(book)
# all_books = []


# db = sqlite3.connect("books-collection.db")  # creates connection to our database

# cursor = db.cursor()  # creates a cursor which will control our database.
# cursor.execute("CREATE TABLE books (id INTEGER PRIMARY KEY, title varchar(250) NOT NULL UNIQUE, author varchar(250)"
# " NOT NULL, rating FLOAT NOT NULL)")

# cursor.execute("INSERT  OR IGNORE INTO books VALUES(1, 'Harry Potter', 'J. K. Rowling', '9.3')") # inserts data
# into db

# db.commit()


# CRUD operations with SQLite

# Create
# new_book = Book(id=1, title="Harry Potter", author="J. K. Rowling", rating=9.3), id field is optional
# db.session.add(new_book)
# db.session.commit()

# Read all records
# all_books = db.session.query(Book).all()

# Read a particular record by query
# book = Book.query.filter_by(title="Harry Potter").first()

# Update a particular record by query
# book_to_update = Book.query.filter_by(title="Harry Potter").first()
# book_to_update.title = "Harry Potter and the Chamber of Secrets"
# db.session.commit()

# Update a record by primary key
# book_id = 1
# book_to_update = Book.query.get(book_id)
# book_to_update.title = "Harry Potter and the Goblet of Fire"
# db.session.commit()

# Delete  particular record by primary key
# book_id = 1
# book_to_delete = Book.query.get(book_id)
# db.session.delete(book_to_delete)
# db.session.commit()
# We can also delete by querying for a particular value e.g. by title or one of the other properties.


@app.route('/')
def home():
    all_books = db.session.query(Book).all()  # reads all the books from the database
    return render_template('index.html', books=all_books)


@app.route("/add", methods=['GET', 'POST'])
def add():
    if request.method == 'POST':
        book_entry = {
            "title": request.form['book_title'],
            "author": request.form['author'],
            "rating": request.form['rating']
        }

        # all_books.append(book_entry)
        # print(all_books)
        book = Book(title=request.form['book_title'], author=request.form['author'], rating=request.form['rating'])
        db.session.add(book)
        db.session.commit()
        return redirect(url_for("home"))
    return render_template('add.html')


@app.route('/edit', methods=['GET', 'POST'])
def edit():
    if request.method == 'POST':
        # UPDATE RECORD
        book_id = request.form['id']
        book_to_update = Book.query.get(book_id)
        book_to_update.rating = request.form["rating"]
        db.session.commit()
        return redirect(url_for('home'))

    book_id = request.args.get('id')
    book_to_edit = Book.query.get(book_id)

    return render_template('edit.html', book=book_to_edit)


@app.route("/delete")
def delete():
    book_id = request.args.get('id')
    book_to_delete = Book.query.get(book_id)
    db.session.delete(book_to_delete)
    db.session.commit()
    return redirect(url_for('home'))


if __name__ == "__main__":
    app.run(debug=True)
