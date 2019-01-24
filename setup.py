from setuptools import setup, find_packages

all_packages = find_packages()

setup(
    name="wstack",
    packages=all_packages,
    entry_points={
        'console_scripts': [
            'wstack = wstack.__main__:main'
        ]
    }
)
