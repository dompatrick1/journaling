from .db import db

class Comment(db.Model):
    __tablename__ = 'comments'

    id = db.Column(db.Integer, primary_key=True)
    body = db.Column(db.String(250), nullable=False)
    userId = db.Column(db.Integer, db.ForeignKey('users.id'), nullable = False)
    entryId = db.Column(db.Integer, db.ForeignKey('entries.id'), nullable=False)

    def to_dict(self):
        return {
            "id": self.id,
            "body": self.body,
            "userId": self.userId,
            "entryId": self.entryId
        }
