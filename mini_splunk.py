"""
    Author: Eric Ren 

    Assumptions:
    1. Search String is case-sensitive.
    2. Log file is in chronological order.
    3. Log file is a file of lines.

"""

import sys
import argparse

def search(search_string, log_file, out_file=None):
    f = open(log_file, 'r')
    lines = f.readlines()
    lines.reverse()
    f.close()

    if out_file == None:
        for line in lines:
            if search_string in line:
                print(line[:-1])
    else:
        with open(out_file, 'w') as f:
            for line in lines:
                if search_string in line:
                    f.write(line)


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Output lines that match given search string in reverse chronological order. Search string is case sensitive.')
    parser.add_argument('logfile', help='Name of log file. Should be in chronological order.')
    parser.add_argument('string', help='Input string to search for.')
    parser.add_argument('-o', '--output', help='Use own specified output file name. Default to stdout.')
    args = parser.parse_args()
 
    search(args.string, args.logfile, args.output)

