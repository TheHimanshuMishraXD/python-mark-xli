import argparse

parser = argparse.ArgumentParser()
#add command line argument
parser.add_argument("arg1",help="description of argument 1")
parser.add_argument("arg2",help = "description of argument 2")


args = pareser.parse_args()