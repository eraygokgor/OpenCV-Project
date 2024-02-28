import os
from src.BackgroudSubstraction import BackGroundSubtractor

# input folder in reference to base folder
input_folder = os.path.join("./", "data")
# output folder in reference to base folder
output_folder = os.path.join("./", "output")


input_video = os.path.join(input_folder, 'videoplayback.mp4')
background_obj = BackGroundSubtractor(input_video)
background_obj.substract_background()
