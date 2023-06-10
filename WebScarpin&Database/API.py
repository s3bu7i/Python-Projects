from flask import Flask, jsonify, request

app = Flask(__name__)

# Sample data
products = [
    {'id': 1, 'name': 'Product 1', 'price': 10.99},
    {'id': 2, 'name': 'Product 2', 'price': 19.99},
    {'id': 3, 'name': 'Product 3', 'price': 15.49}
]

# Get all products
@app.route('/api/products', methods=['GET'])
def get_products():
    return jsonify(products)

# Get a specific product
@app.route('/api/products/<int:product_id>', methods=['GET'])
def get_product(product_id):
    product = next((p for p in products if p['id'] == product_id), None)
    if product:
        return jsonify(product)
    else:
        return jsonify({'error': 'Product not found'}), 404

# Create a new product
@app.route('/api/products', methods=['POST'])
def create_product():
    new_product = {
        'id': len(products) + 1,
        'name': request.json['name'],
        'price': request.json['price']
    }
    products.append(new_product)
    return jsonify(new_product), 201

# Update an existing product
@app.route('/api/products/<int:product_id>', methods=['PUT'])
def update_product(product_id):
    product = next((p for p in products if p['id'] == product_id), None)
    if product:
        product['name'] = request.json.get('name', product['name'])
        product['price'] = request.json.get('price', product['price'])
        return jsonify(product)
    else:
        return jsonify({'error': 'Product not found'}), 404

# Delete a product
@app.route('/api/products/<int:product_id>', methods=['DELETE'])
def delete_product(product_id):
    product = next((p for p in products if p['id'] == product_id), None)
    if product:
        products.remove(product)
        return jsonify({'message': 'Product deleted'})
    else:
        return jsonify({'error': 'Product not found'}), 404

if __name__ == '__main__':
    app.run()
