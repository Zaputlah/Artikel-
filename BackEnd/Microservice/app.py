from flask import Flask, jsonify, request
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:@localhost/posts'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)
migrate = Migrate(app, db)


class Article(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(80))
    body = db.Column(db.Text())
    category = db.Column(db.String(20))
    created_date = db.Column(
        db.TIMESTAMP, server_default=db.func.current_timestamp(), nullable=False)
    updated_date = db.Column(db.TIMESTAMP, server_default=db.func.current_timestamp(
    ), onupdate=db.func.current_timestamp(), nullable=False)
    status = db.Column(db.Enum('publish', 'draft', 'trash'), default='draft')


@app.route('/posts', methods=['POST'])
def create_article():
    data = request.get_json()
    article = Article(title=data['title'], body=data['body'],
                      category=data['category'], status=data['status'])
    db.session.add(article)
    db.session.commit()
    return jsonify({'message': 'Article created successfully!'})


@app.route('/posts/<int:limit>/<int:offset>', methods=['GET'])
def get_articles(limit, offset):
    articles = Article.query.limit(limit).offset(offset).all()
    output = []
    for article in articles:
        article_data = {}
        article_data['id'] = article.id
        article_data['title'] = article.title
        article_data['body'] = article.body
        article_data['category'] = article.category
        article_data['created_date'] = article.created_date
        article_data['updated_date'] = article.updated_date
        article_data['status'] = article.status
        output.append(article_data)
    return jsonify({'articles': output})


@app.route('/posts/<int:id>', methods=['GET'])
def get_article(id):
    article = Article.query.get_or_404(id)
    article_data = {}
    article_data['id'] = article.id
    article_data['title'] = article.title
    article_data['body'] = article.body
    article_data['category'] = article.category
    article_data['created_date'] = article.created_date
    article_data['updated_date'] = article.updated_date
    article_data['status'] = article.status
    return jsonify(article_data)


@app.route('/posts/<int:id>', methods=['PUT', 'PATCH'])
def update_article(id):
    article = Article.query.get_or_404(id)
    data = request.get_json()
    if 'title' in data:
        article.title = data['title']
    if 'body' in data:
        article.body = data['body']
    if 'category' in data:
        article.category = data['category']
    if 'status' in data:
        article.status = data['status']
    db.session.commit()
    return jsonify({'message': 'Article updated successfully!'})


@app.route('/posts/<int:id>', methods=['DELETE'])
def delete_article(id):
    article = Article.query.get_or_404(id)
    db.session.delete(article)
    db.session.commit()
    return jsonify({'message': 'Article deleted successfully!'})


if __name__ == '__main__':
    app.run(debug=True)
