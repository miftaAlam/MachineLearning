def pixels_of_num(remaining):
    limit = 64
    at = 0
    pixels = [[0,0,0]]*64
    while remaining > 0:
        if (remaining > limit):
            pixels[at] = [255,0,0]
            at = at + 1
            limit = limit -1
            remaining = remaining - limit
        else:
            pixels[at] = [255,255,255]
            remaining = remaining -1
            at = at + 1
    return pixels


o = [0,0,0]
w = [250,250,250]
g = [0,100,0]
r = [100,0,0]
b = [0,0,100]
s = [80,80,80]

def question_mark(c):
    return [
        o,w,o,o,o,o,w,o,
        w,w,w,w,w,w,w,w,
        o,w,c,c,c,c,w,o,
        o,o,o,o,o,c,o,o,
        o,o,o,o,c,o,o,o,
        o,o,o,o,c,o,o,o,
        o,o,o,o,o,o,o,o,
        o,o,o,o,c,o,o,o
        ]

def unknown(c):
    return [
        o,o,o,o,o,o,o,o,
        o,o,o,o,o,o,o,o,
        o,o,c,c,c,c,o,o,
        o,o,o,o,o,c,o,o,
        o,o,o,o,c,o,o,o,
        o,o,o,o,c,o,o,o,
        o,o,o,o,o,o,o,o,
        o,o,o,o,c,o,o,o
        ]

def cee(c):
    return [
        o,w,o,o,o,o,w,o,
        w,w,w,w,w,w,w,w,
        o,w,c,c,c,c,w,o,
        o,c,o,o,o,o,o,o,
        o,c,o,o,o,o,o,o,
        o,c,o,o,o,o,o,o,
        o,c,o,o,o,o,o,o,
        o,o,c,c,c,c,o,o
        ]

def ex(c):
    return [
        o,w,o,o,o,o,w,o,
        w,w,w,w,w,w,w,w,
        o,w,o,o,o,o,w,o,
        o,o,c,o,o,c,o,o,
        o,o,o,c,c,o,o,o,
        o,o,o,c,c,o,o,o,
        o,o,c,o,o,c,o,o,
        o,c,o,o,o,o,c,o
        ]

def blocked(c):
    return [
        o,w,o,o,o,o,w,o,
        w,w,w,w,w,w,w,w,
        o,w,c,c,c,c,w,o,
        o,c,o,o,o,c,c,o,
        c,o,o,o,c,o,o,c,
        c,o,o,c,o,o,c,c,
        o,c,c,o,o,o,c,o,
        o,o,c,c,c,c,o,o
        ]

def demo(c):
    return [
        o,w,o,o,o,o,w,o,
        w,w,w,w,w,w,w,w,
        o,w,c,c,c,c,w,o,
        o,o,c,o,o,o,o,o,
        o,o,c,c,c,c,o,o,
        o,o,o,o,o,c,o,o,
        o,o,o,o,o,c,o,o,
        o,o,c,c,c,c,o,o
        ]

def image_net(c):
    return [
        o,w,o,o,o,o,w,o,
        w,w,w,w,w,w,w,w,
        o,w,c,c,c,c,w,o,
        o,c,o,o,o,o,c,o,
        c,o,o,c,c,o,o,c,
        c,o,o,c,c,o,o,c,
        o,c,o,o,o,o,c,o,
        o,c,c,c,c,c,c,o
        ]

def pen(c):
    return [
        o,o,o,o,o,o,c,o,
        o,o,o,o,o,c,c,c,
        o,o,o,o,c,c,c,o,
        o,o,o,c,c,c,o,o,
        o,o,c,c,c,o,o,o,
        o,c,c,c,o,o,o,o,
        c,c,c,o,o,o,o,o,
        c,c,o,o,o,o,o,o
        ]

def bag(c):
    return [
        o,o,o,o,o,o,o,o,
        o,o,o,c,c,o,o,o,
        o,o,c,o,o,c,o,o,
        o,o,c,o,o,c,o,o,
        o,c,c,c,c,c,c,o,
        o,c,c,c,c,c,c,o,
        o,o,c,c,c,c,o,o,
        o,o,o,o,o,o,o,o
        ]

def bottle(c):
    return [
        o,o,o,c,o,o,o,o,
        o,o,c,c,c,o,o,o,
        o,o,c,o,c,o,o,o,
        o,o,c,o,c,o,o,o,
        o,o,c,c,c,o,o,o,
        o,o,c,o,c,o,o,o,
        o,o,c,o,c,o,o,o,
        o,o,c,c,c,o,o,o
        ]

def hand(c):
    return [
        o,o,o,o,o,o,o,o,
        o,o,o,c,o,o,o,o,
        o,o,o,c,o,o,o,o,
        o,o,o,c,c,c,o,o,
        o,c,o,c,c,c,c,o,
        o,o,c,c,c,c,c,o,
        o,o,o,c,c,c,o,o,
        o,o,o,o,o,o,o,o
        ]

def phone(c):
    return [
        o,o,o,o,o,o,o,o,
        o,o,c,o,o,o,o,o,
        o,c,c,c,o,o,o,o,
        o,c,c,o,o,o,o,o,
        o,o,c,c,o,c,o,o,
        o,o,o,c,c,c,c,o,
        o,o,o,o,c,c,o,o,
        o,o,o,o,o,o,o,o
        ]

def stream(c):
    return [
        o,w,o,o,o,o,w,o,
        w,w,w,w,w,w,w,w,
        o,w,o,o,c,o,w,o,
        c,c,c,o,o,c,o,o,
        o,o,o,c,o,o,c,o,
        c,c,o,o,c,o,c,o,
        o,o,c,o,c,o,c,o,
        c,o,c,o,c,o,c,o
        ]


def boat(c):
    return [
        o,w,o,c,o,o,w,o,
        w,w,w,w,w,w,w,w,
        o,w,o,c,c,c,w,o,
        o,o,o,c,c,c,c,o,
        o,o,o,c,c,c,c,c,
        c,c,c,c,c,c,c,c,
        o,c,c,c,c,c,c,o,
        o,o,c,c,c,c,o,o
        ]

def boat_act(c):
    return [
        o,o,o,c,o,o,o,o,
        o,o,o,c,c,o,o,o,
        o,o,o,c,c,c,o,o,
        o,o,o,c,c,c,c,o,
        o,o,o,c,c,c,c,c,
        c,c,c,c,c,c,c,c,
        o,c,c,c,c,c,c,o,
        o,o,c,c,c,c,o,o
        ]

