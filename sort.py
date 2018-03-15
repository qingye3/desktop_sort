#!/bin/python
import desktop_sort.util
import argparse


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Automatic sorting of desktop files.')
    parser.add_argument('--config-file', metavar='config.yaml', dest='config', type=str, help='an integer for the accumulator', required=True)
    args = parser.parse_args()

    desktop_sort.util.sort_files(args.config)