import json
import os
import subprocess
import sys
import re
from distutils.core import Extension

import setuptools
from setuptools.command.build_ext import build_ext

def normalize(name):  # https://peps.python.org/pep-0503/#normalized-names
    return re.sub(r"[-_.]+", "-", name).lower()

PACKAGE_PATH=REPLACE_ME
PACKAGE_NAME=PACKAGE_PATH.split("/")[-1]

# https://pip.pypa.io/en/latest/user_guide/#using-pip-from-your-program
subprocess.check_call([sys.executable, '-m', 'pip', 'install', 'pybindgen'])

if sys.platform == 'darwin':
    PYTHON_BINARY = os.getenv("PYTHON_BINARY_PATH")
if sys.platform == 'linux':
    PYTHON_BINARY = sys.executable


def _generate_path_with_gopath():
    go_path = subprocess.check_output(["go", "env", "GOPATH"]).decode("utf-8").strip()
    path_val = f'{os.getenv("PATH")}:{go_path}/bin'
    return path_val


class CustomBuildExt(build_ext):
    def build_extension(self, ext: Extension):
        bin_path = _generate_path_with_gopath()
        go_env = json.loads(subprocess.check_output(["go", "env", "-json"]).decode("utf-8").strip())

        destination = os.path.dirname(os.path.abspath(self.get_ext_fullpath(ext.name))) + f"/{PACKAGE_NAME}"
        subprocess.check_call(
            ["go", "install", "golang.org/x/tools/cmd/goimports@latest"],
            env={"PATH": bin_path, **go_env},
        )

        subprocess.check_call(
            ["go", "install", "github.com/go-python/gopy@v0.4.5"],
            env={"PATH": bin_path, **go_env},
        )

        subprocess.check_call(
            [
                "gopy",
                "build",
                "-dynamic-link=True",
                "-output",
                destination,
                "-vm",
                PYTHON_BINARY,
                *ext.sources,
            ],
            env={"PATH": bin_path, **go_env, "CGO_LDFLAGS_ALLOW": '.*'},
        )

        # dirty hack to avoid "from pkg import pkg", remove if needed
        with open(f"{destination}/__init__.py", "w") as f:
            f.write(f"from .{PACKAGE_NAME} import *")


setuptools.setup(
    name=normalize(PACKAGE_NAME),
    version="0.1.0",
    author="change_me",
    author_email="change_me@example.com",
    description="",
    url="https://github.com/go-python/gopy",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: BSD License",
        "Operating System :: OS Independent",
    ],
    include_package_data=True,
    cmdclass={
        "build_ext": CustomBuildExt,
    },
    ext_modules=[
        Extension(PACKAGE_NAME, [PACKAGE_PATH],)
    ],
)
