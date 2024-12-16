import chess
import chess.svg
from IPython.display import display, SVG

# Function to render the board
def render_board(board, scale=0.5):
    default_size = 800  # Default board size in pixels
    scaled_size = int(default_size * scale)
    board_svg = chess.svg.board(board=board, size=scaled_size)
    display(SVG(board_svg))