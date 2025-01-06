from PIL import Image, ImageEnhance, ImageFilter
import os

path = 'Image'
output = 'edited photos'

user_input = input("""
============================================
           Choose Your Desired Style
============================================
| (1) Vibrant and Bold                     |
| (2) Soft and Pastel                      |
| (3) Dark and Moody                       |
| (4) Vintage/Retro                        |
============================================
""")

for filename in os.listdir(path):
    if filename.endswith(('.png', '.jpg', '.jpeg')):

        img = Image.open(f"{path}/{filename}")

        if user_input == '1':
            brightness_enhancer = ImageEnhance.Brightness(img)
            img_bright = brightness_enhancer.enhance(30)

            contrast_enhancer = ImageEnhance.Contrast(img)
            img_contrast = contrast_enhancer.enhance(40)

            saturation_enhancer = ImageEnhance.Color(img)
            img_saturation = saturation_enhancer.enhance(50)

            sharpness_enhancer = ImageEnhance.Sharpness(img)
            img_sharpness = sharpness_enhancer.enhance(1)

            img_sharpness.show()

            clean_name = os.path.splitext(filename)[0]
            img_sharpness.save(f"{output}/{clean_name}_vibrant_bold.png")

        elif user_input == '2':
            brightness_enhancer = ImageEnhance.Brightness(img)
            img_bright = brightness_enhancer.enhance(1.15)

            contrast_enhancer = ImageEnhance.Contrast(img)
            img_cont = contrast_enhancer.enhance(0.95)

            saturation_enhancer = ImageEnhance.Color(img)
            img_saturation = saturation_enhancer.enhance(0.9)

            img_bright.show()

            clean_name = os.path.splitext(filename)[0]
            img_bright.save(f"{output}/{clean_name}_soft_pastel.png")

        elif user_input == '3':
            img = img.convert('L')

            brightness_enhancer = ImageEnhance.Brightness(img)
            img_bright = brightness_enhancer.enhance(0.6)

            contrast_enhancer = ImageEnhance.Contrast(img_bright)
            img_cont = contrast_enhancer.enhance(1.3)

            img_cont.show()

            clean_name = os.path.splitext(filename)[0]
            img_cont.save(f"{output}/{clean_name}_dark_gloomy_bw.png")

        elif user_input == '4':
            brightness_enhancer = ImageEnhance.Brightness(img)
            img_bright = brightness_enhancer.enhance(1.1)

            contrast_enhancer = ImageEnhance.Contrast(img)
            img_cont = contrast_enhancer.enhance(1.15)

            saturation_enhancer = ImageEnhance.Color(img)
            img_saturation = saturation_enhancer.enhance(1.2)

            img_cont.show()

            clean_name = os.path.splitext(filename)[0]
            img_cont.save(f"{output}/{clean_name}_vintage_retro.png")
