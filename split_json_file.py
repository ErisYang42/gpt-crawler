# split json file to multiple files(limit the file size)


import json
import os
import argparse
import logging
import shutil

logging.basicConfig(level=logging.DEBUG,
                    format='%(asctime)s - %(levelname)s - %(message)s')

default_size = 6 * 1024 * 1024


def split_json(json_file, output_dir, limit_size):
    logging.info("split json file: %s to %s, limit size: %d",
                 json_file, output_dir, limit_size)
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)
    if not os.path.exists(json_file):
        logging.error("json file not exists")
        return
    if not os.path.isfile(json_file):
        logging.error("json file is not a file")
        return
    if not os.path.isdir(output_dir):
        logging.error("output dir is not a dir")
        return
    if limit_size <= 0:
        logging.error("limit size is not valid")
        return
    file_size = os.path.getsize(json_file)
    logging.info("file size: %d", file_size)
    if file_size <= limit_size:
        shutil.copy(json_file, output_dir)
        return
    # get the name of json file, remove the dir and extension
    input_base_name = os.path.basename(json_file).split('.')[0]
    logging.info("file name: %s", input_base_name)
    with open(json_file, 'r', encoding='utf-8') as file:
        data = json.load(file)

    current_size = 0
    current_data = []
    part = 1

    for item in data:
        item_size = len(json.dumps(item))

        if current_size + item_size > limit_size:
            file_name = f'{output_dir}/{input_base_name}_{part}.json'
            logging.info("current size: %d, file name: %s",
                         current_size, file_name)
            with open(file_name, 'w', encoding='utf-8') as outfile:
                json.dump(current_data, outfile)
            part += 1
            current_data = [item]
            current_size = item_size
        else:
            current_data.append(item)
            current_size += item_size
    # Save any remaining data
    if current_data != []:
        file_name = f'{output_dir}/{input_base_name}_{part}.json'
        logging.info("current size: %d, file name: %s",
                     current_size, file_name)
        with open(file_name, 'w', encoding='utf-8') as outfile:
            json.dump(current_data, outfile)


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('-i', '--input', help='input json file')
    parser.add_argument('-o', '--output', help='output dir')
    parser.set_defaults(size=default_size)
    parser.add_argument(
        '-s', '--size', help='limit size of each file, default is 5M')
    args = parser.parse_args()
    if args.input is None or args.output is None or args.size is None:
        parser.print_help()
        return
    split_json(args.input, args.output, int(args.size))


if __name__ == '__main__':
    main()
