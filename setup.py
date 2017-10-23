from setuptools import setup

setup(
    name='http-server',
    description='''Sets up server and client sockets''',
    author='Cody Dibble, Chai Narukulla and Philip Werner',
    package_dir={'': 'src'},
    py_modules=['client', 'server'],
    install_requires=[],
    extras_require={
        'testing': ['pytest', 'pytest-cov', 'tox'],
        'development': ['ipython']},
    entry_points={
        'console_scripts': [
            'runme = Sockets:main'
        ]})
