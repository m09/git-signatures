from logging import getLogger
from pathlib import Path

from pygit2 import GIT_SORT_TOPOLOGICAL, Repository

from git_signatures._utils import list_git_repositories


_logger = getLogger(__name__)


def resolve(repositories: Path) -> None:
    """
    Resolve signature in the given repositories.

    :param repositories: Git repositories to parse for signatures.
    """
    repository_paths = list_git_repositories(repositories)
    _logger.info("Detected %d git repositories", len(repository_paths))
    _logger.info("Extracting signatures")
    signatures = set()
    for repository_path in repository_paths:
        repository = Repository(str(repository_path))
        for commit in repository.walk(repository.head.target, GIT_SORT_TOPOLOGICAL):
            name = commit.author.name.lower()
            email = commit.author.email.lower()
            signatures.add((repository_path, email, name))
    for repo_path, email, name in signatures:
        print(repo_path.name, email, name)
    _logger.info("Found %d signatures", len(signatures))
