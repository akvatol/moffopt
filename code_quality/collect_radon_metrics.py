"""
Script for collecting Radon's code quality metrics.

See:
* https://radon.readthedocs.io/en/latest/intro.html
* https://radon.readthedocs.io/en/latest/commandline.html
"""

from enum import Enum
from pathlib import Path
from subprocess import run
from sys import argv
from json import dumps, loads


class RadonArgs(str, Enum):
    radon = "radon"
    json = "--json"
    raw = "raw"
    hal = "hal"
    cc = "cc"
    mi = "mi"


def collect_radon_metrics(path: Path) -> dict:
    return {
        RadonArgs.raw: collect_radon_metric_raw(path),
        RadonArgs.hal: collect_radon_metric_hal(path),
        RadonArgs.cc: collect_radon_metric_cc(path),
        RadonArgs.mi: collect_radon_metric_mi(path),
    }


def collect_radon_metric_raw(path: Path) -> dict:
    return run_radon_with_json_flag(path, RadonArgs.raw)


def collect_radon_metric_hal(path: Path) -> dict:
    return run_radon_with_json_flag(path, RadonArgs.hal)


def collect_radon_metric_cc(path: Path) -> dict:
    return run_radon_with_json_flag(path, RadonArgs.cc)


def collect_radon_metric_mi(path: Path) -> dict:
    return run_radon_with_json_flag(path, RadonArgs.mi)


def run_radon_with_json_flag(path: Path, metric: str) -> dict:
    command = [RadonArgs.radon, metric, RadonArgs.json, path]
    return loads(run(args=command, capture_output=True).stdout)


if __name__ == "__main__":
    path = Path(argv[1])
    print(dumps(collect_radon_metrics(path), indent=4))
