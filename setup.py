from setuptools import find_packages, setup

with open("README.md","r") as f:
  long_description = f.read()

setup(
  name="optimisation_algorithms",
  version="0.0.10",
  description="An optimisation tools for minimising functions and inversing matrix",
  packages=find_packages(),
  long_description=long_description,
  long_description_content_type="text/markdown",
  keywords=['python', 'optimisation', 'minimisation', 'inverse', 'functions', 'matrix'],
  url="https://github.com/Ismailea4/Optimisation_algorithms",
  author="Ismail_Eladraoui",
  author_email="eladraoui.ismail4@gmail.com",
  classifiers=[
    "Programming Language :: Python :: 3.10",
  ],
  extras_require={
    "dev": ["pytest>=7.0", "twine>=4.02"],
  },
  python_requires=">=3.10",
)
  
