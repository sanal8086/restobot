from flask import Blueprint, jsonify, request
from firebase_client import get_db

tables_bp = Blueprint('tables', __name__)

@tables_bp.route('/table/<qr_token>', methods=['GET'])
def get_table(qr_token):
    db_ref = get_db()
    
    # Fast lookup using the global index
    table_lookup = db_ref.child(f'table_tokens/{qr_token}').get()
    
    if not table_lookup:
        return jsonify({'error': 'Table not found'}), 404
    
    return jsonify(table_lookup), 200
