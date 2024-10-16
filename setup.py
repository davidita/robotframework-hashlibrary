from setuptools import setup, find_packages

setup(
    name='robotframework-hashlibrary',
    version='0.1',
    description='Een simpele Robot Framework library',
    author='David Italiander',
    author_email='david.italiander@gmail.com',
    packages=find_packages(),
    install_requires=[
        'robotframework',
        'pytest',
    ],
    classifiers=[
        'Programming Language :: Python',
        'Framework :: Robot Framework',
    ],
)