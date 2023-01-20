from extensions import db

class User(db.Model):

    __tablename__ = "user"

    id = db.Column(db.Integer, primary_key = True)
    username = db.Column(db.String(100), nullable = False, unique= True)
    password = db.Column(db.String(200))

    @property
    def data(self):
        return{
            'id': self.id,
            'username':self.username}


    def save (self):
        db.session.add(self)
        db.session.commit()

    @classmethod
    def get_by_username(cls, username):
        return cls.query.filter_by(username=username).first()

