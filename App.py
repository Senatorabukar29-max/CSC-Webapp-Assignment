from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

# Preloaded Nigerian foods
inventory = [
    {'name': 'Jollof Rice', 'quantity': 10},
    {'name': 'Egusi Soup', 'quantity': 5},
    {'name': 'Pounded Yam', 'quantity': 8},
    {'name': 'Moi Moi', 'quantity': 12},
    {'name': 'Suya', 'quantity': 15},
    {'name': 'Akara', 'quantity': 20},
    {'name': 'Amala', 'quantity': 7},
    {'name': 'Fufu', 'quantity': 9},
    {'name': 'Efo Riro', 'quantity': 6},
    {'name': 'Okra Soup', 'quantity': 4},
]

@app.route('/')
def home():
    return render_template('home.html', inventory=inventory)

@app.route('/add', methods=['POST'])
def add_item():
    name = request.form['name']
    quantity = request.form['quantity']
    inventory.append({'name': name, 'quantity': quantity})
    return redirect(url_for('home'))

@app.route('/delete/<int:item_id>')
def delete_item(item_id):
    if 0 <= item_id < len(inventory):
        inventory.pop(item_id)
    return redirect(url_for('home'))

@app.route('/update/<int:item_id>', methods=['POST'])
def update_item(item_id):
    if 0 <= item_id < len(inventory):
        inventory[item_id]['name'] = request.form['name']
        inventory[item_id]['quantity'] = request.form['quantity']
    return redirect(url_for('home'))

if __name__ == '__main__':
    app.run(debug=True)
