# Image Editor

A Python-based image editor that applies various visual effects to images in bulk using the `Pillow` library. It allows users to transform images with different styles such as vibrant and bold, soft and pastel, dark and moody (black and white), and vintage/retro.

## Features

- **Batch image processing:** Select and process multiple images from a folder.
- **Vibrant and Bold:** Enhance brightness, contrast, saturation, and sharpness.
- **Soft and Pastel:** Apply subtle changes to brightness, contrast, and saturation.
- **Dark and Moody (Black & White):** Convert images to grayscale, decrease brightness, and increase contrast for a dark, somber feel.
- **Vintage/Retro:** Apply a vintage look by adjusting brightness, contrast, and saturation.

## Requirements

- Python 3.x
- Pillow library

To install the required libraries, run:

pip install pillow

##Choose the style you want to apply:

-(1) Vibrant and Bold
-(2) Soft and Pastel
-(3) Dark and Moody
-(4) Vintage/Retro
-The edited images will be saved in the edited photos folder.


##Directory Structure

Copy code
/project
  /Image           # Input folder with images
  /edited photos   # Output folder where edited images are saved
  image_editor.py  # Python script to run the image editor
