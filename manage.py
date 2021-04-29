import argparse

parse = argparse.ArgumentParser(description="Active Directory Management")
parse.add_argument("-list", help="List all process")
args = parse.parse_args()

if args.list:
    print("Parameter input is:", args.list)
