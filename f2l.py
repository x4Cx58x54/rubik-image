"""
    Generates F2L images.  

    @author Li Xiao-Tian
"""

import svg
import utils_geometry_colour as gc


FACES_AND_CUTS = {
    'u': ((0,0,0), (0,3,0), (3,3,0), (3,0,0), (0,0,0)),
    'f': ((0,0,0), (0,0,3), (3,0,3), (3,0,0), (0,0,0)),
    'r': ((0,0,0), (0,3,0), (0,3,3), (0,0,3), (0,0,0)),
    'lm': ((2,0,3), (2,0,0), (2,3,0)),
    'mr': ((1,0,3), (1,0,0), (1,3,0)),
    'fs': ((0,1,3), (0,1,0), (3,1,0)),
    'sb': ((0,2,3), (0,2,0), (3,2,0)),
    'ue': ((3,0,1), (0,0,1), (0,3,1)),
    'ed': ((3,0,2), (0,0,2), (0,3,2)),
}

PATCHES = {
    'f1': ((3,0,0), (2,0,0), (2,0,1), (3,0,1), (3,0,0)),
    'f2': ((2,0,0), (1,0,0), (1,0,1), (2,0,1), (2,0,0)),
    'f3': ((1,0,0), (0,0,0), (0,0,1), (1,0,1), (1,0,0)),
    'f4': ((3,0,1), (2,0,1), (2,0,2), (3,0,2), (3,0,1)),
    'f5': ((2,0,1), (1,0,1), (1,0,2), (2,0,2), (2,0,1)),
    'f6': ((1,0,1), (0,0,1), (0,0,2), (1,0,2), (1,0,1)),
    'f7': ((3,0,2), (2,0,2), (2,0,3), (3,0,3), (3,0,2)),
    'f8': ((2,0,2), (1,0,2), (1,0,3), (2,0,3), (2,0,2)),
    'f9': ((1,0,2), (0,0,2), (0,0,3), (1,0,3), (1,0,2)),
    'u1': ((3,3,0), (2,3,0), (2,2,0), (3,2,0), (3,3,0)),
    'u2': ((2,3,0), (1,3,0), (1,2,0), (2,2,0), (2,3,0)),
    'u3': ((1,3,0), (0,3,0), (0,2,0), (1,2,0), (1,3,0)),
    'u4': ((3,2,0), (2,2,0), (2,1,0), (3,1,0), (3,2,0)),
    'u5': ((2,2,0), (1,2,0), (1,1,0), (2,1,0), (2,2,0)),
    'u6': ((1,2,0), (0,2,0), (0,1,0), (1,1,0), (1,2,0)),
    'u7': ((3,1,0), (2,1,0), (2,0,0), (3,0,0), (3,1,0)),
    'u8': ((2,1,0), (1,1,0), (1,0,0), (2,0,0), (2,1,0)),
    'u9': ((1,1,0), (0,1,0), (0,0,0), (1,0,0), (1,1,0)),
    'r1': ((0,0,0), (0,1,0), (0,1,1), (0,0,1), (0,0,0)),
    'r2': ((0,1,0), (0,2,0), (0,2,1), (0,1,1), (0,1,0)),
    'r3': ((0,2,0), (0,3,0), (0,3,1), (0,2,1), (0,2,0)),
    'r4': ((0,0,1), (0,1,1), (0,1,2), (0,0,2), (0,0,1)),
    'r5': ((0,1,1), (0,2,1), (0,2,2), (0,1,2), (0,1,1)),
    'r6': ((0,2,1), (0,3,1), (0,3,2), (0,2,2), (0,2,1)),
    'r7': ((0,0,2), (0,1,2), (0,1,3), (0,0,3), (0,0,2)),
    'r8': ((0,1,2), (0,2,2), (0,2,3), (0,1,3), (0,1,2)),
    'r9': ((0,2,2), (0,3,2), (0,3,3), (0,2,3), (0,2,2)),
}


c = gc.ColourScheme()

