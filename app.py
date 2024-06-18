from flask import Flask, jsonify, render_template
import mysql.connector

app = Flask(__name__, static_url_path='/static', static_folder='static')

# Configuure MySQL connection
db_config = {
    'user': 'root',
    'password': '',
    'host': 'localhost',
    'database': 'bgc_catalog', 
    'raise_on_warnings': True
}

# Define a route to fetch all shirts
@app.route('/api/shirts')
def get_shirts():
    conn = mysql.connector.connect(**db_config)
    cursor = conn.cursor(dictionary=True)
    cursor.execute = 'select * from shirts'
    shirts = cursor.fetchall()
    cursor.close()
    conn.close()
    return jsonify(shirts)

@app.route('/')
def homepage():
    return render_template('homepage.html')

@app.route('/product')
def product_page():
    return render_template('product.html')

@app.route('/brasileirao')
def brasileirao_page():
    return render_template('brasileirao.html')

if __name__ == '__main__':
    app.run(debug=True)