# from flask import Flask
# from flask_sqlalchemy import SQLAlchemy
# from flask_socketio import join_room, leave_room, send, SocketIO


# db = SQLAlchemy()
# DB_NAME = "database.db"

# app = Flask(__name__)
# app.config['SECRET_KEY'] = 'TEST'
# #database is stored at the location defined on the right
# app.config['SQLALCHEMY_DATABASE_URI'] = f'sqlite:///{DB_NAME}'
# db.init_app(app)

    
# from views import views
# from auth import auth

# app.register_blueprint(views, url_prefix='/')
# app.register_blueprint(auth, url_prefix='/')

# socketio = SocketIO(app)

# if __name__ == '__main__':
#     socketio.run(app, debug=True)




