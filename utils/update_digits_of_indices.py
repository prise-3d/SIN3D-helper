# main import
import os
import argparse
import shutil

# parameters
scene_image_quality_separator     = '_'
scene_image_extension             = '.png'

def get_scene_image_quality(img_path):

    # if path getting last element (image name) and extract quality
    img_postfix = img_path.split('/')[-1].split(scene_image_quality_separator)[-1]
    img_quality = img_postfix.replace(scene_image_extension, '')

    return int(img_quality)

def update_digits_folder_images(p_folder, scenes, output, digits):
    
    for scene in scenes:

        scene_p = os.path.join(p_folder, scene)
        output_folder_path = os.path.join(output, scene)

        images = sorted(os.listdir(scene_p))

        if not os.path.exists(output_folder_path):
            os.makedirs(output_folder_path)

        print('Update images indices indices for %s' % scene_p)

        for img in images:
            img_path = os.path.join(scene_p, img)
            current_quality = get_scene_image_quality(img_path)

            img_prefix_split = img_path.split('/')[-1].split(scene_image_quality_separator)
            del img_prefix_split[-1]

            img_prefix = "_".join(img_prefix_split)

            index_str = str(current_quality)

            while len(index_str) < digits:
                index_str = "0" + index_str

            img_output_name = img_prefix + '_' + index_str + '.png'
            img_output_path = os.path.join(output_folder_path, img_output_name)

            shutil.copy2(img_path, img_output_path)

        
def main():

    parser = argparse.ArgumentParser(description="convert folder indices of scenes if needed and save into new folder")

    parser.add_argument('--folder', type=str, help="folder with HD images", required=True)
    parser.add_argument('--output', type=str, help="output folder", required=True)
    parser.add_argument('--digits', type=int, help="max expected index", required=True)

    args = parser.parse_args()

    p_folder = args.folder
    p_output = args.output
    p_digits = args.digits

    scenes = sorted(os.listdir(p_folder))

    update_digits_folder_images(p_folder, scenes, p_output, p_digits)

if __name__ == "__main__":
    main()