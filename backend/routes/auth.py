from flask import Blueprint, request, jsonify
import bcrypt
import time
from firebase_client import get_db
from auth_utils import generate_token

auth_bp = Blueprint('auth', __name__)

# Public registration is disabled. Use SuperAdmin Panel.

@auth_bp.route('/auth/login', methods=['POST'])
def login():
    db_ref = get_db()
    data = request.get_json()
    
    email = data.get('email')
    password = data.get('password')
    
    if not email or not password:
        return jsonify({'message': 'Email and password required'}), 400
        
    user_query = db_ref.child('users').order_by_child('email').equal_to(email).get()
    if not user_query:
        return jsonify({'message': 'Invalid credentials'}), 401
        
    # user_query is a dict {uid: {data}}
    user_id = list(user_query.keys())[0]
    user = user_query[user_id]
    
    if bcrypt.checkpw(password.encode('utf-8'), user['password'].encode('utf-8')):
        token = generate_token(user_id, user['restaurant_id'])
        
        # Get restaurant info
        res = db_ref.child(f"restaurants/{user['restaurant_id']}").get()
        
        return jsonify({
            'token': token,
            'restaurant_id': user['restaurant_id'],
            'user': {
                'email': email,
                'name': user['name'],
                'restaurant_name': res.get('name')
            }
        }), 200
    else:
        return jsonify({'message': 'Invalid credentials'}), 401
