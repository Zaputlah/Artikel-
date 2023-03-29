from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:@localhost/posts'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)
migrate = Migrate(app, db)


class posts(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    title = db.Column(db.String(80), nullable=False)
    content = db.Column(db.Text(), nullable=False)
    category = db.Column(db.String(50), nullable=False)
    created_date = db.Column(db.TIMESTAMP, nullable=False,
                             server_default=db.func.current_timestamp())
    updated_date = db.Column(db.TIMESTAMP, nullable=False, server_default=db.func.current_timestamp(
    ), onupdate=db.func.current_timestamp())
    status = db.Column(db.Enum('publish', 'draft', 'thrash'),
                       nullable=False, server_default='draft')


if __name__ == '__main__':
    app.run()
