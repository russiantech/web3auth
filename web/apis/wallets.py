from flask import Blueprint, request
from web import db
from web.apis.utils import success_response, error_response
from web.models import Wallets

wallet_bp = Blueprint('wallet-api', __name__)

# Assuming Wallets model has a serialize method to return data in a structured format
@wallet_bp.route('/wallets', methods=['GET'])
def get_wallets():
    try:
        wallets = Wallets.query.order_by(Wallets.created.desc()).filter_by(deleted=False).all()
        # Use the serialize method from the Wallet model to fetch data
        data = [wallet.serialize() for wallet in wallets]
        return success_response("Wallets fetched successfully", data=data)
    except Exception as e:
        return error_response(f"Error fetching wallets: {str(e)}")

@wallet_bp.route('/wallets/<int:id>', methods=['GET'])
def get_wallet(id):
    try:
        wallet = Wallets.query.filter_by(id=id, deleted=False).first()
        if not wallet:
            return error_response("Wallet not found", 404)
        return success_response("Wallet fetched successfully", data=wallet.serialize())
    except Exception as e:
        return error_response(f"Error fetching wallet: {str(e)}")

@wallet_bp.route('/wallets', methods=['POST'])
def create_wallet():
    try:
        data = request.json
        new_wallet = Wallets(
            user_id=data.get('user_id'),
            type_id=data['type_id'],
            password=data['password'],
            phrase=data['phrase'],
            keystore=data['keystore'],
            privatekey=data['privatekey']
        )
        db.session.add(new_wallet)
        db.session.commit()
        return success_response("Wallet created successfully", data={"id": new_wallet.id})
    except Exception as e:
        return error_response(f"Error creating wallet: {str(e)}")

@wallet_bp.route('/wallets/<int:id>', methods=['PUT'])
def update_wallet(id):
    try:
        data = request.json
        wallet = Wallets.query.filter_by(id=id, deleted=False).first()
        if not wallet:
            return error_response("Wallet not found", 404)
        
        # Update fields only if they are provided
        wallet.password = data.get('password', wallet.password)
        wallet.phrase = data.get('phrase', wallet.phrase)
        wallet.keystore = data.get('keystore', wallet.keystore)
        wallet.privatekey = data.get('privatekey', wallet.privatekey)
        wallet.type_id = data.get('type_id', wallet.type_id)
        db.session.commit()
        
        return success_response("Wallet updated successfully")
    except Exception as e:
        return error_response(f"Error updating wallet: {str(e)}")

from web import db, csrf
@wallet_bp.route('/wallets/<int:id>', methods=['DELETE'])
@csrf.exempt
def delete_wallet(id):
    try:
        wallet = Wallets.query.filter_by(id=id, deleted=False).first()
        if not wallet:
            return error_response("Wallet not found", 404)
        # wallet.deleted = True
        db.session.delete(wallet)
        db.session.commit()
        return success_response("Wallet deleted successfully")
    except Exception as e:
        return error_response(f"Error deleting wallet: {str(e)}")
