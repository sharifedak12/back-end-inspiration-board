from flask import Blueprint, request, jsonify, make_response
from app import db
from app.models.board import Board

board_bp = Blueprint('board_bp', __name__, url_prefix="/boards")

@board_bp.route("", methods=["POST"])
def create_board():
    request_body = request.get_json()

    try:
        board = Board(title=request_body["title"], owner=request_body["owner"])
    except KeyError as err:
        return make_response({"details": "Invalid data"}, 400)
    
    db.session.add(board)
    db.session.commit()

    return make_response({
        "id": board.board_id,
        "title": board.title,
        "owner": board.owner,
    }, 201)