from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import Mapped, mapped_column, DeclarativeBase
from sqlalchemy import String, Integer, Float

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///Final_database.db'
class Base(DeclarativeBase):
    pass

db = SQLAlchemy(model_class=Base)


class Book(db.Model):
    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    title: Mapped[str] = mapped_column(String, nullable=False, unique=True)
    author: Mapped[str] = mapped_column(String, nullable=False)
    rating: Mapped[float] = mapped_column(Float, nullable=False)

db.init_app(app)

with app.app_context():
    db.create_all()

@app.route('/')
def home():
    with app.app_context():
        result = db.session.execute(db.select(Book).order_by(Book.title))
        all_books = result.scalars()            # It return list
        return render_template('index.html', all_books=all_books)


@app.route("/add", methods=['GET', 'POST'])
def add():
    if request.method == 'POST':
        data = request.form.to_dict()
        # print(data)
        with app.app_context():
            new_book = Book(title=data['title'], author=data['author'], rating=data['rating'])
            db.session.add(new_book)
            db.session.commit()
        return redirect(url_for('home'))
    else:
        return render_template('add.html')


@app.route('/edit', methods=['GET', 'POST'])
def edit():
    if request.method == 'POST':
        # Update Record
        book_id = request.form["id"]
        # print(book_id)
        book_to_update = db.get_or_404(Book, book_id)
        book_to_update.rating = request.form["rating"]
        db.session.commit()
        return redirect(url_for('home'))
    book_id = request.args.get('id')
    book_selected = db.get_or_404(Book, book_id)
    return render_template("edit.html", book=book_selected)

@app.route("/<int:id>")
def delete(id):
    with app.app_context():
        result =  db.session.execute(db.select(Book).where(Book.id == id)).scalar()
        db.session.delete(result)
        db.session.commit()
        return redirect(url_for('home'))

if __name__ == "__main__":
    app.run(debug=True, port=6300)