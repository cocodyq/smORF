#!/usr/bin/env bash

set -e
set -o pipefail

#make db
diamond makedb --in clust_result/0.5_result/metag_ProG_nonsingleton_0.5_clu_rep.faa -d metag_ProG_ns_0.5
diamond makedb --in clust_result/0.9_result/metag_ProG_nonsingleton_0.9_clu_rep.faa -d metag_ProG_ns_0.9

mkdir result_0.5
mkdir result_0.9

#align 
DIR="diamond/split"
for file in $(ls $DIR)
  do
    diamond blastp -q diamond/split/$file -d diamond/metag_ProG_ns_0.5 -o diamond/result_0.5/$file.tsv -e 0.00001 --id 90 -b 12 -c 1
    diamond blastp -q diamond/split/$file -d diamond/metag_ProG_ns_0.9 -o diamond/result_0.9/$file.tsv -e 0.00001 --id 90 -b 12 -c 1
  done
