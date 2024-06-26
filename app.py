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

def connect_to_mysql():
    return mysql.connector.connect(**db_config)


@app.route('/')
def homepage():
    conn = connect_to_mysql()
    cursor = conn.cursor(dictionary=True)
    cursor.execute("SELECT * FROM categories")
    categories = cursor.fetchall()
    cursor.execute("SELECT * FROM shirts WHERE favorite = '1'")
    favorites = cursor.fetchall()
    product_mainImage = []
    for product in favorites:
        cursor.execute(f"SELECT * FROM images WHERE shirt_id={product['id']} AND priority='1'")
        mainImage = cursor.fetchone()
        product_mainImage.append((product, mainImage))
    cursor.close()
    conn.close()
    return render_template('homepage.html', categories=categories, products=product_mainImage)


@app.route('/category/<int:category_id>')
def category_page(category_id):
    conn = connect_to_mysql()
    cursor = conn.cursor(dictionary=True)
    cursor.execute("SELECT * FROM categories")
    categories = cursor.fetchall()
    cursor.execute(f"SELECT * FROM categories WHERE id = {category_id}")
    current_category = cursor.fetchone()
    banner_path = current_category['banner_path']
    cursor.execute(f"SELECT * FROM shirts WHERE category_id = {category_id}")
    shirts = cursor.fetchall()
    product_mainImage = []
    for product in shirts:
        cursor.execute(f"SELECT * FROM images WHERE shirt_id={product['id']} AND priority='1'")
        mainImage = cursor.fetchone()
        product_mainImage.append((product, mainImage))
    cursor.close()
    conn.close()
    return render_template('category_page.html', categories=categories, banner_path=banner_path, products=product_mainImage)


@app.route('/product/<int:shirt_id>')
def product_page(shirt_id):
    conn = connect_to_mysql()
    cursor = conn.cursor(dictionary=True)
    cursor.execute("SELECT * FROM categories")
    categories = cursor.fetchall()
    cursor.execute(f"SELECT * FROM shirts WHERE id = {shirt_id}")
    shirt = cursor.fetchone()
    cursor.execute(f"SELECT * FROM images WHERE shirt_id = {shirt_id}")
    images = cursor.fetchall()
    cursor.close()
    conn.close()
    return render_template("product_page.html", categories=categories, shirt=shirt, images=images)


@app.route('/upload_page')
def upload_page():
    conn = connect_to_mysql()
    cursor = conn.cursor(dictionary=True)
    return render_template("upload_page.html")



if __name__ == '__main__':
    app.run(debug=True)
