from argparse import Namespace
import pandas as pd

from args import parse_args
from data import get_data
from prompt import build_prompt, remove_punc


def main():
    args: Namespace = parse_args()

    dataset: pd.DataFrame = get_data(args.data_dir, args.csv_filename)

    prompt: str; test: str
    prompt, test = build_prompt(
        [args.cipher],
        dataset,
        args.n_examples,
        [{'shift' : args.caesar_shift}],
        not args.random_test,
        args.perturb_prob,
        not args.no_train_augment
    )
    print(prompt)
    print(f"True Decryption: {test}")
    y_pred: str = input("Enter LLM Response:\n")

    y_pred = remove_punc(y_pred)
    words_test: list[str] = test.split()
    words_pred: list[str] = y_pred.split()[:len(words_test)]

    correct: int = sum(words_pred[i] == words_test[i] for i in range(len(words_pred)))
    print(f"Correct: {correct} words out of {len(words_test)}.")

if __name__ == '__main__':
    main()