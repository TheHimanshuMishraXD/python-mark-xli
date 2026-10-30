import argparse

parser = argparse.ArgumentParser()
#add command line argument
parser.add_argument("url",help="description of argument 1")
parser.add_argument("arg2",help = "by which name do you want to save the file")


args = parser.parse_args()

print(args.arg1)
print(args.arg2)