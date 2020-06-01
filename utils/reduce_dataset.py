import os
import argparse

import shutil


def main():
    
    parser = argparse.ArgumentParser(description="Reduced data to keep for SIN3D app")

    parser.add_argument('--folder', type=str, help='folder with all scenes', required=True)
    parser.add_argument('--output', type=str, help='output folder with all reduced dataset', required=True)
    parser.add_argument('--step', type=int, help='step to keep', required=True)
    parser.add_argument('--start_at', type=int, help='start step at specific index', default=0)
    parser.add_argument('--scenes', type=str, help='file which contains line by line scenes names to keep', default='')

    args = parser.parse_args()

    p_folder = args.folder
    p_output = args.output
    p_step   = args.step 
    p_start_at = args.start_at
    p_scenes_f = args.scenes

    if not os.path.exists(p_output):
        os.makedirs(p_output)

    scenes = sorted(os.listdir(p_folder))

    # only keep specific scenes using file
    if len(p_scenes_f) > 1:
        with open(p_scenes_f, 'r') as f:
            scenes = [ s.replace('\n', '') for s in f.readlines() ]

    scenes_path = [ os.path.join(p_folder, p) for p in scenes ]

    for id_scene, scene in enumerate(scenes):

        print('Start loading and reduce number of images for {0}'.format(scene))
        
        # get folder scene path
        scene_path = scenes_path[id_scene]

        # create output scene path
        output_scene_path = os.path.join(p_output, scene)

        if not os.path.exists(output_scene_path):
            os.makedirs(output_scene_path)

        # get image and image path
        images_names = sorted(os.listdir(scene_path))
        images_path = [ os.path.join(scene_path, img_path) for img_path in images_names ]

        for id, img in enumerate(images_names):

            img_path = images_path[id]

            image_index = int(img.split('_')[-1].split('.')[0])

            # check modulo step to check if needed to keep image or not
            if image_index % p_step == 0 or image_index <= p_start_at:

                # we can keep image and save it in to expected folder
                shutil.copy2(img_path, os.path.join(output_scene_path, img))


if __name__ == "__main__":
    main()
