from backend.app import app, db
from backend.models import User, Student, SeatingHistory
from werkzeug.security import generate_password_hash

def init_db():
    with app.app_context():
        try:
            # Create all tables
            db.create_all()
            
            # Create admin user if not exists
            if not User.query.filter_by(username='admin').first():
                admin = User(
                    username='admin',
                    is_admin=True
                )
                admin.set_password('admin123')
                db.session.add(admin)
                db.session.commit()
                print("Admin user created successfully!")
            
            # Create regular user if not exists
            if not User.query.filter_by(username='user').first():
                user = User(
                    username='user',
                    is_admin=False
                )
                user.set_password('user123')
                db.session.add(user)
                db.session.commit()
                print("Regular user created successfully!")
            
            print("Database initialized successfully!")
        except Exception as e:
            print(f"Error initializing database: {str(e)}")
            db.session.rollback()

if __name__ == '__main__':
    init_db() 