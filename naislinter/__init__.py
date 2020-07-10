import yaml

try:
    from yaml import CLoader as Loader, CDumper as Dumper
except ImportError:
    from yaml import Loader, Dumper

import argparse
import requests
import sys
from naislinter import linter


def parse_args():
    parser = argparse.ArgumentParser(
        "naislinter", description="Validates naiserator yaml files"
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
    faults = linter.check_keys(target, reference, [], [])
    if len(faults) > 0:
        print("Found keys outside of the NAIS spec", file=sys.stderr)
        for fault in faults:
            print(f"\t{fault}", file=sys.stderr)
        print(
            "You may want to refer to https://doc.nais.io/nais-application/nais.yaml/reference",
            file=sys.stderr,
        )
        exit(1)


if __name__ == "__main__":
    main()
