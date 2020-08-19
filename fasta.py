#!/usr/bin/env python3
# -*-coding:utf-8 -*-
"""

Contact:zczljw4@ucl.ac.uk

Script:

Description:

Example:

Usage: python3 template.py -i input.file -o output_dir

Options:
  -i <input>  input file
  -o <out>  output Path of analysis
  -h --help
"""
import sys
import re
import os
import time
import argparse
import pandas as pd
import numpy as np
from Bio import SeqIO 

starttime = time.time()

def Main():
    args = argparse.ArgumentParser(description='for analysising ......')
    args.add_argument("-i", "--input", type=str, help="input group.list", required=True)
    args.add_argument("-f", "--fasta", type=str, help="input fasta.file", required=True)
    args.add_argument("-o", "--out", type=str, help="output dir", required=True)
    args = args.parse_args()
    return args

args = Main()
group_list =  pd.read_csv(args.input, header = None, sep = " ")
dict1 = {}
for i in range(len(group_list)):
    dict1[group_list.iloc[i,0]] = group_list.iloc[i,1]

result_fasta_chr = open("result_chr.fasta","w")
result_fasta_other = open("result_other.fasta","w")
for record in SeqIO.parse(args.fasta, "fasta"):
    if record.id in dict1.keys():
      new_id = record.id.replace(record.id,dict1[record.id])
      print(new_id)
      result_fasta_chr.write(">"+new_id+"\n")
      result_fasta_chr.write(str(record.seq)+"\n")
    else:
      result_fasta_other.write(">"+record.id+"\n")
      result_fasta_other.write(str(record.seq)+"\n")

result_fasta_chr.close()
result_fasta_other.close()

endtime = time.time()
print("done",'\n')
print ("Total elapsed time: ",endtime - starttime)
if __name__ == '__main__':
    Main()
