from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


DEFAULT_IMG = "https://tinyurl.com/demo-cupcake"

"""Models for Cupcake app."""

# It should have the following columns:

# - ***id***: a unique primary key that is an auto-incrementing integer
# - ***flavor***: a not-nullable text column
# - ***size***: a not-nullable text column
# - ***rating***: a not-nullable column that is a float
# - ***image***: a non-nullable text column. If an image is not given, default to https://tinyurl.com/demo-cupcake

class Cupcake(db.Model):
    __tablename__ = "cupcakes"

    id = db.Column(db.Integer, primary_key=True)
    flavor = db.Column(db.Text, nullable=False)
    size = db.Column(db.Text, nullable=False)
    rating = db.Column(db.Text, nullable=False)
    image =  db.Column(db.Text, nullable=False, default=DEFAULT_IMG)

    def __repr__(self):
        c = self 
        return f'id = {c.id}, flavor = {c.flavor}, size = {c.size}, rating = {c.rating}, image = {c.image}'
    
    def to_dict(self):
        return {
            'id': self.id,
            'flavor': self.flavor,
            'size': self.size,
            'rating': self.rating,
            'image': self.image
        }
    
    

def connect_db(app):
    """Connect this database to provided Flask app.

    You should call this in your Flask app.
    """

    db.app = app
    db.init_app(app)