"""
    Geometry and colour info.  

    @author Li Xiao-Tian
"""


class Point2d():
    def __init__(self, x, y):
        self.x = x;
        self.y = y;

COLOURS = {
    'u': '#A9A9A9',
    'w': '#F9F9F9',
    'r': '#D8251A',
    'b': '#0194dd',
    'g': '#2EFE2E',
    'o': '#F0A226',
    'y': '#FFFF00',
}

class ColourScheme():
    '''
        Colour of each face of the cube.
    '''

    def __init__(self, d='w', u='y', f='b', r='r', b='g', l='o'):
        self.d = d
        self.u = u
        self.f = f
        self.r = r
        self.b = b
        self.l = l
        self.x = 'u'
    
    def config_colour(self, d, u, f, r, b, l):
        self.d = d
        self.u = u
        self.f = f
        self.r = r
        self.b = b
        self.l = l