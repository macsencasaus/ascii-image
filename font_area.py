from PIL import Image, ImageDraw, ImageFont
import numpy as np

width, height = 20, 20
grayscale_array = np.zeros((height, width), dtype=np.uint8)  # Initialize with zeros


typeable_character = [chr(i) for i in range(32,127)]
font_size = 29

position = (width // 2 -8, height // 2 - 12)

font_path = ".\\font\\Consolas.ttf"  
font = ImageFont.truetype(font_path, font_size)

mean_brightness_dict = {}

for character in typeable_character:
    grayscale_image = Image.fromarray(grayscale_array, mode='L')
    draw = ImageDraw.Draw(grayscale_image)
    draw.text(position, character, fill=255, font=font)
    brightness = (np.array(grayscale_image)/255).mean()
    mean_brightness_dict[round(brightness/.371,3)] = character

last = 0.001

keys = list(mean_brightness_dict.keys())
keys.sort()

for i in keys:
    for j in np.arange(last, i, .001):
        mean_brightness_dict[round(j,3)] = mean_brightness_dict[i]
    last = i + .001

mean_brightness_dict[0.0] = ' '

if __name__ == '__main__':
    print(mean_brightness_dict)