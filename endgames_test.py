import requests

# Function to fetch WDL and DTZ from Lichess Syzygy tablebase
def fetch_wdl_and_dtz_from_lichess(fen: str):
    """
    Fetch WDL (Win/Draw/Loss) and DTZ (Distance to Zero) for a given FEN
    from the Lichess Syzygy tablebase API, replacing spaces with underscores.
    """
    # Save original FEN for local processing
    original_fen = fen
    
    # Replace spaces with underscores in the FEN string for API compatibility
    fen = fen.replace(" ", "_")
    
    # Construct the URL for the Lichess Syzygy API request
    url = f"http://tablebase.lichess.ovh/standard?fen={fen}"
    
    try:
        # Make a GET request to the Lichess API
        response = requests.get(url)
        data = response.json()
        
        # Check if the 'category' field exists in the response
        if "category" in data:
            wdl = data["category"]
            dtz = data["dtz"]

            # Extract which player's turn it is from the original FEN (the second part of the FEN string)
            turn = original_fen.split()[1]  # "w" or "b"

            # Map WDL to the output text (Win/Draw/Loss) based on whose turn it is
            if wdl == "win":
                result = "Win for White" if turn == 'w' else "Win for Black"
            elif wdl == "loss":
                result = "Loss for White" if turn == 'w' else "Loss for Black"
            elif wdl == "draw":
                result = "Draw"
            else:
                result = "Unknown result"

            # Return the result as a dictionary
            return {
                "FEN": original_fen,
                "WDL": result,
                "DTZ": dtz,
                "WDL_numeric": 1 if wdl == "win" else -1 if wdl == "loss" else 0,
                "DTZ_numeric": dtz
            }
        else:
            return {"FEN": original_fen, "Error": "Position not available in tablebase."}
    except requests.exceptions.RequestException as e:
        return {"FEN": original_fen, "Error": f"Request failed: {e}"}

# Define a dictionary of test positions
test_positions = {
    "King vs King": "8/3K4/8/8/8/3k4/8/8 w - - 0 1",  # Draw
    "King and Pawn vs King": "8/8/4PK2/1k6/8/8/8/8 b - - 0 1",  # Win for White
    "King vs King and Rook": "8/8/8/1k6/8/1r6/4K3/8 b - - 0 1",  # Win for Black
    "King and Bishop vs King and Knight": "8/8/8/2n5/1k6/5B2/3K4/8 b - - 0 1",  # Draw
    "King and Queen vs King and Pawn": "8/8/3Q4/1k2P3/8/8/8/5K2 w - - 0 1",  # Win for White
}
