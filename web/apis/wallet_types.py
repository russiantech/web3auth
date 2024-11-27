from flask import Blueprint, jsonify, request
from web import db, csrf
from web.apis.utils import success_response, error_response
from web.models import Wallets, Wallet_types

wallet_types_bp = Blueprint('wallet-type-api', __name__)

# Fetch all Wallet Types
@wallet_types_bp.route('/wallet-types', methods=['GET'])
def get_wallet_types():
    try:
        wallet_types = Wallet_types.query.filter_by(deleted=False).all()
        data = [{"id": wt.id, "title": wt.title, "image": wt.image} for wt in wallet_types]
        return success_response("Wallet types fetched successfully", data=data)
    except Exception as e:
        return error_response(f"An error occurred: {e}")

# Fetch a single Wallet Type by ID
@wallet_types_bp.route('/wallet-types/<int:id>', methods=['GET'])
def get_wallet_type(id):
    try:
        wallet_type = Wallet_types.query.filter_by(id=id, deleted=False).first()
        if not wallet_type:
            return error_response("Wallet type not found", status_code=404)
        return success_response("Wallet type fetched successfully", data={
            "id": wallet_type.id, "title": wallet_type.title, "image": wallet_type.image
        })
    except Exception as e:
        return error_response(f"An error occurred: {e}")

# Create a new Wallet Type
@wallet_types_bp.route('/wallet-types', methods=['POST'])
def create_wallet_type():
    try:
        data = request.json
        if not data.get('title') or not data.get('image'):
            return error_response("Title and Image are required", status_code=400)
        
        new_wallet_type = Wallet_types(
            title=data['title'],
            image=data['image'],
            user_id=data.get('user_id')
        )
        db.session.add(new_wallet_type)
        db.session.commit()
        return success_response("Wallet type created successfully", data={"id": new_wallet_type.id})
    except Exception as e:
        return error_response(f"An error occurred: {e}")

# Update an existing Wallet Type by ID
@wallet_types_bp.route('/wallet-types/<int:id>', methods=['PUT'])
def update_wallet_type(id):
    try:
        data = request.json
        wallet_type = Wallet_types.query.filter_by(id=id, deleted=False).first()
        if not wallet_type:
            return error_response("Wallet type not found", status_code=404)
        
        wallet_type.title = data.get('title', wallet_type.title)
        wallet_type.image = data.get('image', wallet_type.image)
        db.session.commit()
        
        return success_response("Wallet type updated successfully")
    except Exception as e:
        return error_response(f"An error occurred: {e}")

# Soft delete a Wallet Type by ID
@wallet_types_bp.route('/wallet-types/<int:id>', methods=['DELETE'])
def delete_wallet_type(id):
    try:
        wallet_type = Wallet_types.query.filter_by(id=id, deleted=False).first()
        if not wallet_type:
            return error_response("Wallet type not found", status_code=404)
        
        wallet_type.deleted = True
        db.session.commit()
        
        return success_response("Wallet type deleted successfully")
    except Exception as e:
        return error_response(f"An error occurred: {e}")

