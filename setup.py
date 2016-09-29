from setuptools import setup, find_packages

setup(name='requestbin',
    version=0.3,
    description='a silly wrapper around requestb.in api',
    author='dparalen',
    license='GPLv3+',
    provides=['requestbin'],
    install_requires=['requests'],
    classifiers=[
            'License :: OSI Approved :: GNU General Public License v3 or later (GPLv3+)',
            'Programming Language :: Python',
            'Topic :: Software Development :: Libraries :: Python Modules',
            'Operating System :: POSIX',
            'Intended Audience :: Developers',
            'Development Status :: 4 - Beta'
    ],
    url='https://github.com/RedHatQE/requestbin',
    packages = find_packages(),
    )
