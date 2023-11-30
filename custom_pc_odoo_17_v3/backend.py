```python
from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow
from flask_bcrypt import Bcrypt
from flask_cors import CORS
import os

# Init app
app = Flask(__name__)
basedir = os.path.abspath(os.path.dirname(__file__))
# Database
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(basedir, 'db.sqlite')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
# Init db
db = SQLAlchemy(app)
# Init ma
ma = Marshmallow(app)
# Init bcrypt
bcrypt = Bcrypt(app)
# Enable CORS
CORS(app)

# Product Category Model
class ProductCategory(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), unique=True)

    def __init__(self, name):
        self.name = name

# Product Category Schema
class ProductCategorySchema(ma.Schema):
    class Meta:
        fields = ('id', 'name')

# Init schema
product_category_schema = ProductCategorySchema()
product_categories_schema = ProductCategorySchema(many=True)

# Create a Product Category
@app.route('/product-category', methods=['POST'])
def add_product_category():
    name = request.json['name']
    new_product_category = ProductCategory(name)
    db.session.add(new_product_category)
    db.session.commit()
    return product_category_schema.jsonify(new_product_category)

# Get All Product Categories
@app.route('/product-category', methods=['GET'])
def get_product_categories():
    all_product_categories = ProductCategory.query.all()
    result = product_categories_schema.dump(all_product_categories)
    return jsonify(result)

# Run Server
if __name__ == '__main__':
    app.run(debug=True)
```