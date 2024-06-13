# KEENHash
## Note in Paper
* $mAP@k$ is a metric that evaluates the mean (across all retrieving results) of the average of the $Precision@k_i$ ($k_i \in \lbrace i | 1 \leq i \leq k \wedge r(i) = 1 \rbrace$ where $r(i) = 1$ represents that the $i_{th}$ retrieved sample is in the same class to the query sample; otherwise, $r(i) = 0$) to one retrieving. The higher the ranking of same-class results returned, the greater the $mAP@k$.
* $mP@k$ is a metric that calculates the mean of the $Precision@k$ across all retrieving.
* Where $Precision@k_i$ presents the ratio of retrieved same-class samples to the retrieved $Top-k_i$ ones.
* Ref: https://www.educative.io/answers/what-is-the-mean-average-precision-in-information-retrieval

## Description
The repository provides the KEENHash-generated program embeddings to the binaries from coreutils, diffutils, and findutils which are used in [DeepBinDiff](https://github.com/yueduan/DeepBinDiff).

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
