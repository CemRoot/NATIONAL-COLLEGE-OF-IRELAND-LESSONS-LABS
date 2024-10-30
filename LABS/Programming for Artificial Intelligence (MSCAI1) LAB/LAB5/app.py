from flask import Flask, render_template, redirect, url_for, request, flash
from flask_login import LoginManager, login_user, logout_user, login_required, UserMixin, current_user
from flask_mysqldb import MySQL
from werkzeug.security import generate_password_hash, check_password_hash

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

        # Şifreyi hashleme
        hashed_password = generate_password_hash(password)

        cur = mysql.connection.cursor()
        try:
            # Kullanıcıyı veritabanına kaydetme
            cur.execute("INSERT INTO Users (username, password_hash, email) VALUES (%s, %s, %s)",
                        (username, hashed_password, email))
            mysql.connection.commit()
            flash('Registration successful! Please log in.', 'success')
            return redirect(url_for('login'))
        except:
            mysql.connection.rollback()
            flash('Username or email already exists.', 'danger')
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
        user = cur.fetchone()  # Kullanıcıyı çekiyoruz
        cur.close()

        if user:
            # Hashlenmiş şifreyi doğruluyoruz
            if check_password_hash(user[2], password):  # user[2] şifrenin hashli hali
                user_obj = User(user_id=user[0], username=user[1], email=user[3], password_hash=user[2])
                login_user(user_obj)
                flash('Logged in successfully!', 'success')
                return redirect(url_for('home'))
            else:
                flash('Invalid username or password.', 'danger')
        else:
            flash('Invalid username or password.', 'danger')
    return render_template('login.html')


# Logout Route
@app.route('/logout')
@login_required
def logout():
    logout_user()
    flash('You have been logged out.', 'info')
    return redirect(url_for('login'))


# Home Page - Display Products
@app.route('/')
def home():
    cur = mysql.connection.cursor()
    cur.execute("SELECT product_id, Description, UnitPrice FROM Products")
    products = cur.fetchall()
    cur.close()
    return render_template('home.html', products=products)


# Add to Cart
@app.route('/add_to_cart/<int:product_id>', methods=['POST'])
@login_required
def add_to_cart(product_id):
    quantity = int(request.form.get('quantity', 1))
    user_id = current_user.id

    cur = mysql.connection.cursor()
    cur.execute("SELECT * FROM OrderItems WHERE user_id = %s AND product_id = %s", (user_id, product_id))
    item = cur.fetchone()

    if item:
        cur.execute("UPDATE OrderItems SET quantity = quantity + %s WHERE user_id = %s AND product_id = %s",
                    (quantity, user_id, product_id))
    else:
        cur.execute("INSERT INTO OrderItems (user_id, product_id, quantity) VALUES (%s, %s, %s)",
                    (user_id, product_id, quantity))

    mysql.connection.commit()
    cur.close()

    flash('Product added to cart.', 'success')
    return redirect(url_for('cart'))


# Cart Page
@app.route('/cart')
@login_required
def cart():
    user_id = current_user.id
    cur = mysql.connection.cursor()

    cur.execute("""
        SELECT p.Description, p.UnitPrice, oi.quantity 
        FROM OrderItems oi 
        JOIN Products p ON oi.product_id = p.product_id
        WHERE oi.user_id = %s
    """, (user_id,))

    products = cur.fetchall()
    total = sum(item[1] * item[2] for item in products)

    cur.close()

    return render_template('cart.html', products=products, total=total)


# Checkout
@app.route('/checkout', methods=['GET', 'POST'])
@login_required
def checkout():
    user_id = current_user.id
    cur = mysql.connection.cursor()

    cur.execute("""
        SELECT p.Description, p.UnitPrice, oi.quantity 
        FROM OrderItems oi 
        JOIN Products p ON oi.product_id = p.product_id
        WHERE oi.user_id = %s
    """, (user_id,))

    cart_items = cur.fetchall()

    if not cart_items:
        flash('Your cart is empty.', 'warning')
        return redirect(url_for('home'))

    total = sum(item[1] * item[2] for item in cart_items)

    if request.method == 'POST':
        cur.execute("INSERT INTO Orders (user_id, total_amount, order_date) VALUES (%s, %s, NOW())",
                    (user_id, total))
        order_id = cur.lastrowid

        for item in cart_items:
            cur.execute("INSERT INTO OrderItems (order_id, product_id, quantity) VALUES (%s, %s, %s)",
                        (order_id, item[0], item[2]))
            cur.execute("DELETE FROM OrderItems WHERE user_id = %s AND product_id = %s", (user_id, item[0]))

        mysql.connection.commit()
        cur.close()

        flash('Order placed successfully!', 'success')
        return redirect(url_for('home'))

    cur.close()
    return render_template('checkout.html', products=cart_items, total=total)


# Run the application
if __name__ == '__main__':
    app.run(debug=True)
