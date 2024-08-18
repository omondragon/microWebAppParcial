from flask import Blueprint, request, jsonify, session, g
from users.models.user_model import Users
from db.db import db
from datetime import timedelta


user_controller = Blueprint('user_controller', __name__)

@user_controller.route('/api/users', methods=['GET'])
def get_users():
    print("listado de usuarios")

    #print(g.__dict__)

    users = Users.query.all()
    result = [{'id':user.id, 'name': user.name, 'email': user.email, 'username': user.username} for user in users]
    return jsonify(result)

# Get single user by id
@user_controller.route('/api/users/<int:user_id>', methods=['GET'])
def get_user(user_id):
    print("obteniendo usuario")
    user = Users.query.get_or_404(user_id)
    return jsonify({'id': user.id, 'name': user.name, 'email': user.email, 'username': user.username})

@user_controller.route('/api/users', methods=['POST'])
def create_user():
    print("creando usuario")
    data = request.json
    #new_user = Users(name="oscar", email="oscar@gmail", username="omondragon", password="123")
    new_user = Users(name=data['name'], email=data['email'], username=data['username'], password=data['password'])
    db.session.add(new_user)
    db.session.commit()
    return jsonify({'message': 'User created successfully'}), 201

# Update an existing user
@user_controller.route('/api/users/<int:user_id>', methods=['PUT'])
def update_user(user_id):
    print("actualizando usuario")
    user = Users.query.get_or_404(user_id)
    data = request.json
    user.name = data['name']
    user.email = data['email']
    user.username = data['username']
    user.password = data['password']
    db.session.commit()
    return jsonify({'message': 'User updated successfully'})

# Delete an existing user
@user_controller.route('/api/users/<int:user_id>', methods=['DELETE'])
def delete_user(user_id):
    user = Users.query.get_or_404(user_id)
    db.session.delete(user)
    db.session.commit()
    return jsonify({'message': 'User deleted successfully'})

@user_controller.route('/api/login', methods=['POST'])
def login():
    data = request.json

    username = data.get('username')
    password = data.get('password')

    if not username or not password:
        return jsonify({'message': 'Missing username or password'}),400

    user = Users.query.filter_by(username=username).first()

    if not user:
        return jsonify({'message': 'Invalid username or password'}), 401

    #if not check_password_hash(user.password, password):
    if user.password != password:
        return jsonify({'message': 'Invalid username or password'}), 401

    # Store user information in session
    session['user_id'] = user.id
    session['username'] = user.username
    session['email'] = user.email  # Add other user information as needed

    #g.user=user

    #print(g.__dict__)
    print("En session: ",session)

    return jsonify({'message': 'Login successful'})
