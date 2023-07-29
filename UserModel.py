class User:
    def __init__(self, uid, name, email, phone, password):
        self.uid = uid
        self.name = name
        self.email = email
        self.phone = phone
        self.password = password

    def __str__(self):
        return f"User({self.uid}, {self.name}, {self.email}, {self.phone}, {self.password})"


    def to_dict(self):
        return {
            'uid': self.uid,
            'name': self.name,
            'email': self.email,
            'phone': self.phone,
            'password': self.password
        }
    
    @staticmethod
    def users_to_dict(users):
        return {"data":[user.to_dict() for user in users]}

    @staticmethod
    def from_dict(source):
        return User(source['uid'], source['name'], source['email'], source['phone'], source['password'])
    