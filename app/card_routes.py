from flask import Blueprint, request, jsonify, abort, make_response
from app import db
from app.models.card import Card
from app.models.board import Board

cards_bp = Blueprint("cards_bp", __name__, url_prefix="/cards")

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
        abort(make_response({"message":f"cardfff {id} not found"}, 404))

    return model

def error_message(message, status_code):
    abort(make_response(jsonify(dict(details=message)), status_code))

