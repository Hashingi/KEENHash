# KEENHash: Hashing Programs into Function-Aware Embeddings for Large-Scale Binary Code Similarity Analysis (ISSTA'25)
## Description
The repository provides the KEENHash-generated program embeddings to the binaries from coreutils, diffutils, and findutils which are used in our study and [DeepBinDiff](https://github.com/yueduan/DeepBinDiff). To generate the embeddings for your own binaries, please refer to [BinaryAI](https://www.binaryai.cn). You can log in and create an API key to use the [binaryai-sdk](https://github.com/binaryai/sdk) for the embedding generation.

The directory structure is as follows:

```
.
├── data    # The directory stores the program embeddings to binaries
└── script  # The directory contains the script for evaluating the similarity between binaries
```

**Note:** We also provide the long version of the KEENHash paper.

## Environment
You can use the following command of conda to install the required packages and activate the environment:

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
