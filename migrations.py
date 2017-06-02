from models import db, User
from werkzeug.security import generate_password_hash

db.drop_all()
db.create_all()
my_admin_user = User()
my_admin_user.email = 'paco@ocho.es'
my_admin_user.password = generate_password_hash('123')
my_admin_user.username = 'admin'
my_admin_user.is_active = True
my_admin_user.rol = 1
db.session.add(my_admin_user)
db.session.commit()
print('Admin creado')
print('OK')