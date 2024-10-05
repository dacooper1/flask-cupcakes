"""Flask app for Cupcakes"""
from flask import Flask, request, redirect, render_template, flash, jsonify, json
# from flask_debugtoolbar import DebugToolbarExtension
from models import db, connect_db, Cupcake
from forms import NewCupcake
from flask_wtf.csrf import CSRFProtect


app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = "postgresql:///cupcakes"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SECRET_KEY'] = 'ihaveasecret'

BASE_URL= "http://127.0.0.1:5000"
csrf = CSRFProtect(app)

# Having the Debug Toolbar show redirects explicitly is often useful;
# however, if you want to turn it off, you can uncomment this line:
#
# app.config['DEBUG_TB_INTERCEPT_REDIRECTS'] = False

# toolbar = DebugToolbarExtension(app)

connect_db(app)
app.app_context().push()
# db.create_all()

@app.route("/")
def index():
    """Render static homepage."""

    return render_template("index.html")

@app.route('/api/cupcakes')
@csrf.exempt
def get_all_cupcakes():
 
    cupcakes = Cupcake.query.all()
    c_list = [c.to_dict() for c in cupcakes]
    return jsonify(cupcakes = c_list), 200
    
@app.route('/api/cupcakes', methods=['POST'])
@csrf.exempt
def add_cupcake():
    data = request.json

    rating = data.get('rating')
    if not (1 <= int(rating) <= 5):
        return jsonify({"error": "Rating must be between 1 and 5."}), 400
    
    cupcake = Cupcake(
        flavor=data['flavor'],
        rating=rating,
        size=data['size'],
        image=data['image'] or None)

    db.session.add(cupcake)
    db.session.commit()

    return jsonify(cupcake=cupcake.to_dict())

@app.route('/api/cupcakes/<int:cupcake_id>', methods=['GET'])
@csrf.exempt
def get_cupcake(cupcake_id):
    cupcake = Cupcake.query.get_or_404(cupcake_id)

    return jsonify(cupcake=cupcake.to_dict()), 200
    

@app.route('/api/cupcakes/<int:cupcake_id>', methods=['PATCH'])
@csrf.exempt
def edit_cupcake(cupcake_id):
    cupcake = Cupcake.query.get_or_404(cupcake_id)

    data = request.json

    if 'flavor' in data:
        cupcake.flavor = data['flavor']
    if 'rating' in data:
        rating = data['rating']
        if not (1 <= int(rating) <= 5):
            return jsonify({"error": "Rating must be between 1 and 5."}), 400
        cupcake.rating = rating
    if 'size' in data:
        cupcake.size = data['size']
    if 'image' in data:
        cupcake.image = data['image'] or None

    db.session.commit()

    return jsonify(cupcake=cupcake.to_dict()), 200

@app.route('/api/cupcakes/<int:cupcake_id>', methods=['DELETE'])
@csrf.exempt
def delete_cupcake(cupcake_id):
    cupcake = Cupcake.query.get_or_404(cupcake_id)

    db.session.delete(cupcake)
    db.session.commit()

    return jsonify(message="Deleted"), 200
