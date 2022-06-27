from app import db

class Board(db.Model):
    board_id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    title = db.Column(db.String, nullable=False)
    owner = db.Column(db.String, nullable=False)
    cards = db.relationship('Card', backref='board', lazy=True)

    def add_card(self, card):
        self.cards.append(card)
        db.session.commit()
    
    def to_dict(self):
        return {
            'id': self.id,
            'title': self.title,
            'owner': self.owner,
            'cards': [card.to_dict() for card in self.cards]
        }
