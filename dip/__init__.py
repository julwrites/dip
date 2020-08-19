import sys
import argparse


def parse_arguments(args=""):
    parser = argparse.ArgumentParser(
        documentation="Dit: Documentation for git."
    ).add_argument(
        parser="repository",
        metavar="REPO",
        type=str,
        help=
        "The path to the root of the repository to be documented. This should be a git repository root."
    ).add_argument(
        parser="config",
        metavar="CFG",
        type=str,
        help=
        "The path to the config file for dit to load and use as reference for documentation/linting"
    )

    try:
        parser.parse_args(args=args)
    except SystemExit as e:
        raise e


def main():
    parse_arguments()
