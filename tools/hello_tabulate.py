import argparse
from tabulate import tabulate

parser = argparse.ArgumentParser(description="My open-source learning tool")
parser.add_argument("--name", default="World", help="Enter your name")
args = parser.parse_args()

rows = [
    ["Student", args.name],
    ["Subject", "Information Systems Security"],
    ["Library", "tabulate"],
    ["Goal", "Learn open-source tools"],
]

print(tabulate(rows, headers=["Item", "Details"], tablefmt="grid"))