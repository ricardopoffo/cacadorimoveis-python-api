from flask import Blueprint, jsonify, request
from app.models.scrap import Scrap
from app.models.real_estate import RealEstate
from app.service.real_estate import real_estate_create

real_estate_bp = Blueprint('real_estate', __name__)

# Real Estate Routes
# Real Estate list route
@real_estate_bp.route('/', methods=["GET"])
def get_all_real_estate():
    response_real_estate_list = RealEstate.query.all()
    real_estate_list = []
    for real_estate in response_real_estate_list:
        real_sate_data = {
            "id": real_estate.id,
            "name": real_estate.name
        }
        real_estate_list.append(real_sate_data)
    
    return jsonify(real_estate_list)

# Real Estate add route
@real_estate_bp.route('/add', methods=["POST"])
# @login_required
def real_estate_add():
    data = request.json
    if real_estate_create(data):
        return jsonify({"message": "Real Estate inserterd in Database"}), 200
    return jsonify({"message": "Invalid Real Estate data"}), 400
