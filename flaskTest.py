from flask import Flask, redirect, url_for, request, render_template
import sqlite3

app = Flask(__name__)

@app.route('/')
def main():
    return render_template("login.html")


@app.route('/login', methods=['POST', 'GET'])
def login():
    # Connect to the database (creates it if it doesn't exist)
    conn = sqlite3.connect('test.db')
    # Create a cursor object
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM users')
    data = cursor.fetchall()
    conn.close()
    names = []
    passwords = []
    for row in data:
        names.append(row[1])
        passwords.append(row[2])
    if request.method == 'POST':
        user = request.form['name']
        password = request.form['pw']
        print(names)
        if user in names:
            if passwords[names.index(user)] == password:
                return render_template("welcome.html", name=user)
    return redirect(url_for('main'))


if __name__ == '__main__':
    app.run(debug=True)