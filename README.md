# KEENHash
The repository provides the KEENHash-generated program embeddings to the binaries from coreutils which is used in [DeepBinDiff](https://github.com/yueduan/DeepBinDiff).

The directory structure is as follows:

```
.
├── data    # The directory stores the program embeddings to binaries
└── script  # The directory contains the script for evaluating the similarity between binaries
```

## Environment
You can use the following command of conda to install required packages and activate the environment:

```
conda env create -f environment.yaml
conda activate keenhash
```

## Evaluate Similarity between Binary Programs 

You can use the following command to evaluate the similarity between two binaries:

```
python script/evaluate_similarity.py --query <path to the query program embedding>  --repo <path to the repo program embedding> --embedding <KEENHash method> [--lsh <number of hash functions>]
```

For example:
```
python script/evaluate_similarity.py --query data/coreutils-5.93-O0_basename.json  --repo data/coreutils-5.93-O3_ln.json --embedding stru
```

To get more information, you can use the following command:
```
python script/evaluate_similarity.py -h
```