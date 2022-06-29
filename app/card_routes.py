from flask import Blueprint, request, jsonify, abort, make_response
from app import db
from app.models.card import Card

'''
Helper Functions 
'''
def error_message(message, status_code):
    abort(make_response(jsonify(dict(details=message)), status_code))


cards_bp = Blueprint("cards_bp", __name__, url_prefix="/cards")

@cards_bp.route("", methods=['POST'])
def create_card():
    """
    Create a new card
    """
    data = request.get_json()
    try:
        card = Card(messsage = data['message'], board_id = data['board_id'])
    except KeyError:
        error_message('Invalid data', 400)
    db.session.add(card)
    db.session.commit()
    return jsonify(card.to_dict())

@cards_bp.route("/<card_id>", methods=['DELETE'])
def delete_card(card_id):
    card = validate_card(Card, card_id)

    db.session.delete(card)
    db.session.commit()

    return make_response({"details": f'Card {card.card_id} "{card.message}" successfully deleted'})


def validate_card(cls, id):
    try:
        id = int(id)
    except:
        abort(make_response({"message":f"card {id} invalid"}, 400))

    model = cls.query.get(id)

    if not model:
        abort(make_response({"message":f"card {id} not found"}, 404))

    return model



