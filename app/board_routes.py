import json, os, requests
from app import db
from app.models.board import Board
from flask import Blueprint, jsonify, abort, make_response, request
from app.routes_helper import validate_id

boards_bp = Blueprint("boards_bp", __name__, url_prefix="/boards")

@boards_bp.route("", methods=["GET"])
def read_all_boards():
    boards = Board.query.all()
    boards_response = [board.to_dict() for board in boards]

    return make_response(jsonify(boards_response))

@boards_bp.route("/<board_id>", methods=["GET"])
def get_board_by_id(board_id):
    board_data = validate_id(board_id)
    board_dict = board_data.to_dict()

    return make_response(jsonify(dict(board=board_dict)))