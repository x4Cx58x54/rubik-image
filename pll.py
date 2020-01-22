"""
    Generates PLL images.  

    @author Li Xiao-Tian
"""

import svg
import opll_common as op

small_scale = 0.85
G_shape_offset = 18

PLL_STD_CODES = (
    ('',),                                  # 00
    #    Direc,Dbl,Scale,Offset
    (
        ('lbl', 'lbb', 'mbb', 'rbb', 'rbr', 'lfl', 'lff', 'rff', 'rfr'),
        ('64', False, 1, 0),
        ('48', False, 1, 0),
        ('86', False, 1, 0),
    ),                                      # 01
    (
        ('lbl', 'lbb', 'mbb', 'rbb', 'rbr', 'lfl', 'lff', 'rff', 'rfr'),
        ('46', False, 1, 0),
        ('68', False, 1, 0),
        ('84', False, 1, 0),
    ),                                      # 02
    (
        ('lbl', 'lbb', 'rbb', 'rbr', 'lfl', 'lff', 'rff', 'rfr'),
        ('28',  True, 1, 0),
        ('46',  True, 1, 0),
    ),                                      # 03
    (
        ('lbl', 'lbb', 'rbb', 'rbr', 'lfl', 'lff', 'rff', 'rfr'),
        ('26',  True, 1, 0),
        ('48',  True, 1, 0),
    ),                                      # 04
    (
        ('lbl', 'lbb', 'lsl', 'mbb', 'rsr', 'mff'),
        ('73', False, 1, 0),
        ('39', False, 1, 0),
        ('97', False, 1, 0),
    ),                                      # 05
    (
        ('lbl', 'lbb', 'lsl', 'mbb', 'rsr', 'mff'),
        ('37', False, 1, 0),
        ('79', False, 1, 0),
        ('93', False, 1, 0),
    ),                                      # 06
    (
        ('mbb', 'lsl', 'rsr', 'mff'),
        ('17',  True, 1, 0),
        ('39',  True, 1, 0),
    ),                                      # 07
    (
        ('lbl', 'lbb', 'mbb', 'lfl', 'lff', 'mff'),
        ('39',  True, 1, -8),
        ('46',  True, 1, 8),
    ),                                      # 08
    (
        ('lbl', 'lbb', 'lsl', 'lfl', 'lff', 'rsr'),
        ('28',  True, 1, 0),
        ('39',  True, 1, 0),
    ),                                      # 09
    (
        ('lsl', 'lfl', 'lff', 'mff', 'rbb', 'rbr'),
        ('19',  True, 1, 0),
        ('26',  True, 1, 0),
    ),                                      # 10
    (
        ('lfl', 'lff', 'mff', 'rbb', 'rbr', 'rsr'),
        ('19',  True, 1, 0),
        ('24',  True, 1, 0),
    ),                                      # 11
    (
        ('lbb', 'mbb', 'rbb', 'rbr', 'lsl', 'lbl'),
        ('79',  True, 1, 0),
        ('68',  True, 1, 0),
    ),                                      # 12
    (
        ('lbb', 'mbb', 'lff', 'lfl', 'lsl', 'lbl'),
        ('39',  True, 1, 0),
        ('68',  True, 1, 0),
    ),                                      # 13
    (
        ('mbb', 'rfr', 'rff', 'lff', 'lfl', 'lsl'),
        ('13',  True, 1, 0),
        ('68',  True, 1, 0),
    ),                                      # 14
    (
        ('lbb', 'rsr', 'mff', 'lff', 'lfl', 'lbl'),
        ('39',  True, 1, 0),
        ('24',  True, 1, 0),
    ),                                      # 15
    (
        ('lbl', 'lfl', 'mbb', 'rbb'),
        ('91', False, 1, G_shape_offset),
        ('17', False, 1, G_shape_offset),
        ('79', False, 1, G_shape_offset),
        ('46', False, small_scale, -G_shape_offset),
        ('68', False, small_scale, -G_shape_offset),
        ('84', False, small_scale, -G_shape_offset),
    ),                                      # 16
    (
        ('lbl', 'lfl', 'rsr', 'rfr'),
        ('13', False, 1, G_shape_offset),
        ('37', False, 1, G_shape_offset),
        ('71', False, 1, G_shape_offset),
        ('24', False, small_scale, -G_shape_offset),
        ('48', False, small_scale, -G_shape_offset),
        ('82', False, small_scale, -G_shape_offset),
    ),                                      # 17
    (
        ('lbl', 'lfl', 'mff', 'rff'),
        ('13', False, 1, G_shape_offset),
        ('37', False, 1, G_shape_offset),
        ('71', False, 1, G_shape_offset),
        ('24', False, small_scale, -G_shape_offset),
        ('46', False, small_scale, -G_shape_offset),
        ('62', False, small_scale, -G_shape_offset),
    ),                                      # 18
    (
        ('lbl', 'lfl', 'rbr', 'rsr'),
        ('91', False, 1, G_shape_offset),
        ('17', False, 1, G_shape_offset),
        ('79', False, 1, G_shape_offset),
        ('28', False, small_scale, -G_shape_offset),
        ('84', False, small_scale, -G_shape_offset),
        ('42', False, small_scale, -G_shape_offset),
    ),                                      # 19
    (
        ('mbb', 'rbb', 'rbr', 'mff', 'lff', 'lfl'),
        ('19',  True, 1, 0),
        ('46',  True, 1, 0),
    ),                                      # 20
    (
        ('lbb', 'mbb', 'rfr', 'rff', 'mff', 'lbl'),
        ('37',  True, 1, 0),
        ('46',  True, 1, 0),
    ),                                      # 21
)

