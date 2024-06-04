import json
import logging
import warnings
import argparse

import numpy as np

from sklearn import random_projection
from sklearn.metrics.pairwise import cosine_similarity
from scipy.spatial import distance

logger = logging.getLogger(name=__name__)
warnings.filterwarnings("ignore", category=UserWarning)


def main(args):
    logger.debug('Loading query program embedding...')
    with open(args.query, 'r') as f:
        query = json.load(f)

    logger.debug('Loading repo program embedding...')
    with open(args.repo, 'r') as f:
        repo = json.load(f)

    logger.debug('Evaluating similarity...')
    dist = None
    query_embedding = None
    repo_embedding  = None
    if args.embedding == 'stru':
        query_embedding = np.unpackbits(np.array(query['keenhash_16_stru']).astype(np.uint8)).reshape(-1)
        repo_embedding  = np.unpackbits(np.array(repo['keenhash_16_stru']).astype(np.uint8)).reshape(-1)

        dist = 'jaccard'
    elif args.embedding == 'sem':
        query_embedding = np.array(query['keenhash_f_sem']).reshape(1, -1)
        repo_embedding  = np.array(repo['keenhash_f_sem']).reshape(1, -1)

        dist = 'cosine'

        if args.lsh is not None and args.lsh > 0:
            transformer = random_projection.GaussianRandomProjection(
                n_components=args.lsh,
                random_state=1024)

            query_embedding = transformer.fit_transform(query_embedding).astype(np.float32)
            query_embedding = np.where(query_embedding >= 0, 1, 0).reshape(-1)

            repo_embedding = transformer.fit_transform(repo_embedding).astype(np.float32)
            repo_embedding = np.where(repo_embedding >= 0, 1, 0).reshape(-1)

            dist = 'hamming'

    logger.debug(f'The query embedding shape: {query_embedding.shape}')
    logger.debug(f'The repo embedding shape: {repo_embedding.shape}')

    logger.info(f'Evaluated Similarity ({dist}): {evaluate_similarity(query_embedding, repo_embedding, dist)}')


def evaluate_similarity(query: np.ndarray, repo: np.ndarray, dist: str):
    if dist == 'jaccard':
        return 1 - distance.jaccard(query.reshape(-1), repo.reshape(-1))
    elif dist == 'cosine':
        return cosine_similarity(query, repo)[0][0]
    elif dist == 'hamming':
        return 1 - distance.hamming(query, repo)


def parse_options():
    parser = argparse.ArgumentParser('Similarity Evaluation for KEENHash-generated Program Embeddings', add_help=True)

    parser.add_argument('--query', type=str, required=True,
                        help="The path to the program embedding of query binary.")

    parser.add_argument('--repo', type=str, required=True,
                        help="The path to the program embedding of repo binary.")

    parser.add_argument('--embedding', choices=['stru', 'sem'], default='stru',
                        help="Set the embedding to use for similarity evaluation.")

    parser.add_argument('--lsh', type=int,
                        help="The number of LSH functions if using RPH-based hashing for sem.")

    parser.add_argument('--log-level', choices=['DEBUG', 'INFO', 'WARNING', 'ERROR', 'CRITICAL'], default='INFO',
                        help="Set the logging level.")

    parser.add_argument('--logging-file-name', type=str, default=None,
                        help="The name of the log file. If not specified, log output will be directed to the console.")

    args, _ = parser.parse_known_args()

    return args


if __name__ == '__main__':
    args = parse_options()

    logging.basicConfig(level=args.log_level, filename=args.logging_file_name, format='[%(asctime)s] - %(name)s[line:%(lineno)d] - %(levelname)s: %(message)s')

    main(args)
