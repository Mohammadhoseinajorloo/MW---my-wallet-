import argparse


parser = argparse.ArgumentParser()


parser.add_argument("--Rejester","--R",
                    nargs=2,
                    help="This create a user")
parser.add_argument("--Login","--L",
                    nargs=2,
                    help="This login a user")
parser.add_argument("--Add-bank","--A",
                    nargs=3,
                    help="This added cart and wallet")


args = parser.parse_args()
print(args)    
    
