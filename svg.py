"""
    Generates SVG patterns.  

    @author Li Xiao-Tian
"""

def str_round3(x):
    '''
        Round x to at most 3 decimal places and convert to string.
    '''
    if isinstance(x, float):
        if abs(round(x, 0)-x) < 0.001:
            y = str(int(x))
        elif abs(round(x, 1)-x) < 0.001:
            y = '%.1f'%x
        elif abs(round(x, 2)-x) < 0.001:
            y = '%.2f'%x
        else:
            y = '%.3f'%x
    else:
        y = str(x)

    return y

def element(elem, **kwargs):
    """
        Generates SVG text.

        <*elem* *key*="*value*"/>

        'rotate' and 'd' parameters are specially treated.
    """

    svg_str = '\n<' + elem
    for key, value in kwargs.items():
        if key == 'd':
            pathd = ' d="'
            for i in value:
                pathd += str_round3(i) + ' '
            svg_str += pathd.rstrip() + '"'
        elif key == 'rotate':
            if isinstance(value, int):
                angle = str_round3(value)
                rotate_x = '285'                    # opll_common.VIEWBOX_SIZE / 2
                rotate_y = '285'
            elif isinstance(value, tuple):
                if len(value) == 3:                 # for rotations specifying centres
                    angle = str_round3(value[0])
                    rotate_x = str_round3(value[1])
                    rotate_y = str_round3(value[2])
                elif len(value) % 3 == 0:           # for multiple rotations
                    svg_str += ' transform="'
                    for j in range(len(value)//3):
                        angle = str_round3(value[3*j])
                        rotate_x = str_round3(value[3*j+1])
                        rotate_y = str_round3(value[3*j+2])
                        if angle not in ('-360', '0', '360'):
                            svg_str += 'rotate(%s,%s,%s)'%(angle, rotate_x, rotate_y)
                    svg_str += '"'
                    continue
                else:
                    raise Exception('Rotate tuple length error!')
            else:
                raise Exception('Rotate arguments type error!')
            if angle not in ('-360', '0', '360'):
                svg_str += ' transform="rotate(%s,%s,%s)"'%(angle, rotate_x, rotate_y)
        else:
            svg_str += ' %s="%s"'%(key.replace('_', '-'), str_round3(value))
    svg_str += '/>'
    return svg_str

def head(width, height, viewBoxWidth, viewBoxHeight):
    head_str = """<!DOCTYPE svg PUBLIC "-//W3C//DTD SVG 20010904//EN" "http://www.w3.org/TR/2001/REC-SVG-20010904/DTD/svg10.dtd">
<svg version="1.0" xmlns="http://www.w3.org/2000/svg" width="%dpx" height="%dpx" viewBox="0 0 %d %d" preserveAspectRatio="xMidYMid meet">
<metadata> Created by Rubik Image Generator, written by Li Xiao-Tian. </metadata>
"""
    return head_str%(width, height, viewBoxWidth, viewBoxHeight)

TAIL = '\n</svg>'