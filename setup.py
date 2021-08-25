from setuptools import setup
import codecs
import os
import re

here = os.path.abspath(os.path.dirname(__file__))

# Read the version number from a source file.
# Why read it, and not import?
# see https://groups.google.com/d/topic/pypa-dev/0PkjVpcxTzQ/discussion
def find_version(*file_paths):
    # Open in Latin-1 so that we avoid encoding errors.
    # Use codecs.open for Python 2 compatibility
    with codecs.open(os.path.join(here, *file_paths), 'r', 'latin1') as f:
        version_file = f.read()

    # The version line must have the form
    # __version__ = 'ver'
    version_match = re.search(r"^__version__ = ['\"]([^'\"]*)['\"]",
                              version_file, re.M)
    if version_match:
        return version_match.group(1)
    raise RuntimeError('Unable to find version string.')

with open("README.rst", "r") as fh:
    long_description = fh.read()

setup(name='slackeventsapi',
      version=find_version('slackeventsapi', 'version.py'),
      description='Python Slack Events API adapter for Flask',
      url='http://github.com/slackapi/python-slack-events-api',
      author='Slack Technologies, LLC',
      author_email='opensource@slack.com',
      license='MIT',
      packages=['slackeventsapi'],
      long_description_content_type='text/x-rst',
      long_description=long_description,
      install_requires=[
          'flask>=1,<2',
          'pyee>=7,<8',
          'itsdangerous<2', # for Python 2.7
          'Jinja2<3', # for Python 2.7
          'MarkupSafe<2', # for Python 2.7
      ],
      classifiers=[
          'Development Status :: 5 - Production/Stable',
          'Intended Audience :: Developers',
          'Topic :: Communications :: Chat',
          'Topic :: System :: Networking',
          'Topic :: Office/Business',
          'License :: OSI Approved :: MIT License',
          'Programming Language :: Python',
          'Programming Language :: Python :: 2.7',
          'Programming Language :: Python :: 3.5',
          'Programming Language :: Python :: 3.6',
          'Programming Language :: Python :: 3.7',
          'Programming Language :: Python :: 3.8',
      ],
      zip_safe=False)
