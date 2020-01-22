"""
    Generates OLL images.  

    @author Li Xiao-Tian
"""

import svg
import opll_common as op


OLL_STD_CODES = (
    'uuuuuuuuu',        # 00
    'lbrlurlfr',        # 01
    'lbblurlff',        # 02
    'bbrlurlfu',        # 03
    'lbulurffr',        # 04
    'bbrluuluu',        # 05
    'luuluuffr',        # 06
    'buruuruff',        # 07
    'ubbuurfur',        # 08
    'lubuurffu',        # 09
    'bbuuurluf',        # 10
    'bbrluuuuf',        # 11
    'uubluuffr',        # 12
    'bbuuuulff',        # 13
    'lbbuuuffu',        # 14
    'bbruuulfu',        # 15
    'lbuuuuffr',        # 16
    'ubblurlfu',        # 17
    'ubulurfff',        # 18
    'ubulurlfr',        # 19
    'ubulurufu',        # 20
    'bubuuufuf',        # 21
    'lubuuuluf',        # 22
    'bubuuuuuu',        # 23
    'buuuuufuu',        # 24
    'luuuuuuuf',        # 25
    'luuuuufur',        # 26
    'buruuuuuf',        # 27
    'uuuuurufu',        # 28
    'buuuurffu',        # 29
    'ubuluulur',        # 30
    'ubbuuruuf',        # 31
    'bbuluufuu',        # 32
    'bbuuuuffu',        # 33
    'lbruuuufu',        # 34
    'ubrluufuu',        # 35
    'ubruurfuu',        # 36
    'uuruurffu',        # 37
    'buuuurufr',        # 38
    'lbuuuuuff',        # 39
    'ubbuuulfu',        # 40
    'bubuurufu',        # 41
    'ubuuurfuf',        # 42
    'ubruuruur',        # 43
    'lbuluuluu',        # 44
    'lbuuuulfu',        # 45
    'uurluruur',        # 46
    'burluuffr',        # 47
    'lubuurlff',        # 48
    'bbruurfur',        # 49
    'lbbluuluf',        # 50
    'lbbuuulff',        # 51
    'lublurluf',        # 52
    'bbbuurfuf',        # 53
    'bubuurfff',        # 54
    'bbbuuufff',        # 55
    'lbruuulfr',        # 56
    'ubuuuuufu'         # 57
)


def oll(x, rotate=0, filename="oll.svg"):
    """
        Generates OLL images.  

        x: state code.  

        rotate: rotation angle, clockwise, in [-270, -180, -90, 0, 90, 180, 270].  

        filename: SVG filename.

        State code (x) syntax:
          1. int, OLL code, 1~57.
          2. 9-char string, specifying orientation of the 9 pieces (ULB, UB, URB, ..., ULR), 
             for example OLL20 (X-shaped) = 'ubulurufu'. Case-insensitive.
          3. list of 3-char strings. Each string specifies a 'colour patch',
             for example OLL20 = ['lbu', 'mbb', 'rbu', 'lsl', ..., 'rfu'].  
             Format: [lmr][bsf][ulrbf]
             The 1st and 2nd char specifies the position of the corner/edge/centre piece, and the 3rd char specifies its orientation. Case-insensitive.
    """

    states = []
    for bsf in 'bsf':
        for lmr in 'lmr':
            states.append(lmr+bsf)

    if isinstance(x, int):
        if x > 57 or x < 0:
            raise Exception("OLL code is %d, not in [1, 57]."%x)
        code = OLL_STD_CODES[x]
        for i in range(9):
            states[i] = states[i] + code[i]
    elif isinstance(x, str) and len(x) == 9:
        for i in range(9):
            states[i] = states[i] + x[i]
    elif isinstance(x, list):
        states = x
    else:
        raise Exception('Invalid OLL state code "%s".'%str(x))
        
    if rotate not in [-270, -180, -90, 0, 90, 180, 270]:
        raise Exception('Invalid angle: "%s".'%str(rotate))

    rect_str = ''
    for state in states:
        rect_coord = op.rect_top_coord(state)
        rect_str = rect_str + svg.element('rect', id=state, x=rect_coord[0], y=rect_coord[1], width=rect_coord[2], height=rect_coord[3], rotate=rotate)

    
    with open(filename, 'w') as f:
        f.write(op.SVG_HEAD)
        f.write(op.SVG_BG)
        f.write(op.GRID_STR)
        f.write(rect_str)
        f.write(svg.TAIL)
