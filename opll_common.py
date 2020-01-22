"""
    Common elements for OLL and PLL. Covers the grid and the rects.  

    @author Li Xiao-Tian
"""

import svg

RECT_CODES = [
    'lbu', 'lbb', 'lbl',
    'mbu', 'mbb',
    'rbu', 'rbb', 'rbr',
    'lsu', 'lsl',
    'msu', 
    'rsu', 'rsr',
    'lfu', 'lff', 'lfl',
    'mfu', 'mff',
    'rfu', 'rff', 'rfr'
]

GRID_UL = 40
GRID_PATCH_SIZE = 150
GRID_STROKE_WIDTH = 10
GRID_BLOCK_GAP = 10

SVG_SIZE = 256
VIEWBOX_SIZE = 570

BLOCK_LONG = GRID_PATCH_SIZE - 2*GRID_BLOCK_GAP  # =130
BLOCK_SHORT = 18

UPPER_LIMIT = 12
LOWER_LIMIT = VIEWBOX_SIZE - UPPER_LIMIT - BLOCK_SHORT

BLOCK_1 = GRID_UL + GRID_STROKE_WIDTH + GRID_BLOCK_GAP
BLOCK_2 = BLOCK_1 + GRID_PATCH_SIZE + GRID_STROKE_WIDTH
BLOCK_3 = BLOCK_2 + GRID_PATCH_SIZE + GRID_STROKE_WIDTH
BASELINE = {'l':BLOCK_1, 'm':BLOCK_2, 'r':BLOCK_3,
            'b':BLOCK_1, 's':BLOCK_2, 'f':BLOCK_3 }

def rect_top_coord(state):
    """
        state: 3-char code specifying the state of one corner/edge/centre piece.  

        output: a dict containing x, y, width and height of the rectangle.   

        Format: [lmr][bsf][ulrbf] (regex). The 1st and 2nd char specifies the position of the corner/edge/centre piece, and the 3rd char specifies its orientation.  
    """

    state = state.lower()
    if state not in RECT_CODES:
        raise Exception('Invalid OLL colour block code "%s".'%state)

    if state[2] == 'u':
        width = BLOCK_LONG
        height = BLOCK_LONG
        x = BASELINE[state[0]]
        y = BASELINE[state[1]]

    elif state[2] == 'l':
        width = BLOCK_SHORT
        height = BLOCK_LONG
        x = UPPER_LIMIT
        y = BASELINE[state[1]]

    elif state[2] == 'r':
        width = BLOCK_SHORT
        height = BLOCK_LONG
        x = LOWER_LIMIT
        y = BASELINE[state[1]]

    elif state[2] == 'f':
        width = BLOCK_LONG
        height = BLOCK_SHORT
        x = BASELINE[state[0]]
        y = LOWER_LIMIT

    elif state[2] == 'b':
        width = BLOCK_LONG
        height = BLOCK_SHORT
        x = BASELINE[state[0]]
        y = UPPER_LIMIT

    return x, y, width, height


def square_d(x, y, a, anticlockwise=False):
    '''
        Generates a 'd' in SVG path  
    '''

    if anticlockwise == False:
        h = 'h'
        v = 'v'
    else:
        h = 'v'
        v = 'h'
    return ['M', x, y, h, a, v, a, h, -a, v, -a,'z']

def grid_path():
    '''
        Generates a 'path' element of the U face grid.
    '''

    grid_d = square_d(GRID_UL, GRID_UL, GRID_STROKE_WIDTH*4 + GRID_PATCH_SIZE*3)
    for i in range(3):
        for j in range(3):
            x = GRID_UL + GRID_STROKE_WIDTH + i*(GRID_PATCH_SIZE + GRID_STROKE_WIDTH)
            y = GRID_UL + GRID_STROKE_WIDTH + j*(GRID_PATCH_SIZE + GRID_STROKE_WIDTH)
            grid_d.extend(square_d(x, y, GRID_PATCH_SIZE, anticlockwise=True))
    return svg.element('path', id="grid", d=grid_d)

GRID_STR = grid_path()

SVG_HEAD = svg.head(SVG_SIZE, SVG_SIZE, VIEWBOX_SIZE, VIEWBOX_SIZE)

SVG_BG = svg.element('rect', id="bg", width=VIEWBOX_SIZE, height=VIEWBOX_SIZE, fill="#ffffff")