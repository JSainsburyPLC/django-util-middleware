from setuptools import setup

setup(
    name='django-util-middleware',
    packages=['django_util_middleware'],
    license='MIT',
    version='0.1',
    description='Misc utility middleware for Django and DRF',
    author='Phillip B Oldham',
    author_email='phillip.oldham@rethought-solutions.com',
    keywords=['django', 'middleware'],
    classifiers=[],
    install_requires=['Django>=1.4.0'],
    test_suite='django_util_middleware.tests',
)
