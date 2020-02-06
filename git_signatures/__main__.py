from argparse import ArgumentParser
from logging import _nameToLevel as logging_name_to_level
from pathlib import Path

from coloredlogs import install as coloredlogs_install

from git_signatures.resolving import resolve


def main() -> None:
    """Entry point of the git-signatures tool."""
    parser = ArgumentParser("git-signatures", description="Git Signatures Resolver.")
    parser.add_argument("repositories", type=Path, help="Repositories to resolve.")
    parser.add_argument(
        "--log-level",
        default="INFO",
        choices=logging_name_to_level,
        help="Logging verbosity.",
    )
    args = parser.parse_args()

    coloredlogs_install(
        level=args.log_level,
        fmt="%(asctime)s %(name)10s %(message)s",
        datefmt="%H:%M:%S",
    )
    delattr(args, "log_level")

    resolve(**vars(args))
