from .db import db

class Like(db.Model):
    __tablename__ = 'likes'

    id = db.Column(db.Integer, primary_key=True)
    entryId = db.Column(db.Integer, db.ForeignKey('entries.id'), nullable=False)
    userId = db.Column(db.Integer, db.ForeignKey('users.id'), nullable = False)

    def to_dict(self):
        return {
            "id": self.id,
            "entryId": self.entryId,
            "userId": self.userId
        }
