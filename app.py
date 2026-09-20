import sqlite3
from flask import Flask, jsonify, request
from flask_cors import CORS
app = Flask(__name__)
CORS(app)
def get_db():
    conn = sqlite3.connect('database.db')
    conn.row_factory = sqlite3.Row
    return conn
@app.route('/api/ping', methods=['GET'])
def ping():
    return jsonify({"status": "ok"})
@app.route('/api/decks', methods=['GET'])
def get_decks():
    conn = get_db()
    decks = conn.execute('SELECT * FROM decks').fetchall()
    conn.close()
    return jsonify([dict(deck) for deck in decks]), 200
@app.route('/api/decks', methods=['POST'])
def create_deck():
    data = request.get_json()
    if not data or not data.get('name'):
        return jsonify({"error": "Deck name is required"}), 400
    conn = get_db()
    cursor = conn.cursor()
    cursor.execute('INSERT INTO decks (name) VALUES (?)', (data['name'],))
    conn.commit()
    deck_id = cursor.lastrowid
    conn.close()
    return jsonify({"id": deck_id, "name": data['name']}), 201
@app.route('/api/decks/<int:deck_id>/cards', methods=['GET'])
def get_cards(deck_id):
    conn = get_db()
    cards = conn.execute('SELECT * FROM cards WHERE deck_id = ?', (deck_id,)).fetchall()
    conn.close()
    return jsonify([dict(card) for card in cards]), 200
@app.route('/api/decks/<int:deck_id>/cards', methods=['POST'])
def create_card(deck_id):
    data = request.get_json()
    if not data or not data.get('front') or not data.get('back'):
        return jsonify({"error": "Front and back fields are required"}), 400
    conn = get_db()
    cursor = conn.cursor()
    cursor.execute(
        'INSERT INTO cards (deck_id, front, back) VALUES (?, ?, ?)',
        (deck_id, data['front'], data['back'])
    )
    conn.commit()
    card_id = cursor.lastrowid
    conn.close()
    return jsonify({
        "id": card_id,
        "deck_id": deck_id,
        "front": data['front'],
        "back": data['back']
    }), 201
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)