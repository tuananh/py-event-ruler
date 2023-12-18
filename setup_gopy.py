import os
import setuptools
import re

def normalize(name):  # https://peps.python.org/pep-0503/#normalized-names
    return re.sub(r"[-_.]+", "-", name).lower()

PACKAGE_PATH=os.getenv("_PACKAGE_PATH", "event_ruler")
PACKAGE_NAME=PACKAGE_PATH.split("/")[-1]

with open('README.md') as f:
    readme = f.read()

with open('LICENSE') as f:
    license = f.read()
    
setuptools.setup(
    name=normalize(PACKAGE_NAME),
    version="0.3.0",
    author="Tuan Anh Tran",
    author_email="me@tuananh.org",
    description="Test EventBridge pattern with Python locally",
    long_description=readme,
    long_description_content_type="text/markdown",
    license=license,
    url="https://github.com/tuananh/py-event-ruler",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    include_package_data=True,
    package_dir={".": f"./_tmp/{PACKAGE_PATH}/../"},
    package_data={"": ["*.so"]}
)
