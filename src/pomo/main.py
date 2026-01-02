import argparse
import math
import sys
import time
from dataclasses import dataclass


@dataclass
class PomoParam:
    work: int
    short_break: int
    long_break: int
    count: int


def parse_arguments() -> PomoParam:
    argument_parser = argparse.ArgumentParser()
    argument_parser.add_argument(
        "-w",
        "--work",
        type=int,
        default=25,
        help="Duration of work period in minutes (default: 25)",
    )
    argument_parser.add_argument(
        "-s",
        "--short-break",
        type=int,
        default=5,
        help="Duration of break period in minutes (default: 5)",
    )
    argument_parser.add_argument(
        "-l",
        "--long-break",
        type=int,
        default=15,
        help="Duration of long break period in minutes (default: 15)",
    )
    argument_parser.add_argument(
        "-c",
        "--count",
        type=int,
        default=4,
        help="Number of sets in one cycle (default: 4)",
    )

    args = argument_parser.parse_args()
    return PomoParam(
        work=args.work * 60,
        short_break=args.short_break * 60,
        long_break=args.long_break * 60,
        count=args.count,
    )


def overwrite(text: str):
    sys.stdout.write("\r\033[2K")
    sys.stdout.write(text)
    sys.stdout.flush()


def countdown(duration: int, message: str) -> None:
    end_time = time.monotonic() + duration
    sec: int | None = None

    while True:
        remaining = max(0, math.ceil(end_time - time.monotonic()))

        if remaining != sec:
            sec = remaining
            minutes, seconds = divmod(sec, 60)
            overwrite(f"{message}: {minutes:02}:{seconds:02}")

        if remaining == 0:
            break

        time.sleep(0.1)


def main() -> None:
    args = parse_arguments()

    count = 0

    while True:
        countdown(args.work, "Work Time")
        count += 1
        if count % args.count != 0:
            countdown(args.short_break, "Short Break")
        else:
            countdown(args.long_break, "Long Break")
