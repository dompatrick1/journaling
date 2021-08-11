from .db import db


class Entry(db.Model):
    _tablename_ = 'entries'

    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(60), nullable=False)
    description = db.Column(db.String(250), nullable=False)
    text = db.Column(db.String(5000), nullable=False)
    public = db.Column(db.Boolean, nullable=False)
    userId = db.Column(db.Integer, db.ForeignKey('users.id'), nullable = False)

    def to_dict(self):
        return {
            "id": self.id,
            "title": self.title,
            "description": self.description,
            "text": self.text,
            "public": self.public,
            "userId": self.userId
        }
