from flask import Blueprint, request, jsonify, make_response
from app import db
from app.models.board import Board
from app.routes.helper_routes import validate_id, validate_request

boards_bp = Blueprint("boards_bp", __name__, url_prefix="/boards")

@boards_bp.route("/<board_id>/cards", methods=["GET"])
def get_cards_from_one_board(board_id):
    board = validate_id(Board, board_id)
    response = board.to_dict()
    return make_response({"cards": response["cards"]}, 201)
