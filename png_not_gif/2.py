from PIL import Image
import numpy as np

# Создаем изображение с заданными параметрами
img = Image.new('P', (5, 1))

# Определяем палитру и приводим тип данных к uint8
palette = np.array([(0, 0, 255),    # синий
                    (255, 255, 0),  # желтый
                    (255, 165, 0),  # оранжевый
                    (0, 128, 0),    # зеленый
                    (255, 0, 0)], dtype=np.uint8)

# Присваиваем каждому пикселю соответствующий цвет из палитры
img.putpalette(palette)
for x in range(5):
    img.putpixel((x, 0), x)

# Сохраняем изображение в файл
img.save('indexed_colors.png')

img = Image.open('indexed_colors.png')
print(img.getcolors(maxcolors=img.size[0]*img.size[1]))
