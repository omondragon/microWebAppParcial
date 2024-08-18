from flask import Flask, render_template
from flask_cors import CORS

app = Flask(__name__)
app.secret_key = 'secret123'
CORS(app, supports_credentials=True)
app.config.from_object('config.Config')


# Ruta para renderizar el template index.html
@app.route('/')
def index():
    return render_template('index.html')

@app.route('/dashboard')
def dashboard():
    return render_template('dashboard.html')

# Ruta para renderizar el template users.html
@app.route('/users')
def users():
    return render_template('users.html')

# Ruta para renderizar el template products.html
@app.route('/products')
def products():
    return render_template('products.html')

# Ruta para renderizar el template orders.html
@app.route('/orders')
def orders():
    return render_template('orders.html')

@app.route('/editUser/<string:id>')
def edit_user(id):
    print("id recibido",id)
    return render_template('editUser.html', id=id)

@app.route('/editProduct/<string:id>')
def edit_product(id):
    print("id recibido",id)
    return render_template('editProduct.html', id=id)

@app.route('/editOrder/<string:id>')
def edit_order(id):
    print("id recibido",id)
    return render_template('editOrder.html', id=id)

if __name__ == '__main__':
    app.run()
