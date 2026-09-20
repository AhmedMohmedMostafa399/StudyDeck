let decks = JSON.parse(localStorage.getItem('study_decks')) || [];
let activeDeckId = null;

function save() {
  localStorage.setItem('study_decks', JSON.stringify(decks));
}

function loadDecks() {
  const list = document.getElementById('deck-list');
  list.innerHTML = '';
  
  decks.forEach(deck => {
    const li = document.createElement('li');
    li.textContent = deck.name;
    if (deck.id === activeDeckId) {
      li.style.fontWeight = 'bold';
    }
    li.onclick = () => selectDeck(deck.id, deck.name);
    list.appendChild(li);
  });
}

document.getElementById('deck-form').addEventListener('submit', (e) => {
  e.preventDefault();
  const nameInput = document.getElementById('deck-name');
  const name = nameInput.value.trim();
  if (!name) return;
  
  const newDeck = { id: Date.now(), name, cards: [] };
  decks.push(newDeck);
  save();
  nameInput.value = '';
  loadDecks();
});

function selectDeck(id, name) {
  activeDeckId = id;
  document.getElementById('selected-deck-title').textContent = `Deck: ${name}`;
  document.getElementById('card-section').style.display = 'block';
  loadDecks();
  loadCards();
}

function loadCards() {
  const list = document.getElementById('card-list');
  list.innerHTML = '';
  const activeDeck = decks.find(d => d.id === activeDeckId);
  if (!activeDeck || activeDeck.cards.length === 0) {
    list.innerHTML = '<li>No cards in this deck yet.</li>';
    return;
  }
  
  activeDeck.cards.forEach(card => {
    const li = document.createElement('li');
    li.textContent = `${card.front} | ${card.back}`;
    list.appendChild(li);
  });
}

document.getElementById('card-form').addEventListener('submit', (e) => {
  e.preventDefault();
  if (!activeDeckId) return;
  
  const frontInput = document.getElementById('card-front');
  const backInput = document.getElementById('card-back');
  
  const activeDeck = decks.find(d => d.id === activeDeckId);
  if (activeDeck) {
    activeDeck.cards.push({
      id: Date.now(),
      front: frontInput.value,
      back: backInput.value
    });
    save();
    frontInput.value = '';
    backInput.value = '';
    loadCards();
  }
});

loadDecks();