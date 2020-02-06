from pathlib import Path
from typing import List

from pygit2 import GitError, Repository


def list_git_repositories(path: Path) -> List[Path]:
    """
    List the git repositories under a given path.

    :param path: Path to list the repositories from.
    :return: The list of git repositories.
    """
    repositories = []
    if path.is_dir():
        try:
            Repository(str(path))
            repositories.append(path)
        except GitError:
            for item in path.iterdir():
                repositories.extend(list_git_repositories(item))
    return repositories
