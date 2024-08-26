from flask import Flask, jsonify, render_template, request
from flask_sqlalchemy import *
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column
from sqlalchemy import Integer, String, Boolean
import random

'''
Install the required packages first: 
Open the Terminal in PyCharm (bottom left). 

On Windows type:
python -m pip install -r requirements.txt

On MacOS type:
pip3 install -r requirements.txt

This will install the packages from requirements.txt for this project.
'''

app = Flask(__name__)

# CREATE DB
class Base(DeclarativeBase):
    pass
# Connect to Database
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///cafes.db'
db = SQLAlchemy(model_class=Base)
db.init_app(app)


# Cafe TABLE Configuration
class Cafe(db.Model):
    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    name: Mapped[str] = mapped_column(String(250), unique=True, nullable=False)
    map_url: Mapped[str] = mapped_column(String(500), nullable=False)
    img_url: Mapped[str] = mapped_column(String(500), nullable=False)
    location: Mapped[str] = mapped_column(String(250), nullable=False)
    seats: Mapped[str] = mapped_column(String(250), nullable=False)
    has_toilet: Mapped[bool] = mapped_column(Boolean, nullable=False)
    has_wifi: Mapped[bool] = mapped_column(Boolean, nullable=False)
    has_sockets: Mapped[bool] = mapped_column(Boolean, nullable=False)
    can_take_calls: Mapped[bool] = mapped_column(Boolean, nullable=False)
    coffee_price: Mapped[str] = mapped_column(String(250), nullable=True)

    def to_dict(self):
        return {
            'id': self.id,
            'name': self.name,
            'map_url': self.map_url,
            'img_url': self.img_url,
            'location': self.location,
            'has_sockets': self.has_sockets,
            'has_toilet': self.has_toilet,
            'has_wifi': self.has_wifi,
            'can_take_calls': self.can_take_calls,
            'seats': self.seats,
            'coffee_price': self.coffee_price
        }



with app.app_context():
    db.create_all()


@app.route("/")
def home():
    return render_template("index.html")

@app.route('/random', methods=['GET'])
def random_():
    cafe_data=db.session.execute(db.select(Cafe))
    all_cafes=cafe_data.scalars().all()
    random_cafe=random.choice(all_cafes)
    return jsonify(
        cafe={'name':random_cafe.name,
               'map_url':random_cafe.map_url,
               'img_url':random_cafe.img_url,
               'location':random_cafe.location,
               'has_sockets':random_cafe.has_sockets,
               'has_toilet':random_cafe.has_toilet,
               'has_wifi':random_cafe.has_wifi,
               'can_take_calls':random_cafe.can_take_calls,
               'seats':random_cafe.seats,
               'coffee_price':random_cafe.coffee_price
        }
    )

@app.route('/all',methods=['GET'])
def all():
    cafe_list=[]
    cafe_data=db.session.execute(db.select(Cafe))
    all_cafes=cafe_data.scalars().all()
    for cafe in all_cafes:
        cafe_list.append(cafe.to_dict())
    return jsonify(cafes=cafe_list)

@app.route('/search')
def search():
    cafe_list=[]
    loc = request.args.get('loc')
    cafe_data=db.session.execute(db.select(Cafe).where(Cafe.location==loc))
    all_cafes=cafe_data.scalars().all()
    if all_cafes:
        for cafe in all_cafes:
            cafe_list.append(cafe.to_dict())
        return jsonify(cafes=cafe_list)     
    else:
            return jsonify(error={'Not Found':"Sorry we don't have a cafe at that location."})                 

@app.route("/add", methods=["POST"])
def post_new_cafe():
    new_cafe = Cafe(
        name=request.form.get("name"),
        map_url=request.form.get("map_url"),
        img_url=request.form.get("img_url"),
        location=request.form.get("location"),
        has_sockets=bool(request.form.get("has_sockets")),
        has_toilet=bool(request.form.get("has_toilet")),
        has_wifi=bool(request.form.get("has_wifi")),
        can_take_calls=bool(request.form.get("can_take_calls")),
        seats=request.form.get("seats"),
        coffee_price=request.form.get("coffee_price"),
    )
    db.session.add(new_cafe)
    db.session.commit()
    return jsonify(response={"success": "Successfully added the new cafe."})

@app.route('/update-price/<int:id>', methods=['PATCH'])
def update(id):
    new_price=request.args.get("new_price")
    cafe_to_update = db.get_or_404(Cafe, id)
    if cafe_to_update:
        cafe_to_update.coffee_price = new_price
        db.session.commit()
        return jsonify(response={"success": "Successfully updated the cafe."}), 200
    else:
        return jsonify(response={"error":"No such cafe present."}),404
    
@app.route('/report-closed/<id>', methods=['DELETE'])
def delete(id):
    app_key="123452345"
    api_key=request.args.get('api_key')
    if app_key==api_key:
        result =  db.session.execute(db.select(Cafe).where(Cafe.id == id)).scalar()
        db.session.delete(result)
        db.session.commit()
        return jsonify(response={"success": "Successfully updated the cafe."}), 200
    else:
        return jsonify(response={"api_key invalid":"Not authorised to delete."}),405
# HTTP GET - Read Record

# HTTP POST - Create Record

# HTTP PUT/PATCH - Update Record

# HTTP DELETE - Delete Record


if __name__ == '__main__':
    app.run(debug=True)
