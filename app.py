from flask import Flask, render_template, request, redirect, url_for, flash
import sqlite3

app = Flask(__name__)
app.secret_key = "secret_key"

# Connect to SQLite Database
def connect_db():
    conn = sqlite3.connect('database.db')
    return conn

# Create Database Table
def create_table():
    conn = connect_db()
    conn.execute('''CREATE TABLE IF NOT EXISTS students 
                    (id INTEGER PRIMARY KEY AUTOINCREMENT,
                    name TEXT,
                    subject TEXT,
                    grade TEXT)''')
    conn.close()

# Home Page
@app.route('/')
def index():
    conn = connect_db()
    cursor = conn.execute("SELECT * FROM students")
    students = cursor.fetchall()
    conn.close()
    return render_template('index.html', students=students)

# Add Student and Grade
@app.route('/add', methods=['GET', 'POST'])
def add_student():
    if request.method == 'POST':
        name = request.form['name']
        subject = request.form['subject']
        grade = request.form['grade']
        
        conn = connect_db()
        conn.execute("INSERT INTO students (name, subject, grade) VALUES (?, ?, ?)",
                     (name, subject, grade))
        conn.commit()
        conn.close()

        flash("Student and grade added successfully!")
        return redirect(url_for('index'))
    
    return render_template('add_student.html')

# View Student Details
@app.route('/student/<int:id>')
def view_student(id):
    conn = connect_db()
    cursor = conn.execute("SELECT * FROM students WHERE id=?", (id,))
    student = cursor.fetchone()
    conn.close()
    return render_template('view_student.html', student=student)

if __name__ == '__main__':
    create_table()
    app.run(debug=True)
