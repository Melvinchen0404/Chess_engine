# chess_engine.py

import chess
import chess.engine
import requests

# Initialize Stockfish engine before starting the program
engine = chess.engine.SimpleEngine.popen_uci("/usr/games/stockfish")

def get_stockfish_best_move(board, depth=3):
    result = engine.play(board, chess.engine.Limit(time=2.0))
    return result.move.uci()

def close_engine():
    engine.quit()  # Ensure proper cleanup

def fetch_wdl_and_dtz_from_lichess(fen: str):
    """
    Fetch WDL (Win/Draw/Loss) and DTZ (Distance to Zero) for a given FEN
    from the Lichess Syzygy tablebase API, replacing spaces with underscores.
    """
    original_fen = fen
    fen = fen.replace(" ", "_")  # Replace spaces with underscores for API compatibility
    url = f"http://tablebase.lichess.ovh/standard?fen={fen}"

    try:
        response = requests.get(url)
        data = response.json()
        
        if "category" in data:
            wdl = data["category"]
            dtz = data["dtz"]
            turn = original_fen.split()[1]  # "w" or "b"
            result = {
                "win": f"Win for White" if turn == 'w' else "Win for Black",
                "loss": f"Loss for White" if turn == 'w' else "Loss for Black",
                "draw": "Draw"
            }.get(wdl, "Unknown result")
            
            return {"WDL": result, "DTZ": dtz}
        else:
            return {"Error": "Position not available in tablebase."}
    except requests.exceptions.RequestException as e:
        return {"Error": f"Request failed: {e}"}
