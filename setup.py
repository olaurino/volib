import sys
from setuptools import setup, find_packages, Command
from setuptools.command.test import test as TestCommand

class PyTest(TestCommand):
    user_options = [('pytest-args=', 'a', "Arguments to pass to py.test")]

    def initialize_options(self):
        TestCommand.initialize_options(self)
        self.pytest_args = []

    def finalize_options(self):
        TestCommand.finalize_options(self)
        self.test_args = []
        self.test_suite = True

    def run_tests(self):
        #import here, cause outside the eggs aren't loaded
        import pytest
        errno = pytest.main(self.pytest_args)
        sys.exit(errno)

version = '0.1'

setup(name='volib',
      version=version,
      description="A Python Library and Library Generator for the Virtual Observatory",
      classifiers=[],
      keywords='',
      author='Omar Laurino',
      author_email='olaurino@cfa.harvard.edu',
      url='',
      license='GPL3',
      packages=find_packages(exclude=['ez_setup', 'examples', 'tests']),
      include_package_data=True,
      zip_safe=True,
      install_requires=[
	  'six',
          'furl',
          'jinja2',
          'networkx',
          'pyxb==1.2.4',
      ],
      tests_require=[
	      'pytest-cov',
      ],
      cmdclass={'test': PyTest},
      entry_points="""
[vodml.resolver]
ivoa,1.0=volib.astro.ivoa_1_0:resolver
""",
      )
