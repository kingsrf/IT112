from flask import Flask, url_for, jsonify, request
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///games.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

#  Game Model 
class Game(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    genre = db.Column(db.String(50), nullable=False)
    platform = db.Column(db.String(50), nullable=False)

#  Game Sync Logic 
def sync_games(game_list):
    for game in game_list:
        if not Game.query.filter_by(title=game['title']).first():
            db.session.add(Game(**game))
    current_titles = {game['title'] for game in game_list}
    for existing in Game.query.all():
        if existing.title not in current_titles:
            db.session.delete(existing)
    db.session.commit()

#  Game List to Sync 
game_list = [
    {"title": "The Legend of Zelda", "genre": "Adventure", "platform": "Nintendo Switch"},
    {"title": "Halo Infinite", "genre": "Shooter", "platform": "Xbox Series X"},
    {"title": "God of War", "genre": "Action", "platform": "PlayStation 5"},
    {"title": "Minecraft", "genre": "Sandbox", "platform": "PC"},
    {"title": "Elden Ring", "genre": "RPG", "platform": "PC"}
]

#  Sync Database on Startup 
with app.app_context():
    db.create_all()
    sync_games(game_list)

#  Dashboard Route 
@app.route('/')
def dashboard():
    return f"""
    <head>
        <title>App Dashboard</title>
        <link rel="stylesheet" href="{url_for('static', filename='style.css')}">
    </head>
    <body>
        <h1>📦 King's App Dashboard</h1>
        <div class="button-container">
            <a href="/games" class="button-link">🎮 Game Library</a>
            <a href="https://linkedin.com/in/kingsambonge" target="_blank" class="button-link">🔗 LinkedIn</a>
            <a href="https://github.com/yourgithub" target="_blank" class="button-link">🐙 GitHub</a>
        </div>
    </body>
    """

#  Game List Page 
@app.route('/games')
def list_games():
    games = Game.query.all()
    game_list = ""
    for game in games:
        game_list += f"<li><a href='/games/{game.id}' class='button-link'>{game.title}</a></li>"
    return f"""
    <head>
        <title>Game List</title>
        <link rel="stylesheet" href="{url_for('static', filename='style.css')}">
    </head>
    <body>
        <h1>🎮 Games</h1>
        <ul>
            {game_list}
        </ul>
        <br>
        <a href='/' class='button-link'>🏠 Home</a>
    </body>
    """

#  Game Detail Page 
@app.route('/games/<int:game_id>')
def game_detail(game_id):
    game = Game.query.get_or_404(game_id)
    return f"""
    <head>
        <title>{game.title} - Details</title>
        <link rel="stylesheet" href="{url_for('static', filename='style.css')}">
    </head>
    <body>
        <h1>{game.title}</h1>
        <p><strong>Genre:</strong> {game.genre}</p>
        <p><strong>Platform:</strong> {game.platform}</p>
        <br>
        <a href='/games' class='button-link'>🔙</a>
    </body>
    """

#  API: Get All Games 
@app.route('/api/games', methods=['GET'])
def api_get_games():
    games = Game.query.all()
    data = [
        {
            "id": g.id,
            "title": g.title,
            "genre": g.genre,
            "platform": g.platform
        } for g in games
    ]
    return jsonify(data), 200

#  API: Add New Game 
@app.route('/api/games', methods=['POST'])
def api_add_game():
    try:
        data = request.get_json()
        title = data['title']
        genre = data['genre']
        platform = data['platform']

        new_game = Game(title=title, genre=genre, platform=platform)
        db.session.add(new_game)
        db.session.commit()

        return jsonify({"message": "Game added successfully!"}), 200
    except Exception as e:
        return jsonify({"error": "Failed to add game", "details": str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True)
