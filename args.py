from argparse import ArgumentParser, Namespace

def parse_args() -> Namespace:
    """
    Parses arguments from the command line and returns a Namespace object with
    the parsed argument values.
    """
    parser: ArgumentParser = ArgumentParser()

    parser.add_argument('--data-dir', type=str, default='./dataset/')
    parser.add_argument('--csv-filename', type=str, default='brown.csv')
    parser.add_argument('--n-examples', type=int, default=3)
    parser.add_argument('--cipher', type=str, choices=['caesar'], default='caesar')
    parser.add_argument('--no-train-augment', action='store_true', default=False)
    parser.add_argument('--caesar-shift', type=int, default=10)
    parser.add_argument('--perturb-prob', type=float, default=0)
    parser.add_argument('--random-test', action='store_true', default=False)
    
    return parser.parse_args()