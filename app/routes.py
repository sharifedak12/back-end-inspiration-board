from flask import Blueprint, request, jsonify, make_response
from app import db
from app.models.card import Card

# example_bp = Blueprint('example_bp', __name__)
cards = Blueprint('cards', __name__)

@cards.route('/cards', methods=['POST'])
def create_card():
    """
    Create a new card
    """
    data = request.get_json()
    card = Card(messsage = data['message'], board_id = data['board_id'])
    db.session.add(card)
    db.session.commit()
    return jsonify(card.to_dict())
