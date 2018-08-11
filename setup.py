import setuptools

with open('README.md', 'r') as fh:
    long_description = fh.read()

setuptools.setup(
    name='questradeapi',
    version='0.0.3',
    author='Antoine Viscardi',
    author_email='antoine.viscardi@gmail.com',
    description='Python wrapper for the Questrade API',
    long_description=long_description,
    long_description_content_type='text/markdown',
    url='https://github.com/antoineviscardi/questradeapi',
    license='MIT',
    packages=setuptools.find_packages(),
    classifiers=(
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',    
    ),
)