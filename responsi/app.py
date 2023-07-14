from flask import Flask, render_template
import mysql.connector

app = Flask(__name__)

# Fungsi untuk menghubungkan ke database
def get_db_connection():
    conn = mysql.connector.connect(
        host='localhost',
        user='root',  # Ganti dengan username MySQL Anda
        password='your_password',  # Ganti dengan password MySQL Anda
        database='users'  # Ganti dengan nama database Anda
    )
    return conn

# Route untuk menampilkan isi tabel 'users'
@app.route('/')
def show_users():
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM users')
    users = cursor.fetchall()
    cursor.close()
    conn.close()
    return render_template('user.html', users=users)

if __name__ == '__main__':
    app.run()
