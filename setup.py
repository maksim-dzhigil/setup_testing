# from distutils.core import setup
import io
import os
from setuptools import setup


def read(*names, **kwargs):
    with io.open(
        os.path.join(os.path.dirname(__file__), *names),
        encoding=kwargs.get("encoding", "utf8"),
    ) as fp:
        return fp.read()


def find_requirements(*file_path):
    requirements = read(*file_path).split("\n")
    return [req for req in requirements if req]


requirements = find_requirements("requirements.txt")

setup(
    name="testprojlib",
    packages=['code', 'code.utils'],
    url='https://github.com/maksim-dzhigil/setup_testing',
    install_requires=requirements
)
