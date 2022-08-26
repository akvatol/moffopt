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
from typing import Union
from json import dumps, loads


class RadonArgs(str, Enum):
    RADON = "radon"
    JSON = "--json"
    RAW = "raw"
    HAL = "hal"
    CC = "cc"
    MI = "mi"


def collect_radon_metrics(path: Path) -> dict:
    return {
        RadonArgs.RAW: collect_radon_metric_raw(path),
        RadonArgs.HAL: collect_radon_metric_hal(path),
        RadonArgs.CC: collect_radon_metric_cc(path),
        RadonArgs.MI: collect_radon_metric_mi(path),
    }


def collect_radon_metric_raw(path: Path) -> dict:
    return run_radon_with_json_flag(path, RadonArgs.RAW)


def collect_radon_metric_hal(path: Path) -> dict:
    return run_radon_with_json_flag(path, RadonArgs.HAL)


def collect_radon_metric_cc(path: Path) -> dict:
    return run_radon_with_json_flag(path, RadonArgs.CC)


def collect_radon_metric_mi(path: Path) -> dict:
    return run_radon_with_json_flag(path, RadonArgs.MI)


def run_radon_with_json_flag(path: Union[Path, str], metric: str) -> dict:
    command = [RadonArgs.RADON, metric, RadonArgs.JSON, path]
    return loads(run(args=command, capture_output=True, check=True).stdout)


if __name__ == "__main__":
    print(dumps(collect_radon_metrics(Path(argv[1])), indent=4))
