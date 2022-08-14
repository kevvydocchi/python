import argparse

parser = argparse.ArgumentParser()
parser.add_argument("echo", help="Echo the string we use here")
arg = parser.parse_args()
print(arg.echo)