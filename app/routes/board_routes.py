from flask import Blueprint, request, jsonify, make_response
from app import db
from app.models.board import Board
from app.routes.helper_routes import validate_id, validate_request

board_bp = Blueprint("board_bp", __name__, url_prefix="/boards")

# View a list of cards that belong to the selected board.
# need to add validate_id helper function
# need to add get_cards method to board
@board_bp.route("/<board_id>/cards", methods=["GET"])
def get_cards_from_one_board(board_id):
    board = validate_id(Board, board_id)
    response = board.to_dict()
    # response["cards"] = board.get_cards()
    # return make_response(response)
    return make_response({"cards": response["cards"]})
