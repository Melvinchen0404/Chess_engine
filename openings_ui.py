from IPython.display import display, SVG, clear_output
import chess.svg

# Render the board with optional scaling
def render_board(board, scale=0.5):
    default_size = 800  # Default board size in pixels
    scaled_size = int(default_size * scale)
    board_svg = chess.svg.board(board=board, size=scaled_size)
    display(SVG(board_svg))

# Render the board and print opening name
def render_board_with_opening(board, opening_name=None, scale=1.0):
    clear_output(wait=True)
    if opening_name:
        print(f"Opening Name: {opening_name}")
    else:
        print("No matching opening found.")
    render_board(board, scale)
