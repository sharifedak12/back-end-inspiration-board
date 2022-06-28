from flask import Blueprint, request, jsonify, make_response, abort
from app import db
from app.models.card import Card
'''
Helper Functions 
'''
def error_message(message, status_code):
    abort(make_response(jsonify(dict(details=message)), status_code))

# example_bp = Blueprint('example_bp', __name__)
cards = Blueprint('cards', __name__)

@cards.route('/cards', methods=['POST'])
def create_card():
    """
    Create a new card
    """
    data = request.get_json()
    try:
        card = Card(messsage = data['message'], board_id = data['board_id'])
    except KeyError:
        error_message('Invalid Data', 400)
    db.session.add(card)
    db.session.commit()
    return jsonify(card.to_dict())
