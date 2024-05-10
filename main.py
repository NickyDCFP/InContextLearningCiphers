from argparse import Namespace
import pandas as pd

from args import parse_args
from data import get_data
from prompt import build_prompt


def main():
    args: Namespace = parse_args()

    dataset: pd.DataFrame = get_data(args.data_dir, args.csv_filename)

    prompt: str; test: str
    prompt, test = build_prompt(
        ['caesar'],
        dataset,
        3,
        [{'shift' : 10}],
    )
    print(prompt)
    print(f"True Decryption: {test}")

if __name__ == '__main__':
    main()