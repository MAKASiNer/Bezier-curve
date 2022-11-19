from PIL import Image
from PIL.ImageDraw import ImageDraw
from random import randint
from scipy.special import binom


SIZE = (512, 512)
COUNT = 30
RESULT = 'out.png'
RESOLUTION = COUNT * 10


def T(resolution):
    return [0, *map(lambda x: (x+1.0)/resolution, range(resolution))]


def rand_P(count, limits):
    return [(randint(0, limits[0] - 1), randint(0, limits[1] - 1)) for _ in range(count)]


img = Image.new('RGBA', SIZE, '#fff')
draw = ImageDraw(img)

P = rand_P(COUNT, limits=SIZE)

pts = []
for t in T(RESOLUTION):
    x, y = 0, 0
    for i, p in enumerate(P):
        c = binom(len(P) - 1, i)
        k1, k2 = i, len(P) - i - 1
        x += c * p[0] * t**k1 * (1.0 - t)**k2
        y += c * p[1] * t**k1 * (1.0 - t)**k2
    pts.append((x, y))

draw.line(P, '#000', width=1)
draw.line(pts, '#00f', width=2)

for p in P:
    draw.ellipse(
        (p[0] - 1.5, p[1] - 1.5,
         p[0] + 1.5, p[1] + 1.5),
        '#f00'
    )

img.save(RESULT)
