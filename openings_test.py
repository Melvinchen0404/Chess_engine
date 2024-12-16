import chess
from datasets import load_dataset

# Test bank of openings
test_openings = {
    'Dutch Defense': 'g2g3 f7f5',
    'Grob Opening': 'g2g4',
    "Barnes Opening: Fool's Mate": 'f2f3 e7e5 g2g4 d8h4',
    'Polish Opening': 'b2b4',
    'Sodium Attack': 'b1a3',
    'Nimzo-Larsen Attack': 'b2b3',
    'Zukertort Opening: Black Mustang Defense': 'g1f3 b8c6',
    'English Opening': 'c2c4',
    "King's Pawn Game": 'e2e4 e7e5',
    'Scandinavian Defense': 'e2e4 d7d5 b2b3',
    'Alekhine Defense': 'e2e4 g8f6 e4e5 f6d5 d2d4 d7d6 c2c4',
    'Caro-Kann Defense': 'e2e4 c7c6 d2d4 d7d5 b1c3 d5e4',
    'Sicilian Defense': 'e2e4 c7c5 g1f3 d7d6 d2d4 c5d4',
    'French Defense': 'e2e4 e7e6 d2d4 d7d5',
    "King's Pawn Game: Philidor Gambit": 'e2e4 e7e5 d2d4 d7d6 d4e5 c8d7'
}

# Load the chess openings dataset
def load_openings_dataset():
    dset = load_dataset("Lichess/chess-openings")
    train_data = dset['train']
    return {entry["name"]: entry["uci"] for entry in train_data}

# Get opening name by UCI sequence
def get_opening_name_by_uci(uci_sequence, openings_dict):
    for opening_name, opening_moves in openings_dict.items():
        if opening_moves == uci_sequence:
            return opening_name
    return None

# Generate a chess board from a UCI sequence
def generate_board_from_uci(uci_sequence):
    board = chess.Board()
    for move in uci_sequence.split():
        board.push_uci(move)
    return board
