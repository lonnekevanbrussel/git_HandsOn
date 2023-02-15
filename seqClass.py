#!/usr/bin/env python

import sys, re
from argparse import ArgumentParser
from collections import Counter

parser = ArgumentParser(description = 'Classify a sequence as DNA or RNA')
parser.add_argument("-s", "--seq", type = str, required = True, help = "Input sequence")
parser.add_argument("-m", "--motif", type = str, required = False, help = "Motif")
parser.add_argument("-p", "--perc", type = int, required = False, help = "Percentage in decimals")

if len(sys.argv) == 1:
    parser.print_help()
    sys.exit(1)

args = parser.parse_args()

args.seq = args.seq = args.seq.upper()			# transform sequence into upperclass
if re.search('^[ACGTU]+$', args.seq):			# search for ACGTU in sequence
    if re.search('T', args.seq) and re.search('U', args.seq):		# if T ánd U are in the sequence
        print ('The sequence is not DNA nor RNA')
    elif re.search('T', args.seq):			# if T is in sequence
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

# if percentage argument is added, calculate per base type the percentage in the sequence
if args.perc:
    base_counter = Counter(args.seq)
    seq_length = len(args.seq)
    for base, value in base_counter.items():
        print("Percentage " + base + " in sequence " + args.seq + ": " + str(round((value/seq_length)*100,args.perc)) + "%")
