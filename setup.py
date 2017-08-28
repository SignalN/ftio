from setuptools import setup

setup(
  name = 'ftio',
  packages = ['ftio', 'ftio.wiki'], # this must be the same as the name above
  version = '0.7',
  description = 'Python tools for working with fastText, an open-source library from the Facebook AI Research lab',
  author = 'Signal N',
  author_email = 'ftio@signaln.com',
  url = 'https://github.com/signaln/ftio',
  download_url = 'https://github.com/signaln/ftio/archive/0.7.tar.gz',
  keywords = ['fastText', 'word2vec', 'word embeddings', 'natural language processing', 'text'],
  classifiers = [],
)
