from PIL import Image, ImageDraw

array = [
    ['K','P','T','P','K'],
    ['K','P','K','P','K'],
    ['K','P','K','P','K'],
    ['K','P','K','P','K'],
    ['K','P','T','P','K'],
]
color_dict = {
    "K": (234,51,41),
    "P": (101, 203, 91),
    "T": (255, 255, 146),
    "M": (137, 238, 240),
    "FR": (56, 127, 75),
    "FL": (234, 51, 185),
    "BR": (115, 20, 144),
    "XRp": (251, 231, 78),
    "XRm": (242, 168, 60),
    "XLp": (73, 162, 248),
    "XLm": (50, 115, 213),
    "BL": (179, 179, 179),
    "S": (109,62,61),
}

width = 5
height = 5

image = Image.new('RGB', (width,height), color='white')
draw = ImageDraw.Draw(image)
for x, row in enumerate(array):
    for y, value in enumerate(row):
        #print(x, y, value)
        draw.point((y, x), color_dict.get(value))
        print(x,y)

image.save('000.png')