from flask import Flask, render_template, redirect, url_for, request, session, flash
from flask_login import LoginManager, login_user, logout_user, login_required, UserMixin, current_user
from flask_mysqldb import MySQL
from werkzeug.security import generate_password_hash, check_password_hash
from datetime import datetime

app = Flask(__name__)
app.secret_key = 'your_secret_key'  # Replace with your secret key

# MySQL in config.py
from config import Config
app.config.from_object(Config)

mysql = MySQL(app)

# Flask-Login Configuration
login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = 'login'

# User Model
class User(UserMixin):
    def __init__(self, user_id, username, email, password_hash):
        self.id = user_id
        self.username = username
        self.email = email
        self.password_hash = password_hash

@login_manager.user_loader
def load_user(user_id):
    cur = mysql.connection.cursor()
    cur.execute("SELECT * FROM Users WHERE user_id = %s", (user_id,))
    user = cur.fetchone()
    cur.close()
    if user:
        return User(user_id=user[0], username=user[1], email=user[3], password_hash=user[2])
    return None

# Registration Route
@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        email = request.form['email']
        hashed_password = generate_password_hash(password)

        cur = mysql.connection.cursor()
        try:
            cur.execute("INSERT INTO Users (username, password_hash, email) VALUES (%s, %s, %s)",
                        (username, hashed_password, email))
            mysql.connection.commit()
            flash('Registration successful! Please log in.', 'success')
            return redirect(url_for('login'))
        except:
            mysql.connection.rollback()
            flash('Username or email already exists.', 'danger')
            return render_template('register.html')
        finally:
            cur.close()
    return render_template('register.html')

# Login Route
@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username_or_email = request.form['username']
        password = request.form['password']

        cur = mysql.connection.cursor()
        cur.execute("SELECT * FROM Users WHERE username = %s OR email = %s", (username_or_email, username_or_email))
        user = cur.fetchone()
        cur.close()

        if user and check_password_hash(user[2], password):
            user_obj = User(user_id=user[0], username=user[1], email=user[3], password_hash=user[2])
            login_user(user_obj)
            flash('Logged in successfully!', 'success')
            return redirect(url_for('home'))
        else:
            flash('Invalid username or password.', 'danger')
            return render_template('login.html')
    return render_template('login.html')

# Logout Route
@app.route('/logout')
@login_required
def logout():
    logout_user()
    flash('You have been logged out.', 'info')
    return redirect(url_for('login'))

# Home Page - Display Products (StockCode, Description, UnitPrice)
@app.route('/')
def home():
    cur = mysql.connection.cursor()
    cur.execute("SELECT StockCode, Description, UnitPrice FROM online_retail")  # Adjust query to the new dataset
    products = cur.fetchall()
    cur.close()
    return render_template('home.html', products=products)

# Product Details Route
@app.route('/product/<int:stock_code>')
def product_detail(stock_code):
    cur = mysql.connection.cursor()
    cur.execute("SELECT * FROM online_retail WHERE StockCode = %s", (stock_code,))
    product = cur.fetchone()
    cur.close()
    if product:
        return render_template('product_detail.html', product=product)
    else:
        flash('Product not found.', 'warning')
        return redirect(url_for('home'))

# Add to Cart Functionality
@app.route('/add_to_cart/<int:stock_code>', methods=['POST'])
def add_to_cart(stock_code):
    quantity = int(request.form.get('quantity', 1))
    if 'cart' not in session:
        session['cart'] = {}
    cart = session['cart']
    if str(stock_code) in cart:
        cart[str(stock_code)] += quantity
    else:
        cart[str(stock_code)] = quantity
    session['cart'] = cart
    flash('Product added to cart.', 'success')
    return redirect(url_for('cart'))

# Shopping Cart Page
@app.route('/cart')
def cart():
    cart = session.get('cart', {})
    products = []
    total = 0
    if cart:
        cur = mysql.connection.cursor()
        for stock_code, quantity in cart.items():
            cur.execute("SELECT StockCode, Description, UnitPrice FROM online_retail WHERE StockCode = %s", (stock_code,))
            product = cur.fetchone()
            if product:
                product_data = {
                    'stock_code': product[0],
                    'description': product[1],
                    'price': product[2],
                    'quantity': quantity,
                    'total_price': product[2] * quantity
                }
                total += product_data['total_price']
                products.append(product_data)
        cur.close()
    return render_template('cart.html', products=products, total=total)

# Update Cart Quantities and Remove Products
@app.route('/update_cart', methods=['POST'])
def update_cart():
    cart = session.get('cart', {})
    for stock_code in list(cart.keys()):
        quantity = int(request.form.get(f'quantity_{stock_code}', 1))
        if quantity <= 0:
            cart.pop(stock_code)
        else:
            cart[stock_code] = quantity
    session['cart'] = cart
    flash('Cart updated.', 'success')
    return redirect(url_for('cart'))

# Checkout Page
@app.route('/checkout', methods=['GET', 'POST'])
@login_required
def checkout():
    cart = session.get('cart', {})
    if not cart:
        flash('Your cart is empty.', 'warning')
        return redirect(url_for('home'))
    products = []
    total = 0
    cur = mysql.connection.cursor()
    for stock_code, quantity in cart.items():
        cur.execute("SELECT StockCode, Description, UnitPrice, Quantity FROM online_retail WHERE StockCode = %s", (stock_code,))
        product = cur.fetchone()
        if product:
            if product[3] < quantity:  # Check stock availability (Quantity column)
                flash(f"Not enough stock for {product[1]}. Available: {product[3]}", 'danger')
                return redirect(url_for('cart'))
            product_data = {
                'stock_code': product[0],
                'description': product[1],
                'price': product[2],
                'quantity': quantity,
                'total_price': product[2] * quantity
            }
            total += product_data['total_price']
            products.append(product_data)
    if request.method == 'POST':
        # Insert into Orders (Use InvoiceNo if needed)
        order_date = datetime.now().date()
        cur.execute("INSERT INTO Orders (user_id, total_amount, order_date) VALUES (%s, %s, %s)",
                    (current_user.id, total, order_date))
        order_id = cur.lastrowid
        # Insert into OrderItems and update stock (Quantity column)
        for item in products:
            cur.execute("INSERT INTO OrderItems (order_id, stock_code, quantity) VALUES (%s, %s, %s)",
                        (order_id, item['stock_code'], item['quantity']))
            # Update product stock
            cur.execute("UPDATE online_retail SET Quantity = Quantity - %s WHERE StockCode = %s",
                        (item['quantity'], item['stock_code']))
        mysql.connection.commit()
        cur.close()
        session.pop('cart')
        flash('Order placed successfully!', 'success')
        return redirect(url_for('home'))
    cur.close()
    return render_template('checkout.html', products=products, total=total)

# Run the application
if __name__ == '__main__':
    app.run(debug=True)
