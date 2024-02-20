import argparse


parser = argparse.ArgumentParser()


parser.add_argument("--login",
                    nargs=3,
                    help="This create a user")


args = parser.parse_args()
