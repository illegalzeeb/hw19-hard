from dao.model.user import User


class UserDAO:
    def __init__(self, session):
        self.session = session

    def get_one(self, bid):
        return self.session.query(User).get(bid)

    def get_all(self):
        return self.session.query(User).all()

    def get_by_login(self, username):
        return self.session.query(User).filter(User.username == username).one()

    def create(self, data):
        ent = User(**data)
        self.session.add(ent)
        self.session.commit()
        return ent

    def delete(self, rid):
        user = self.get_one(rid)
        self.session.delete(user)
        self.session.commit()

    def update(self, data):
        user = self.get_one(data.get("id"))
        user.name = data.get("name")
        user.role = data.get("role")
        user.password = data.get("password")
        self.session.add(user)
        self.session.commit()
