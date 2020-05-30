import os
import argparse

def main():

    parser = argparse.ArgumentParser(description="convert folder indices if needed")

    parser.add_argument('--folder', type=str, help="folder with HD images", required=True)
    parser.add_argument('--output', type=str, help="output folder", required=True)
    parser.add_argument('--filter', type=str, help="filter to apply to keep scenes names from folder", required=True)

    args = parser.parse_args()

    p_folder = args.folder
    p_output = args.output
    p_filter = args.filter

    scenes = sorted([ s for s in  os.listdir(p_folder) if p_filter in s ] )

    # writing scene into file
    f = open(p_output, 'w')

    for s in scenes:
        f.write(s + '\n')

    f.close()


if __name__ == "__main__":
    main()