from flask import Flask, jsonify, request, abort, make_response
# from sqlalchemy.orm import relationship

from config import Configuration
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime, timedelta
import secrets

app = Flask(__name__)
app.config.from_object(Configuration)
db = SQLAlchemy(app)


class Cars(db.Model):
    __tablename__ = 'cars'
    id = db.Column(db.Integer, primary_key=True)
    car_name = db.Column(db.String(100))
    user_id = db.Column(db.Integer(), db.ForeignKey('users.id'))
    date_from = db.Column(db.DateTime, default=datetime.now())
    date_to = db.Column(db.DateTime, default=datetime.now())
    info = db.Column(db.String(404))

    @property
    def serialize(self):
        return {'id': self.id, 'car_name': self.car_name, "user_id": self.user_id, 'date_from': self.date_from, 'date_to': self.date_to, "info": self.info}


class User(db.Model):
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100))
    status = db.Column(db.Integer(), default=0)
    api_key = db.Column(db.String(32))

    def __init__(self, *args, **kwargs):
        super(User, self).__init__(*args, **kwargs)
        self.api_key = secrets.token_urlsafe(16)

    @property
    def serialize(self):
        return {'id': self.id, 'name': self.name, 'status': self.status}

@app.route('/rent', methods=["POST"])
def rent():
    if not 'api_key' in request.headers:
        abort(401)
    api_key = request.headers["api_key"].split("_")
    user = User.query.get(api_key[0])
    if user is None or user.api_key != api_key[1]:
        abort(401)
    if not request.json or not 'car_id' in request.json:
        abort(400)
    car = Cars.query.get(request.json["car_id"])
    if not car:
        abort(404)
    if car.date_to > datetime.now():
        abort(403)
    car.date_from = datetime.now()
    car.date_to = datetime.now() + timedelta(days=1)
    car.user_id = user.id
    db.session.add(car)
    db.session.commit()
    return jsonify(car.serialize)



@app.route('/users', methods=["POST", "GET"])
def get_users():
    if request.method == "GET":
        return jsonify([i.serialize for i in User.query.all()])
    elif request.method == "POST":
        if not 'api_key' in request.headers:
            abort(401)
        api_key = request.headers["api_key"].split("_")
        user = User.query.get(api_key[0])
        if user is None or user.api_key != api_key[1]:
            abort(401)
        if user.status != 1:
            abort(406)
        if not request.json or not 'name' in request.json or not 'status' in request.json:
            abort(400)
        u = User(name=request.json["name"], status=request.json["status"])
        db.session.add(u)
        db.session.commit()
        return jsonify(u.serialize)


@app.route('/users/<int:user_id>', methods=["GET", "DELETE", "PUT"])
def user(user_id):
    user_info = User.query.get(user_id)
    if user_info is None:
        abort(404)
    if request.method == "GET":
        return jsonify(user_info.serialize)
    elif request.method == "PUT":
        if not 'api_key' in request.headers:
            abort(401)
        api_key = request.headers["api_key"].split("_")
        user = User.query.get(api_key[0])
        if user is None or user.api_key != api_key[1]:
            abort(401)
        if user.status != 1 and user.id != user_info.id:
            abort(406)
        if not request.json or not 'name' in request.json:
            return jsonify(user_info.serialize)
        else:
            user_info.name = request.json["name"]
            db.session.add(user_info)
            db.session.commit()
            return jsonify(user_info.serialize)
    elif request.method == "DELETE":
        if not 'api_key' in request.headers:
            abort(401)
        api_key = request.headers["api_key"].split("_")
        user = User.query.get(api_key[0])
        if user is None or user.api_key != api_key[1]:
            abort(401)
        if user.root != 1 and user.id != user_info.id:
            abort(406)
        db.session.delete(user_info)
        db.session.commit()
        return jsonify({"status": "ok"})


@app.route('/cars', methods=["POST", "GET"])
def get_cars():
    if request.method == "GET":
        return jsonify([i.serialize for i in Cars.query.all()])
    elif request.method == "POST":
        if not 'api_key' in request.headers:
            abort(401)
        else:
            api_key = request.headers["api_key"].split("_")
            user = User.query.get(api_key[0])
            if user is None or user.api_key != api_key[1]:
                abort(401)
            if user.status != 1:
                abort(406)
            if not request.json or not 'car_name' in request.json:
                abort(400)
            car = Cars(car_name=request.json["car_name"], info=request.json.get('info', ''))
            db.session.add(car)
            db.session.commit()
            return jsonify(car.serialize)


@app.route('/cars/<int:car_id>', methods=["GET", "DELETE", "PUT"])
def car(car_id):
    car_info = Cars.query.get(car_id)
    if car_info is None:
        abort(404)
    if request.method == "GET":
        return jsonify(car_info.serialize)
    elif request.method == "PUT":
        if not 'api_key' in request.headers:
            abort(401)
        api_key = request.headers["api_key"].split("_")
        user = User.query.get(api_key[0])
        if user is None or user.api_key != api_key[1]:
            abort(401)
        if user.status != 1 and car.id != car_info.id:
            abort(406)
        if not request.json or not 'car_name' in request.json:
            return jsonify(car_info.serialize)
        else:
            car_info.name = request.json["car_name"]
            db.session.add(car_info)
            db.session.commit()
            return jsonify(car_info.serialize)
    elif request.method == "DELETE":
        if not 'api_key' in request.headers:
            abort(401)
        api_key = request.headers["api_key"].split("_")
        user = User.query.get(api_key[0])
        if user is None or user.api_key != api_key[1]:
            abort(401)
        if user.root != 1 and car.id != car_info.id:
            abort(406)
        db.session.delete(car_info)
        db.session.commit()
        return jsonify({"status": "ok"})


@app.errorhandler(400)
def not_found(error):
    return make_response(jsonify({'error': 'Bad data'}), 400)


@app.errorhandler(401)
def not_found(error):
    return make_response(jsonify({'error': 'Unauthorized'}), 401)


@app.errorhandler(406)
def not_found(error):
    return make_response(jsonify({'error': 'Not Acceptable'}), 406)


@app.errorhandler(404)
def not_found(error):
    return make_response(jsonify({'error': 'Not Found'}), 404)


@app.errorhandler(403)
def not_found(error):
    return make_response(jsonify({'error': 'Is rented'}), 403)


if __name__ == "__main__":
    app.run()
