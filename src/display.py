import random
import board
import displayio
from adafruit_display_shapes.rect import Rect

SQUARE_SIZE = const(20)

def main():
    display = board.DISPLAY
    display.auto_refresh = False

    root_group = displayio.Group()
    display.root_group = root_group

    ROWS = display.height // SQUARE_SIZE
    COLUMNS = display.width // SQUARE_SIZE

    grid = [
        [
            Rect(
                1 + r * SQUARE_SIZE,
                1 + c * SQUARE_SIZE,
                SQUARE_SIZE - 2,
                SQUARE_SIZE - 2,
                fill=0x00,
            )
            for c in range(COLUMNS)
        ]
        for r in range(ROWS)
    ]

    for r in range(ROWS):
        for c in range(COLUMNS):
            root_group.append(grid[r][c])

    while True:
        c = random.randrange(ROWS)
        r = random.randrange(COLUMNS)
        fill = random.getrandbits(24)
        grid[r][c].fill = fill
        display.refresh()

main()