def arrow_d(x, y, arrow_len=275, scale=1, rotate=0):
    '''
        Generates 'd' parameter in arrow path.
    '''

    head_length = 35*scale
    head_width = 70*scale
    tail_length = arrow_len
    tail_width = 10*scale

    #     |a|
    #    /\    -
    #   /  \   b
    #   -  -   _
    #    ||e
    #    ||
    #    ||    c
    #    ||
    #    ||
    #    ||    _
    #    --
    #    |d|

    a = head_width/2
    b = head_length
    c = tail_length
    d = tail_width
    e = a - d/2

    d = ['M', x, y, 'l', a, b, 'h', -e, 'v', c, 'h', -d, 'v', -c, 'h', -e, 'l', a, -b, 'z']

    return d

def arrow_path(x, double=False, scale=1, offset=0, rotate=0):
    """
        x: 2 char string. Specifying the start and the end of the arrow in numeric codes:

         ---
        |123|
        |456|
        |789|
         ---

        double: arrow is bi-directional if true.

        scale: factor the arrow is scaled.

        offset: distance the arrow moved outside from the standard position.

        rotate: rotation angle
        
        output: svg_str of arrow(s)
    """
    
    corner_straight_cw = ('71', '13', '39', '97')
    corner_straight_acw = ('93', '79', '17', '31')
    edge_straight = ('82', '46', '28', '64')
    corner_slant = ('91', '73', '19', '37')
    edge_slant_cw = ('42', '26', '68', '84')
    edge_slant_acw = ('62', '86', '48', '24')

    corner_straight_x = 125-offset
    corner_straight_y = 85
    corner_straight_len = 280+offset

    edge_straight_x = 570//2
    edge_straight_y = 85-offset
    edge_straight_len = 270

    corner_slant_x = 100-offset
    corner_slant_y = corner_slant_x
    corner_slant_len = 410+offset*1.4

    edge_slant_y = 100-offset
    edge_slant_len = 175

    if x in corner_straight_cw:
        spikex = corner_straight_x
        spikey = corner_straight_y
        arrow_len = corner_straight_len
        rotate_arrow = 90*corner_straight_cw.index(x)+rotate

    elif x in corner_straight_acw:
        spikex = 570 - corner_straight_x
        spikey = corner_straight_y
        arrow_len = corner_straight_len
        rotate_arrow = 90*corner_straight_acw.index(x)+rotate

    elif x in edge_straight:
        spikex = edge_straight_x
        spikey = edge_straight_y
        arrow_len = edge_straight_len
        rotate_arrow = 90*edge_straight.index(x)+rotate

    elif x in corner_slant:
        spikex = corner_slant_x
        spikey = corner_slant_y
        arrow_len = corner_slant_len
        rotate_arrow = (90*corner_slant.index(x)+rotate, 285, 285, -45, spikex, spikey)
            
    elif x in edge_slant_cw:
        spikey = edge_slant_y
        spikex = 360+50-edge_slant_y
        arrow_len = edge_slant_len
        rotate_arrow = (90*edge_slant_cw.index(x)+rotate, 285, 285, 45, spikex, spikey)
            
    elif x in edge_slant_acw:
        spikey = edge_slant_y
        spikex = 210-50+edge_slant_y
        arrow_len = edge_slant_len
        rotate_arrow = (90*edge_slant_acw.index(x)+rotate, 285, 285, -45, spikex, spikey)
            
    else:
        raise Exception("Invalid arrow code.")

    res = svg.element('path', id=x, d=arrow_d(spikex, spikey, arrow_len, scale), rotate=rotate_arrow)

    if double == True:
        res += arrow_path(x[1]+x[0], False, scale, offset, rotate)
     
    return res


def pll(x, rotate=0, filename="pll.svg"):
    """
        Generates PLL images.  
        
        x: state code, 1~21.

        rotate: rotation angle, clockwise, in [-270, -180, -90, 0, 90, 180, 270].  

        filename: SVG filename.
    """

    arrow_str = ''
    arrows = ''
    if isinstance(x, int):
        if x > 21 or x < 0:
            raise Exception("PLL code is %d, not in [1, 21]."%x)
        arrows = PLL_STD_CODES[x][1:]
    else:
        raise Exception('Invalid PLL state code "%s".'%str(x))

    if rotate not in [-270, -180, -90, 0, 90, 180, 270]:
        raise Exception('Invalid angle: "%s".'%str(rotate))
    
    for arrow in arrows:
        arrow_str += arrow_path(arrow[0], arrow[1], arrow[2], arrow[3], rotate)

    rect_str = ''
    for rect in PLL_STD_CODES[x][0]:
        rect_coord = op.rect_top_coord(rect)
        rect_str = rect_str + svg.element('rect', id=rect, x=rect_coord[0], y=rect_coord[1], width=rect_coord[2], height=rect_coord[3], rotate=rotate)

    with open(filename, 'w') as f:
        f.write(op.SVG_HEAD)
        f.write(op.SVG_BG)
        f.write(arrow_str)
        f.write(rect_str)
        f.write(op.GRID_STR)
        f.write(svg.TAIL)
