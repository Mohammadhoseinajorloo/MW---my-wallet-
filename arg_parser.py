import argparse


parser = argparse.ArgumentParser()


parser.add_argument("--Rejester","--R",
                    nargs=2,
                    help="This create a user")
parser.add_argument("--Login","--L",
                    nargs=2,
                    help="This login a user")


args = parser.parse_args()
