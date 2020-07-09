import yaml

try:
    from yaml import CLoader as Loader, CDumper as Dumper
except ImportError:
    from yaml import Loader, Dumper

import argparse
import requests
from pybars import Compiler
from naislinter import linter


def parse_args():
    parser = argparse.ArgumentParser(
        "nais-linter", description="Validates naiserator yaml files"
    )
    parser.add_argument("input", type=str, help="The input naiserator yaml file")

    args = parser.parse_args()
    return args.input


def fetch_reference():
    return yaml.load(
        requests.get(
            "https://raw.githubusercontent.com/nais/naiserator/master/config/nais.io_applications.yaml"
        ).text,
        Loader=Loader,
    )["spec"]["validation"]["openAPIV3Schema"]


def get_target(infile):
    with open(infile, "r") as f:
        contents = f.read()
        return yaml.load(contents, Loader=Loader)


def main():
    infile = parse_args()
    target = get_target(infile)
    reference = fetch_reference()
    if linter.check_keys(target, reference):
        exit(1)


if __name__ == "__main__":
    main()