# 76 total
# Function to insert wallet data into the database
@wallet_types_bp.route('/wallet-insert')
def insert_wallets():
    wallets_data = [
        {"name": "Wallet Connect", "image": "../static/web3/wallets/assets/e726391f66eb7da7a0ed7d780b4df5e8e2416a17.png"},
        {"name": "Trust", "image": "../static/web3/wallets/assets/4622a2b2d6af1c9844944291e5e7351a6aa24cd7b23099efac1b2fd875da31a0.jpg"},
        {"name": "Metamask", "image": "../static/web3/wallets/assets/c57ca95b47569778a828d19178114f4db188b89b763c899ba0be274e97267d96.jpg"},
        {"name": "Ledger", "image": "../static/web3/wallets/assets/ledger_logo.png"},
        {"name": "BRD wallet", "image": "../static/web3/wallets/assets/brd.jpg"},
        {"name": "Coinbase", "image": "../static/web3/wallets/assets/Coinbaselogo_Supplied_250x250-2.png"},
        {"name": "Saitamask wallet", "image": "../static/web3/wallets/assets/saitama.png"},
        {"name": "Terra station", "image": "../static/web3/wallets/assets/terra.png"},
        {"name": "Phantom wallet", "image": "../static/web3/wallets/assets/phantom.jpg"},
        {"name": "Cosmos station", "image": "../static/web3/wallets/assets/cosmos.png"},
        {"name": "Exodus wallet", "image": "../static/web3/wallets/assets/exodus.png"},
        {"name": "Rainbow", "image": "../static/web3/wallets/assets/1ae92b26df02f0abca6304df07debccd18262fdf5fe82daa81593582dac9a369.jpg"},
        {"name": "Argent", "image": "../static/web3/wallets/assets/m92jEcPI_400x400.jpg"},
        {"name": "Binance Chain", "image": "../static/web3/wallets/assets/54043975-b6cdb800-4182-11e9-83bd-0cd2eb757c6e.png"},
        {"name": "Safemoon", "image": "../static/web3/wallets/assets/lg.png"},
        {"name": "Gnosis Safe", "image": "../static/web3/wallets/assets/lg(1).jpg"},
        {"name": "DeFi", "image": "../static/web3/wallets/assets/f2436c67184f158d1beda5df53298ee84abfc367581e4505134b5bcf5f46697d.jpg"},
        {"name": "Pillar", "image": "../static/web3/wallets/assets/pillar.png"},
        {"name": "imToken", "image": "../static/web3/wallets/assets/unnamed.png"},
        {"name": "ONTO", "image": "../static/web3/wallets/assets/dceb063851b1833cbb209e3717a0a0b06bf3fb500fe9db8cd3a553e4b1d02137.jpg"},
        {"name": "TokenPocket", "image": "../static/web3/wallets/assets/20459438007b75f4f4acb98bf29aa3b800550309646d375da5fd4aac6c2a2c66.jpg"},
        {"name": "Aave", "image": "../static/web3/wallets/assets/aave-aave-logo.png"},
        {"name": "Digitex", "image": "../static/web3/wallets/assets/2772.png"},
        {"name": "Portis", "image": "../static/web3/wallets/assets/portis_logo_dribbble.png"},
        {"name": "Formatic", "image": "../static/web3/wallets/assets/rtDOqMXY_400x400.jpg"},
        {"name": "MathWallet", "image": "../static/web3/wallets/assets/7674bb4e353bf52886768a3ddc2a4562ce2f4191c80831291218ebd90f5f5e26.jpg"},
        {"name": "BitPay", "image": "../static/web3/wallets/assets/1581439195205.jpg", "modal_target": "#exampleModal20"},
        {"name": "Ledger Live", "image": "../static/web3/wallets/assets/lg(2).jpg", "modal_target": "#exampleModal21"},
        {"name": "WallETH", "image": "../static/web3/wallets/assets/28189800.png", "modal_target": "#exampleModal22"},
        {"name": "Authereum", "image": "../static/web3/wallets/assets/49746116.png", "modal_target": "#exampleModal23"},
        {"name": "Dharma", "image": "../static/web3/wallets/assets/5DxVDK36_400x400.png", "modal_target": "#exampleModal24"},
        {"name": "1inch Wallet", "image": "../static/web3/wallets/assets/lg(3).jpg", "modal_target": "#exampleModal25"},
        {"name": "Huobi", "image": "../static/web3/wallets/assets/lg(4).jpg", "modal_target": "#exampleModal26"},
        {"name": "Eidoo", "image": "../static/web3/wallets/assets/8EXrk57o_400x400.jpg", "modal_target": "#exampleModal27"},
        {"name": "MYKEY", "image": "../static/web3/wallets/assets/512x512bb.jpg", "modal_target": "#exampleModal28"},
        {"name": "Loopring", "image": "../static/web3/wallets/assets/lg(5).jpg", "modal_target": "#exampleModal29"},
        {"name": "TrustVault", "image": "../static/web3/wallets/assets/trustvault.png", "modal_target": "#exampleModal30"},
        {"name": "Atomic", "image": "../static/web3/wallets/assets/unnamed(1).png", "modal_target": "#exampleModal31"},
        {"name": "Coin98", "image": "../static/web3/wallets/assets/10903.png", "modal_target": "#exampleModal32"},
        {"name": "Tron", "image": "../static/web3/wallets/assets/tron-trx-logo.png", "modal_target": "#exampleModal33"},
        {"name": "Alice", "image": "data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAOEAAADhCAMAAAAJbSJIAAAAeFBMVEX..."},
        {"name": "AlphaWallet", "image": "../static/web3/wallets/assets/138f51c8d00ac7b9ac9d8dc75344d096a7dfe370a568aa167eabc0a21830ed98.jpg"},
        {"name": "D'CENT", "image": "../static/web3/wallets/assets/unnamed(2).png"},
        {"name": "ZelCore", "image": "../static/web3/wallets/assets/6323b69954bc41ff9409f033_public.png"},
        {"name": "Nash", "image": "../static/web3/wallets/assets/lg(6).jpg"},
        {"name": "Coinmoni", "image": "../static/web3/wallets/assets/1433894569.png"},
        {"name": "GridPlus", "image": "../static/web3/wallets/assets/28931745.png"},
        {"name": "CYBAVO", "image": "../static/web3/wallets/assets/unnamed(3).png"},
        {"name": "Tokenary", "image": "../static/web3/wallets/assets/512x512bb(1).jpg"},
        {"name": "Torus", "image": "../static/web3/wallets/assets/44049579.png"},
        {"name": "Spatium", "image": "../static/web3/wallets/assets/unnamed(4).png"},
        {"name": "SafePal", "image": "../static/web3/wallets/assets/0b415a746fb9ee99cce155c2ceca0c6f6061b1dbca2d722b3ba16381d0562150.jpg"},
        {"name": "Infinito", "image": "../static/web3/wallets/assets/unnamed(5).png"},
        {"name": "wallet.io", "image": "../static/web3/wallets/assets/images.png"},
        {"name": "Ownbit", "image": "../static/web3/wallets/assets/unnamed(6).png"},
        {"name": "EasyPocket", "image": "../static/web3/wallets/assets/512x512bb(2).jpg"},
        {"name": "Bridge Wallet", "image": "../static/web3/wallets/assets/unnamed(7).png"},
        {"name": "Spark Point", "image": "../static/web3/wallets/assets/Sparkpoint-wallet-logo.png"},
        {"name": "ViaWallet", "image": "../static/web3/wallets/assets/unnamed(8).png"},
        {"name": "BitKeep", "image": "../static/web3/wallets/assets/ofbdehdu4sju07vlltgf.jpg"},
        {"name": "Vision", "image": "../static/web3/wallets/assets/images(1).jpg"},
        {"name": "PEAKDEFI", "image": "../static/web3/wallets/assets/unnamed(9).png"},
        {"name": "Unstoppable", "image": "../static/web3/wallets/assets/unnamed(10).png"},
        {"name": "HaloDeFi", "image": "../static/web3/wallets/assets/76861339.png"},
        {"name": "Dok Wallet", "image": "../static/web3/wallets/assets/unnamed(11).png"},
        {"name": "Midas", "image": "../static/web3/wallets/assets/images(2).png"},
        {"name": "Ellipal", "image": "../static/web3/wallets/assets/1_N6Uvv2QMQGqQubnGP1tGig.png"},
        {"name": "KEYRING PRO", "image": "../static/web3/wallets/assets/LOGO-KEYRING-PRO.png"},
        {"name": "Aktionariat", "image": "../static/web3/wallets/assets/19ad8334f0f034f4176a95722b5746b539b47b37ce17a5abde4755956d05d44c.jpg"},
        {"name": "Talken", "image": "../static/web3/wallets/assets/unnamed(12).png"},
        {"name": "Flare", "image": "../static/web3/wallets/assets/0x0.png"},
        {"name": "KyberSwap", "image": "../static/web3/wallets/assets/lg(7).jpg"},
        {"name": "PayTube", "image": "../static/web3/wallets/assets/unnamed(13).png"},
        {"name": "Linen", "image": "../static/web3/wallets/assets/dd8ee41915d967e547c80266e883d77ee808427405f4e8026a85ac1308104221.jpg"},
        {"name": "Kucoin", "image": "../static/web3/wallets/assets/crypto-kucoin.webp"},
        {"name": "Other Wallets", "image": "../static/web3/wallets/assets/c2a7686e-a832-4f09-9e31-29ffafcf9b75_20-45_Crypto-wallet_Blog.avif"},
    ]

    # Insert each wallet into the database
    for wallet_data in wallets_data:
        wallet = Wallet_types(
            title=wallet_data["name"],
            image=wallet_data["image"]
        )
        db.session.add(wallet)
    
    db.session.commit()
    print("Wallet data inserted successfully!")
