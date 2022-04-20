from setuptools import find_packages, setup


# Read the readme file into a string variable inject
# into the long_description paramter of our setup function
# call
with open("README.md", "r") as file_handler:
    long_description: str = file_handler.read()

setup(
        name="flitton_fib_py",
        version="0.0.1",
        author=" Daniel Temiagin",
        author_email="danile.temiagin@gmail.com",
        description="Calculate a Fibonacci number",
        long_description=long_description,
        long_description_content_type="text/markdown",
        url="https://github.com/talk2drys/flitton-fib-py",
        install_requires=[],
        packages=find_packages(exclude=("tests",)),
        classifiers=[ 
            "Development Status :: 4 - Beta",
            "Programjing Language :: Python 3",
            "Operating System :: OS Independent",
            ],
        python_requires='>=-3',
        test_requires=["pytest"],
        )
