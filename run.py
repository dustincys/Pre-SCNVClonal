#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
# =============================================================================
#      FileName: run.py
#          Desc:
#        Author: Chu Yanshuo
#         Email: chu@yanshuo.name
#      HomePage: http://yanshuo.name
#       Version: 0.0.1
#    LastChange: 2016-12-05 20:34:26
#       History:
# =============================================================================
'''

import argparse

from preprocess.run_preprocess import run_preprocess_MixClone
from preprocess.run_preprocess import run_preprocess_THetA

parser = argparse.ArgumentParser()
subparsers = parser.add_subparsers()

#===============================================================================
# Add MixClone type
#===============================================================================

parser_MixClone = subparsers.add_parser('MixClone',
                                        help='''Out put MixClone format''')

parser_MixClone.add_argument('normal_bam',
                             help='''BAM file for normal sample.''')

parser_MixClone.add_argument('tumor_bam',
                             help='''BAM file for tumor sample.''')

parser_MixClone.add_argument('reference_genome',
                             help='''FASTA file for reference genome.''')

parser_MixClone.add_argument( 'input_filename_base',
                             help='''Base name of the preprocessed input
                             file to be created.''')

parser_MixClone.add_argument('segments_bed',
                             help='''BED file for segments.''')

parser_MixClone.add_argument('--max_copynumber', default=6, type=int,
                          help='''Set the maximum copy number''')

parser_MixClone.add_argument('--subclone_num', default=2, type=int,
                          help='''Set the subclone number''')

parser_MixClone.add_argument('--baseline_thred_LOH', default=0.16, type=float,
                          help='''The threshold of LOH sites fraction
                              within each segment to
                              define the segment is LOH, the range is
                             [baseline_thred_LOH, 1]. Default is
                              0.16.''')

parser_MixClone.add_argument('--baseline_thred_APM',
                          default=0.3, type=float,
                          help='''The threshold of average P and M SNP sites
                              fraction within each segment to
                              define the segment as baseline, the range is
                             [baseline_thred_APM, 1]. Default is
                              0.6.''')

parser_MixClone.add_argument( '--min_depth', default=20, type=int,
                             help='''Minimum reads depth required for both
                             normal and tumor samples.  Default is 20.''')

parser_MixClone.add_argument( '--min_base_qual', default=10, type=int,
                             help='''Minimum base quality required.
                             Default is 10.''')

parser_MixClone.add_argument( '--min_map_qual', default=10, type=int,
                             help='''Minimum mapping quality required.
                             Default is 10.''')

parser_MixClone.add_argument( '--process_num', default=1, type=int,
                             help='''Number of processes to launch for
                             preprocessing. Default is 1.''')

parser_MixClone.add_argument('--gc_correction_method', default="auto",
                             help='''The gc correction method, one of auto and
                             visual''')

parser_MixClone.add_argument('--baseline_selection_method', default="auto",
                             help='''The baseline selection method, one of auto
                             and visual''')

parser_MixClone.set_defaults(func=run_preprocess_MixClone)

#===============================================================================
# Add THetA type
#===============================================================================

parser_THetA = subparsers.add_parser('THetA',
                                     help='''Out put THetA parameter''')

parser_THetA.add_argument('BICseq_bed',
                          help='''BICseq result file''')

parser_THetA.add_argument('BICseq_bed_corrected',
                          help='''The name of corrected BICseq result file''')

parser_THetA.add_argument('tumor_SNP',
                          help='''tumor snp file, generated by THetA script''')

parser_THetA.add_argument('normal_SNP',
                          help='''normal snp file. generated by THetA script''')

parser_THetA.add_argument('--max_copynumber', default=6, type=int,
                          help='''Set the maximum copy number''')

parser_THetA.add_argument('--subclone_num', default=2, type=int,
                          help='''Set the subclone number''')

parser_THetA.add_argument('--sampleNumber', default=10000, type=int,
                          help='''Set the sample number for visual plot''')

parser_THetA.add_argument('--baseline_thred_LOH', default=0.16, type=float,
                          help='''The threshold of LOH SNP sites fraction
                              within each segment to
                              define the segment as baseline. Default is
                              0.16.''')

parser_THetA.add_argument('--baseline_thred_APM',
                          default=0.6, type=float,
                          help='''The threshold of average P and M SNP sites
                              fraction within each segment to
                              define the segment as baseline. Default is
                              0.6.''')

parser_THetA.add_argument('--gc_correction_method', default="auto",
                          help='''The gc correction method, one of auto and
                             visual''')

parser_THetA.add_argument('--baseline_selection_method', default="auto",
                          help='''The baseline selection method, one of auto and
                             visual''')

print "run preprocess THetA"
parser_THetA.set_defaults(func=run_preprocess_THetA)


args = parser.parse_args()
args.func(args)
