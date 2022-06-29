from flask import Blueprint, request, jsonify, make_response
from app import db
from app.models.card import Card
from app.routes.helper_routes import validate_id, validate_request

cards_bp = Blueprint("cards_bp", __name__, url_prefix="/cards")

@cards_bp.route("/<card_id>/like", methods=["PATCH"])
def like_card(card_id):
    card = validate_id(Card, card_id)
    card.likes += 1
    db.session.commit()
    return make_response({'details': f'Card {card_id} likes increased to {card.likes}.'})