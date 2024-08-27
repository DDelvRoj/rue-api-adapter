from ..models.user import User
from ..extensions import db

def get_all_users():
    """Obtener todos los usuarios."""
    return User.query.all()

def get_user_by_id(user_id):
    """Obtener un usuario por ID."""
    return User.query.get(user_id)

def get_user_by_username(username):
    """Obtener un usuario por nombre de usuario."""
    return User.query.filter_by(username=username).first()

def create_user(username, email, password):
    """Crear un nuevo usuario."""
    new_user = User(username=username, email=email, password=password)
    db.session.add(new_user)
    db.session.commit()
    return new_user

def update_user(user_id, username=None, email=None, password=None):
    """Actualizar la información de un usuario."""
    user = User.query.get(user_id)
    if not user:
        return None
    
    if username:
        user.username = username
    if email:
        user.email = email
    if password:
        user.password = password

    db.session.commit()
    return user

def delete_user(user_id):
    """Eliminar un usuario."""
    user = User.query.get(user_id)
    if not user:
        return None
    
    db.session.delete(user)
    db.session.commit()
    return user
