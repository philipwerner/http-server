from setuptools import setup

setup(
    name='Sockets',
    description='''Sets up server and client sockets''',
    author='Cody Dibble, Chai Narukulla and Philip Werner'
    package_dir={'': 'src'},
    py_modules=['Sockets'],
    install_requires=[],
    extras_require={
        'testing': ['pytest', 'pytest --cov']
        'development': ['ipython']},
    entry_points={
        'console_scripts': [
            'runme = Sockets:main'
        ]})