from setuptools import setup, find_packages

setup(
    name='compute_net',
    version='1.0.0',
    packages=find_packages(),
    entry_points={
        'console_scripts': [
            'compute_net=compute_net.main:main'
        ]
    }
)
