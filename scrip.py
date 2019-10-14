import pandas as pd
import sys

from argparse import ArgumentParser


def read_csv_to_json(filename, destination):
	try:
		print("Data processing. CSV file reading starting")
		df = pd.read_csv(filename, destination)
		print("Data processed. CSV file reading completed and processing to Json File")
		df.to_json(destination)
		print("Json File creation completed.")
	except Exception as error:
		print("Error while processing script. Please try again. Error: {}".format(error))


if __name__ == "__main__":
	parser = ArgumentParser()
	parser.add_argument("-f", "--file", dest="filename",
	                    help="CSV FILE", metavar="FILE")

	parser.add_argument("-d", "--filedest", dest="filenamedestination",
	                    help="write report to FILE", metavar="FILE")
	args = parser.parse_args()
	if args.filename is None and args.filenamedestination:
		print("Please provide file path inorder to proceed this action.")
		sys.exit(0)
	read_csv_to_json(args.filename, args.filenamedestination)
