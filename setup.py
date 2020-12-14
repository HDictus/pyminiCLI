from setuptools import setup

with open('README.md', encoding='utf-8') as f:
    README = f.read()

setup(
    name='pyminiCLI',
    version='0.1.7',
    packages=['minicli'],
    license='MIT',
    author='HDIctus',
    tests_require=['pytest'],
    author_email='h.t.dictus@gmail.com',
    description='quick and easy command-line interfaces',
    long_description=README,
    long_description_content_type="text/markdown",
    url="https://github.com/HDictus/pyminiCLI"
)