BASESTATES = {
    'u' : {             # All gray
            'u1': 'u', 'u2': 'u', 'u3': 'u',
            'u4': 'u', 'u5': 'u', 'u6': 'u',
            'u7': 'u', 'u8': 'u', 'u9': 'u',

            'f1': 'u', 'f2': 'u', 'f3': 'u',
            'f4': 'u', 'f5': 'u', 'f6': 'u',
            'f7': 'u', 'f8': 'u', 'f9': 'u',

            'r1': 'u', 'r2': 'u', 'r3': 'u', 
            'r4': 'u', 'r5': 'u', 'r6': 'u',
            'r7': 'u', 'r8': 'u', 'r9': 'u',
    },
    
    'w' : {             # All white
            'u1': 'w', 'u2': 'w', 'u3': 'w',
            'u4': 'w', 'u5': 'w', 'u6': 'w',
            'u7': 'w', 'u8': 'w', 'u9': 'w',

            'f1': 'w', 'f2': 'w', 'f3': 'w',
            'f4': 'w', 'f5': 'w', 'f6': 'w',
            'f7': 'w', 'f8': 'w', 'f9': 'w',
            
            'r1': 'w', 'r2': 'w', 'r3': 'w', 
            'r4': 'w', 'r5': 'w', 'r6': 'w',
            'r7': 'w', 'r8': 'w', 'r9': 'w',
    },

    'cross' : {         # Cross solved
            'u1': 'u', 'u2': 'u', 'u3': 'u',
            'u4': 'u', 'u5': 'u', 'u6': 'u',
            'u7': 'u', 'u8': 'u', 'u9': 'u',

            'f1': 'u', 'f2': 'u', 'f3': 'u',
            'f4': 'u', 'f5': c.f, 'f6': 'u',
            'f7': 'u', 'f8': c.f, 'f9': 'u',

            'r1': 'u', 'r2': 'u', 'r3': 'u', 
            'r4': 'u', 'r5': c.r, 'r6': 'u',
            'r7': 'u', 'r8': c.r, 'r9': 'u',
    },
    
    'f2l' : {           # F2l solved
            'u1': 'u', 'u2': 'u', 'u3': 'u',
            'u4': 'u', 'u5': 'u', 'u6': 'u',
            'u7': 'u', 'u8': 'u', 'u9': 'u',

            'f1': 'u', 'f2': 'u', 'f3': 'u',
            'f4': c.f, 'f5': c.f, 'f6': c.f,
            'f7': c.f, 'f8': c.f, 'f9': c.f,

            'r1': 'u', 'r2': 'u', 'r3': 'u', 
            'r4': c.r, 'r5': c.r, 'r6': c.r,
            'r7': c.r, 'r8': c.r, 'r9': c.r,
    },
    
    'oll' : {           # F2l and OLL solved
            'u1': c.u, 'u2': c.u, 'u3': c.u,
            'u4': c.u, 'u5': c.u, 'u6': c.u,
            'u7': c.u, 'u8': c.u, 'u9': c.u,

            'f1': 'u', 'f2': 'u', 'f3': 'u',
            'f4': c.f, 'f5': c.f, 'f6': c.f,
            'f7': c.f, 'f8': c.f, 'f9': c.f,

            'r1': 'u', 'r2': 'u', 'r3': 'u', 
            'r4': c.r, 'r5': c.r, 'r6': c.r,
            'r7': c.r, 'r8': c.r, 'r9': c.r,
    },
    
    'slot' : {          # F2l except FR slot solved
            'u1': 'u', 'u2': 'u', 'u3': 'u',
            'u4': 'u', 'u5': 'u', 'u6': 'u',
            'u7': 'u', 'u8': 'u', 'u9': 'u',

            'f1': 'u', 'f2': 'u', 'f3': 'u',
            'f4': c.f, 'f5': c.f, 'f6': 'u',
            'f7': c.f, 'f8': c.f, 'f9': 'u',

            'r1': 'u', 'r2': 'u', 'r3': 'u', 
            'r4': 'u', 'r5': c.r, 'r6': c.r,
            'r7': 'u', 'r8': c.r, 'r9': c.r,
    },
    
    'complete' : {
            'u1': c.u, 'u2': c.u, 'u3': c.u,
            'u4': c.u, 'u5': c.u, 'u6': c.u,
            'u7': c.u, 'u8': c.u, 'u9': c.u,

            'f1': c.f, 'f2': c.f, 'f3': c.f,
            'f4': c.f, 'f5': c.f, 'f6': c.f,
            'f7': c.f, 'f8': c.f, 'f9': c.f,

            'r1': c.r, 'r2': c.r, 'r3': c.r, 
            'r4': c.r, 'r5': c.r, 'r6': c.r,
            'r7': c.r, 'r8': c.r, 'r9': c.r,
    },
}

