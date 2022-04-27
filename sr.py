import argparse
import


parser = argparse.ArgumentParser(description="convert integers to decimal system")
parser.add_argument('address')
parser.add_argument('port')
parser.add_argument('file')
args = parser.parse_args()
r = f'http://{args.adress}:{args.port}/luck'

