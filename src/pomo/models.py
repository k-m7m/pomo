import argparse
from dataclasses import dataclass


@dataclass
class PomoParam:
    work: int
    short_break: int
    long_break: int
    count: int

    @classmethod
    def from_cli_args(cls) -> "PomoParam":
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
        return cls(
            work=args.work * 60,
            short_break=args.short_break * 60,
            long_break=args.long_break * 60,
            count=args.count,
        )
