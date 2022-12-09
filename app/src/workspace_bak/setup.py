from setuptools import setup, find_packages

setup(
  install_requires=[
    'Click~=7.0',
    'sampleproject@git+https://github.com/pypa/sampleproject#sha1=2cf198529c6c5a4fa50c28505ce6a90266b89868'
  ],
  extras_require={
    's3':['boto3~=1.10.0'],
    'gcs':['google-cloud-storage~=1.23.0']
  },
  package_data={'pythonbook':['data/*']},
  name='pythonbook',
  version='1.0.0',
  packages=find_packages()
)