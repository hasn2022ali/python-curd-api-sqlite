from models import db, User

class UserService:
    def create_user(self, username, password, active=True):
        user = User(username=username, password=password, active=active)
        db.session.add(user)
        db.session.commit()
        return user
    
    def get_all_users(self):
        return User.query.all()
    
    def get_user_by_id(self, user_id):
        return User.query.get(user_id)
    
    def update_user(self, user_id, data):
        user = User.query.get(user_id)
        if not user:
            return None
        user.username = data.get('username', user.username)
        user.password = data.get('password', user.password)
        user.active = data.get('active', user.active)
        db.session.commit()
        return user
    
    def delete_user(self, user_id):
        user = User.query.get(user_id)
        if not user:
            return False
        db.session.delete(user)
        db.session.commit()
        return True