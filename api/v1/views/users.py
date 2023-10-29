#!/usr/bin/python3
"""User views"""
from flask import jsonify, abort, request
from api.v1.views import app_views
from models import storage
from models.user import User

@app_views.route('/users', strict_slashes=False, methods=['GET', 'POST'])
def view_users():
    if request.method == 'POST':
        data = request.get_json()

        if data is None:
            return jsonify({"error": "Not a JSON"}), 400

        if 'email' not in data:
            return jsonify({'error': 'Missing email'}), 400
        if 'password' not in data:
            return jsonify({'error': 'Missing password'}), 400

        new_user = User(**data)
        storage.new(new_user)
        storage.save()
        return jsonify(new_user.to_dict()), 201

    if request.method == 'GET':
        users = storage.all(User)
        user_list = [user.to_dict() for user in users.values()]
        return jsonify(user_list)

@app_views.route('/users/<user_id>', strict_slashes=False, methods=['GET', 'DELETE', 'PUT'])
def view_user(user_id):
    user = storage.get(User, user_id)

    if user is None:
        abort(404)

    if request.method == 'GET':
        return jsonify(user.to_dict())

    if request.method == 'DELETE':
        storage.delete(user)
        storage.save()
        return jsonify({}), 200

    if request.method == 'PUT':
        data = request.get_json()

        if data is None:
            return jsonify({"error": "Not a JSON"}), 400

        # Update user object
        for key, value in data.items():
            if key not in ["id", "email", "created_at", "updated_at"]:
                setattr(user, key, value)

        storage.save()
        return jsonify(user.to_dict())

