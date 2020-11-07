from setuptools import setup

with open("README.md", "r") as fh:
    long_description = fh.read()

setup(name='jakesutils',
      version='0.2',
      description='A collection of utils that I use all the time in my projects',
      long_description=long_description,
      long_description_content_type="text/markdown",
      url='https://github.com/JakeRoggenbuck/jakesutils',
      author='Jake Roggenbuck',
      author_email='jake@jr0.org',
      license='MIT',
      packages=['jakesutils'],
      zip_safe=False)
