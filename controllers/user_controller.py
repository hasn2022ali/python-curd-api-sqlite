from flask import request, jsonify, abort
from models import db, User
from schemas import user_schema, users_schema
from services import user_service
from . import user_bp

# create a new user
@user_bp.route('/users', methods=['POST'])
def create_user():
    json_data = request.get_json()
    if not json_data:
        return jsonify({"error", "No input data provided"}), 400
    
    errors = user_schema.validate(json_data)
    if errors:
        return jsonify(errors), 422
    
    username = json_data.get('username')
    password = json_data.get('password')
    active = json_data.get('active', True)

    # check if user already exists
    existing_user = User.query.filter_by(username=username).first()
    if existing_user:
        return jsonify({"error", "User with this username already exists"}), 400
    
    try:
        user = user_service.create_user(username, password, active)
        result = user_schema.dump(user)
        return jsonify({"message":"User created successfully", "user": result}), 201
    except Exception as e:
        db.session.rollback()
        return jsonify({"error", str(e)}), 500


# get all users
@user_bp.route("/users", methods=['GET'])
def get_users():
    users = user_service.get_all_users()
    result = users_schema.dump(users)
    return jsonify(result), 200

# get user details by user id
@user_bp.route("/users/<int:user_id>", methods=['GET'])
def get_user(user_id):
    user = user_service.get_user_by_id(user_id)
    if not user:
        return jsonify({"error", "User not found"}), 404
    result =  user_schema.dump(user)
    return jsonify(result), 200

# update user
@user_bp.route('users/<int:user_id>', methods=['PUT'])
def update_user(user_id):
    json_data = request.get_json()
    if not json_data:
        return jsonify({"error": "No input data provided"}), 400
    errors = user_schema.validate(json_data, partial=True)
    if errors:
        return jsonify(errors), 422
    try:
        user = user_service.update_user(user_id, json_data)
        if not user:
            return jsonify({"error": "User not found"}), 404
        result = user_schema.dump(user)
        return jsonify({"message": "User updated successfully", "user": result}), 200
    
    except Exception as e:
        db.session.rollback()
        return jsonify({"error", str(e)}), 500
    
# delete a user

@user_bp.route('/users/<int:user_id>', methods=['DELETE'])
def delete_user(user_id):
    try:
        success = user_service.delete_user(user_id)
        if not success:
            return jsonify({"error": "User not found"}), 404
        return jsonify({"message": "User deleted successfully"}), 200
    except Exception as e:
        db.session.rollback()
        return jsonify({"error": str(e)}),500
