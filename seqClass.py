#!/usr/bin/env python

import sys, re
from argparse import ArgumentParser

parser = ArgumentParser(description = 'Classify a sequence as DNA or RNA')
parser.add_argument("-s", "--seq", type = str, required = True, help = "Input sequence")
parser.add_argument("-m", "--motif", type = str, required = False, help = "Motif")

if len(sys.argv) == 1:
    parser.print_help()
    sys.exit(1)

args = parser.parse_args()

args.seq = args.seq = args.seq.upper()			# transform sequence into upperclass
if re.search('^[ACGTU]+$', args.seq):			# search for ACGTU in sequence
    if re.search('T', args.seq):			# if T is in sequence
        print ('The sequence is DNA')
    elif re.search('U', args.seq):			# if U is in sequence
        print ('The sequence is RNA')
    else:
        print ('The sequence can be DNA or RNA')
else:
    print ('The sequence is not DNA nor RNA')

if args.motif:						# if a motif is entered
    args.motif = args.motif.upper()			# transform motif into upperclass
    print(f'Motif search enabled: looking for motif "{args.motif}" in sequence "{args.seq} "... ', end = '')
    if re.search(args.motif, args.seq):			# if motif is found
        print("MOTIF FOUND")
    else:
        print("MOTIF NOT FOUND")
