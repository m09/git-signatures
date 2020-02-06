from importlib.machinery import SourceFileLoader
from pathlib import Path
from types import ModuleType

from setuptools import find_packages, setup


loader = SourceFileLoader("git_signatures", "./git_signatures/__init__.py")
git_signatures = ModuleType(loader.name)
loader.exec_module(git_signatures)

setup(
    name="git-signatures",
    version=git_signatures.__version__,  # type: ignore
    description="Git Signatures Resolver.",
    long_description=(Path(__file__).parent / "README.md").read_text(encoding="utf-8"),
    long_description_content_type="text/markdown",
    author="mloncode",
    python_requires=">=3.6.0",
    url="https://github.com/mloncode/git-signatures",
    packages=find_packages(exclude=["tests"]),
    entry_points={"console_scripts": ["git-signatures=git_signatures.__main__:main"]},
    install_requires=["coloredlogs", "fastparquet", "pygit2", "PyYAML", "tqdm"],
    include_package_data=True,
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: Apache Software License",
        "Programming Language :: Python",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3 :: Only",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Topic :: Software Development :: Version Control",
        "Topic :: Software Development :: Version Control :: Git",
    ],
)
