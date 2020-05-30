# Steps to follow in order to prepare SIN3D images data

## Download and prepare projet

```sh
git clone --recursive https://github.com/prise-3d/sin3d-helper
```

Prepare the `rawls-tools` submodule:

```sh
cd rawls-tools
mkdir build && cd build
cmake ..
make -j
```

## Reconstruction of .rawls files

```sh
cd rawls-tools
bash run/reconstruct_png_all.sh {rawls_folder} {output_png} {step}
```

**Note:** this script also do convertion if .rawls has incremention of 1

## Fix images indices

If max indices is not as expected while reconstructed images, that means you do not generate 1 to 10000 by step one images but 1 to 500 by step 1 (with 20 samples per images).

In order to fix that, you can multiply by factor indices

```sh
python utils/check_indices.py --folder {png_folder} --output {expected_output_folder} --expected {max_expected_index_of_image}
```

## Extract center of images

```sh
bash utils/convert_folder_center.sh {input_png_folder} {output_folder} {width} {height}
```

## Reduce dataset images

```sh 
python utils/extract_scenes_folder.py --folder {input_png_folder} --output {filename} --filter {your_filter}
```

```sh
bash utils/reduce_dataset.py --folder {input_png_folder} --output {output_folder} --step {step_of_indices_kept} --start_at {start_step_at} --scenes {scenes_filename_filtered}
```