F2L_STD_CODES = (                                           # based on 'slot'
    {},                                                     # 00
    {'f6':c.r, 'r4':c.f, 'f9':c.f, 'r7':c.r, },             # 01
    {'u8':c.r, 'f2':c.f, 'f9':c.f, 'r7':c.r, },             # 02
    {'u6':c.f, 'r2':c.r, 'f9':c.f, 'r7':c.r, },             # 03
    {'f6':c.f, 'r4':c.r, 'f9':c.d, 'r7':c.f, },             # 04
    {'f6':c.r, 'r4':c.f, 'f9':c.d, 'r7':c.f, },             # 05
    {'u8':c.r, 'f2':c.f, 'f9':c.d, 'r7':c.f, },             # 06
    {'u6':c.f, 'r2':c.r, 'f9':c.d, 'r7':c.f, },             # 07
    {'f6':c.f, 'r4':c.r, 'f9':c.r, 'r7':c.d, },             # 08
    {'f6':c.r, 'r4':c.f, 'f9':c.r, 'r7':c.d, },             # 09
    {'u8':c.r, 'f2':c.f, 'f9':c.r, 'r7':c.d, },             # 10
    {'u6':c.f, 'r2':c.r, 'f9':c.r, 'r7':c.d, },             # 11
    {'u9':c.d, 'f3':c.r, 'r1':c.f, 'f6':c.f, 'r4':c.r, },   # 12
    {'u9':c.d, 'f3':c.r, 'r1':c.f, 'f6':c.r, 'r4':c.f, },   # 13
    {'u8':c.r, 'u9':c.d, 'f2':c.f, 'f3':c.r, 'r1':c.f, },   # 14
    {'u4':c.r, 'u9':c.d, 'f3':c.r, 'r1':c.f, },             # 15
    {'u2':c.r, 'u9':c.d, 'f3':c.r, 'r1':c.f, },             # 16
    {'u6':c.r, 'u9':c.d, 'f3':c.r, 'r1':c.f, 'r2':c.f, },   # 17
    {'u8':c.f, 'u9':c.d, 'f2':c.r, 'f3':c.r, 'r1':c.f, },   # 18
    {'u4':c.f, 'u9':c.d, 'f3':c.r, 'r1':c.f, },             # 19
    {'u2':c.f, 'u9':c.d, 'f3':c.r, 'r1':c.f, },             # 20
    {'u6':c.f, 'u9':c.d, 'f3':c.r, 'r1':c.f, 'r2':c.r, },   # 21
    {'u9':c.f, 'f3':c.d, 'r1':c.r, 'f6':c.f, 'r4':c.r, },   # 22
    {'u9':c.f, 'f3':c.d, 'r1':c.r, 'f6':c.r, 'r4':c.f, },   # 23
    {'u8':c.r, 'u9':c.f, 'f2':c.f, 'f3':c.d, 'r1':c.r, },   # 24
    {'u4':c.r, 'u9':c.f, 'f3':c.d, 'r1':c.r, },             # 25
    {'u2':c.r, 'u9':c.f, 'f3':c.d, 'r1':c.r, },             # 26
    {'u6':c.r, 'u9':c.f, 'f3':c.d, 'r1':c.r, 'r2':c.f, },   # 27
    {'u8':c.f, 'u9':c.f, 'f2':c.r, 'f3':c.d, 'r1':c.r, },   # 28
    {'u4':c.f, 'u9':c.f, 'f3':c.d, 'r1':c.r, },             # 29
    {'u2':c.f, 'u9':c.f, 'f3':c.d, 'r1':c.r, },             # 30
    {'u6':c.f, 'u9':c.f, 'f3':c.d, 'r1':c.r, 'r2':c.r, },   # 31
    {'u9':c.r, 'f3':c.f, 'r1':c.d, 'f6':c.f, 'r4':c.r, },   # 32
    {'u9':c.r, 'f3':c.f, 'r1':c.d, 'f6':c.r, 'r4':c.f, },   # 33
    {'u8':c.r, 'u9':c.r, 'f2':c.f, 'f3':c.f, 'r1':c.d, },   # 34
    {'u4':c.r, 'u9':c.r, 'f3':c.f, 'r1':c.d, },             # 35
    {'u2':c.r, 'u9':c.r, 'f3':c.f, 'r1':c.d, },             # 36
    {'u6':c.r, 'u9':c.r, 'f3':c.f, 'r1':c.d, 'r2':c.f, },   # 37
    {'u8':c.f, 'u9':c.r, 'f2':c.r, 'f3':c.f, 'r1':c.d, },   # 38
    {'u4':c.f, 'u9':c.r, 'f3':c.f, 'r1':c.d, },             # 39
    {'u2':c.f, 'u9':c.r, 'f3':c.f, 'r1':c.d, },             # 40
    {'u6':c.f, 'u9':c.r, 'f3':c.f, 'r1':c.d, 'r2':c.r, },   # 41
)

