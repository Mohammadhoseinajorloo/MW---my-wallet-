import argparse


parser = argparse.ArgumentParser()


parser.add_argument("--Rejester",
                    nargs=3,
                    help="This create a user")


args = parser.parse_args()
