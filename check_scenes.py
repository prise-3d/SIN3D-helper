import os
import argparse
import shutil


parser = argparse.ArgumentParser(description="Reduce dataset based on modulo indices values")

parser.add_argument('--folder', type=str, help="folder with HD images", required=True)
parser.add_argument('--output', type=str, help="output folder", required=True)
parser.add_argument('--modulo', type=int, help="modulo expected index", required=True)

args = parser.parse_args()

p_folder = args.folder
p_output = args.output
p_modulo = args.modulo

scenes = os.listdir(p_folder)


print(scenes)

if not os.path.exists(p_output):
   os.makedirs(p_output)

for scene in scenes:
    scene_folder = os.path.join(p_folder, scene)
    images = sorted(os.listdir(scene_folder))
    images = [ img for img in images ]
    
    output_scene_folder = os.path.join(p_output, scene)

    if not os.path.exists(output_scene_folder):
       os.makedirs(output_scene_folder)

    for img in images: 
        quality = int(img.split('_')[-1].replace('.png', '')) 
        img_path = os.path.join(scene_folder, img) 
        
        if quality % p_modulo == 0:
            output_img_path = os.path.join(output_scene_folder, img)
            shutil.copy2(img_path, output_img_path)
            print('Copy from `' + img_path + '` into `' + output_img_path + '`')
            
