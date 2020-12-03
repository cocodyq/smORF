from jug import TaskGenerator, bvalue

@TaskGenerator
def mergeseq(outfile):
    import heapq
    import gzip
    from glob import glob
    from fasta import fasta_iter

    with gzip.open(outfile, compresslevel=1, mode='wt') as output:
        inputs = [fasta_iter(f) for f in glob(f'*.dedup.faa.gz')]
        merged = heapq.merge(*inputs, key=lambda h_seq: (h_seq[1], h_seq[0]))
        preseq="x"
        for h,seq in merged:
            if seq != preseq:
                output.write(f'>{h}\n{seq}\n')
                preseq = seq

OUTPUT_FILE="smorf_dedup.faa.gz"
mergeseq(OUTPUT_FILE)
