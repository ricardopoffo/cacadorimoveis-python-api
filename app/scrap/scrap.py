from flask import Blueprint

scrap_bp = Blueprint('scrap', __name__)

@scrap_bp.route('/', methods=["GET"])
def get_all_scrap():
    return 'Scrap root route'