X3 = gc.Point2d(15, 63)
Y3 = gc.Point2d(240, 27)
Z3 = gc.Point2d(179, 249)
ORIGIN = gc.Point2d(179, 84)


def get_coord(p):
    '''
        Projection from 3d coord to 2d coord in SVG.
    '''
    x = p[0]
    y = p[1]
    z = p[2]
    ex = gc.Point2d((X3.x-ORIGIN.x)/3, (X3.y-ORIGIN.y)/3)
    ey = gc.Point2d((Y3.x-ORIGIN.x)/3, (Y3.y-ORIGIN.y)/3)
    ez = gc.Point2d((Z3.x-ORIGIN.x)/3, (Z3.y-ORIGIN.y)/3)
    resx = ORIGIN.x + x*ex.x + y*ey.x + z*ez.x
    resy = ORIGIN.y + x*ex.y + y*ey.y + z*ez.y
    return gc.Point2d(resx, resy)

def grid_path():
    '''
        Generates the grid in F2L
    '''
    grid_str = ''
    for fc, fcpoints in FACES_AND_CUTS.items():
        pathd = ['M',]
        for p in fcpoints:
            coord = get_coord(p)
            pathd.append(coord.x)
            pathd.append(coord.y)
        grid_str += svg.element('path', id=fc, d=pathd, fill='none', stroke="#000000", stroke_width="2")
    return grid_str


def patch_path(patch, colour):
    pathd = ['M',]
    for point in PATCHES[patch]:
        coord = get_coord(point)
        pathd.append(coord.x)
        pathd.append(coord.y)
    pathd.append('z')
    return svg.element('path', id=patch, d=pathd, fill=gc.COLOURS[colour])


def f2l(x, basestate='slot', filename='f2l.svg'):
    '''
        Generates F2L SVG.

        x: F2L number, or a dict containing 'u1', 'u2', 'u3', ..., 'r9' items specifying the colours of each visible patch. For example {'f6':'r', 'f9':'b', 'r4':'b', 'r7':'r'} (if based on 'slot', =F2l 1).

        basestate: the default state of the cube, 'u' = all gray, 'w' = all white, 'cross' = cross solved, 'f2l' = F2L solved, 'oll' = OLL solved, 'complete' = all complete, default 'slot', F2L except RF slot solved.
    '''

    patches_str = ''
    if isinstance(x, int):
        if x > 41 or x < 0:
            raise Exception("F2L code is %d, not in [1, 41]."%x)
        patches = F2L_STD_CODES[x]
    elif isinstance(x, dict):
        patches = x
    else:
        raise Exception('Invalid F2L state code "%s".'%str(x))

    for patch in PATCHES.keys():
        if patch in patches:
            colour = patches[patch]
        else:
            colour = BASESTATES[basestate][patch]
        patches_str += patch_path(patch, colour)

    with open(filename, 'w') as f:
        f.write(svg.head(256, 256, 256, 256))
        f.write(svg.element('rect', id='bg', width="256", height="256", fill="#ffffff"))
        f.write(patches_str)
        f.write(grid_path())
        f.write(svg.TAIL)
