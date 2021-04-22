
import argparse

parser = argparse.ArgumentParser()

parser.add_argument('-h', '--help', help='helpful message showing flags and usage of insapy')
parser.add_argument('-f', '--file', help='The filename of file to apply filter to')
parser.add_argument('-se', '--sepia', help='Select sepia filter')
parser.add_argument('-g', '--gray', help='Select gray filter')
parser.add_argument('-sc', '--scale', help=' Scale factor to resize image')
parser.add_argument('-i', '--implement', help='Choose the implementatin')
parser.add_argument('-o', '--out', help='The output filename')

args = parser.parse_args()

# TODO: implement flags