from flask import Flask, render_template, request
from dataclasses import dataclass
from flask_sqlalchemy import SQLAlchemy

# ---------------------------------------------------------
#  FLASK + DATABASE SETUP
# ---------------------------------------------------------

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:postgres@192.168.2.252/animeworldspring2026'
db = SQLAlchemy(app)

# ---------------------------------------------------------
#  DATABASE MODELS
# ---------------------------------------------------------

@dataclass
class Product(db.Model):
    __tablename__ = 'Product'

    id: int
    name: str
    description: str
    image: str
    price: float
    stockAvailable: int

    id = db.Column(db.Integer(), primary_key=True)
    name = db.Column(db.String(200))
    description = db.Column(db.String(2000))
    image = db.Column(db.String(500))
    price = db.Column(db.Float())
    stockAvailable = db.Column(db.Integer())


@dataclass
class Order(db.Model):
    __tablename__ = 'Order'

    id: int
    shippingAddress: str
    city: str
    country: str
    region: str
    productOrdered: int
    totalCost: float

    id = db.Column(db.Integer(), primary_key=True)
    shippingAddress = db.Column(db.String(2000))
    city = db.Column(db.String(200))
    country = db.Column(db.String(200))
    region = db.Column(db.String(200))
    productOrdered = db.Column(db.Integer())
    totalCost = db.Column(db.Float())

# ---------------------------------------------------------
#  HOME PAGE — LOAD PRODUCTS + RENDER ORDER FORM
# ---------------------------------------------------------

@app.route('/')
def default_route():
    allProducts = Product.query.all()

    product_id_list = [p.id for p in allProducts]
    product_name_list = [p.name for p in allProducts]
    product_image_list = [p.image for p in allProducts]
    product_price_list = [p.price for p in allProducts]

    return render_template(
        'index.html',
        productLength=len(product_id_list),
        productsByID=product_id_list,
        productsByName=product_name_list,
        productsByImage=product_image_list,
        productByPrice=product_price_list
    )

# ---------------------------------------------------------
#  DEBUG ROUTES (OPTIONAL)
# ---------------------------------------------------------

@app.route('/product/list')
def list_products():
    return Product.query.all()

@app.route('/order/list')
def list_orders():
    return Order.query.all()

# ---------------------------------------------------------
#  ORDER SUBMISSION ROUTE
# ---------------------------------------------------------

@app.route('/order/insert', methods=['POST'])
def insert_order():
    # SAFE FORM ACCESS
    shipping_address_val = request.form.get('shippingAddress')
    city_val = request.form.get('city')
    country_val = request.form.get('country')
    region_val = request.form.get('region')
    product_ordered_val = request.form.get('productOrdered')

    # Prevent KeyError
    if not product_ordered_val:
        return "Error: No product selected"

    # Convert product ID
    product_id = int(product_ordered_val)

    # Look up product
    product_found = Product.query.filter_by(id=product_id).first()
    if not product_found:
        return "Error: Product not found"

    # SHIPPING COST LOGIC
    region_int = int(region_val)
    if region_int == 1:
        total_price = product_found.price + 5
    elif region_int == 2:
        total_price = product_found.price + 7
    elif region_int == 3:
        total_price = product_found.price + 7
    elif region_int == 4:
        total_price = product_found.price + 10
    else:
        return "Error: Invalid region"

    # SAVE ORDER
    newOrder = Order(
        shippingAddress=shipping_address_val,
        city=city_val,
        country=country_val,
        region=region_val,
        productOrdered=product_id,
        totalCost=total_price
    )

    db.session.add(newOrder)
    db.session.commit()

    message = 'You have ordered ' + product_found.name + ' for a total cost of ' + str(total_price)
    print( message )
    return message

# ---------------------------------------------------------
#  RUN APP
# ---------------------------------------------------------

if __name__ == '__main__':
    app.run(debug=True, port=5055)
