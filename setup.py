from setuptools import setup

setup(
    name='httpserver',
    description='''Sets up server and client sockets''',
    author='Cody Dibble and Philip Werner',
    package_dir={'': 'src'},
    py_modules=['client', 'server'],
    install_requires=[],
    extras_require={
        'tests': ['pytest', 'pytest-cov', 'tox'],
        'development': ['ipython']},
    entry_points={
        'console_scripts': [
            'runme = server:server'
        ]})
