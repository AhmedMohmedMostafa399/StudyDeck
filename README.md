# Study Deck
a webpage build to help student study easily and with more efficiency and productivity by using new methods as flashcards and spaced-repetition 


**[Click here to open the webpage](https://ahmedmohmedmostafa399.github.io/signal-lost/)**

## Features
- Deck Creation
- Card Management
- RESTful Backend
- Spaced Repetition Ready

## Tech Stack
- Backend: Python, Flask, Flask-CORS
- Database: SQLite
- Frontend: HTML, CSS3, JavaScript

Endpoints:

    GET /api/decks (List all decks)   
    POST /api/decks (Create a deck)   
    GET /api/decks/<id>/cards (List cards in a deck)   
    POST /api/decks/<id>/cards (Add a card)   
    GET /api/decks/<id>/due (Get cards due for review)   
    POST /api/cards/<id>/review (Submit correct/incorrect result)   
    GET /api/stats (Get study stats)

JSON Card Structure :

    {
        "id": 1,
        "deck_id": 1,
        "front": "Question text",
        "back": "Answer text",
        "interval_days": 1,
        "next_review": "2026-09-20"
    }
