from argparse import ArgumentParser, Namespace

def parse_args() -> Namespace:
    parser: ArgumentParser = ArgumentParser()

    parser.add_argument('--data-dir', type=str, default='./dataset/')
    parser.add_argument('--csv-filename', type=str, default='brown.csv')
    parser.add_argument('--cipher', type=str, choices=['caesar'])
    
    return parser.parse_args()