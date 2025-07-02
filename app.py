from flask import Flask, render_template, request, redirect
import mysql.connector

app = Flask(__name__)

# Connect to MySQL
db = mysql.connector.connect(
    host="localhost",
    user="root",
    password="Swetha@28",  # Add your password if any
    database="library"
)
cursor = db.cursor()

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/add', methods=['GET', 'POST'])
def add_book():
    if request.method == 'POST':
        title = request.form['title']
        author = request.form['author']
        cursor.execute("INSERT INTO books (title, author) VALUES (%s, %s)", (title, author))
        db.commit()
        return redirect('/')
    return render_template('add.html')

@app.route('/delete', methods=['GET', 'POST'])
def delete_book():
    if request.method == 'POST':
        book_id = request.form['book_id']
        cursor.execute("DELETE FROM books WHERE id = %s", (book_id,))
        db.commit()
        return redirect('/')
    return render_template('delete.html')

@app.route('/borrow', methods=['GET', 'POST'])
def borrow_book():
    if request.method == 'POST':
        book_id = request.form['book_id']
        cursor.execute("UPDATE books SET status='borrowed' WHERE id = %s", (book_id,))
        db.commit()
        return redirect('/')
    return render_template('borrow.html')

@app.route('/return', methods=['GET', 'POST'])
def return_book():
    if request.method == 'POST':
        book_id = request.form['book_id']
        cursor.execute("UPDATE books SET status='available' WHERE id = %s", (book_id,))
        db.commit()
        return redirect('/')
    return render_template('return.html')

@app.route('/view')
def view_books():
    cursor.execute("SELECT * FROM books")
    books = cursor.fetchall()
    return render_template('view.html', books=books)

if __name__ == '__main__':
    app.run(debug=True)
