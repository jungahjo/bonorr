from setuptools import setup, find_packages

with open('README.md', encoding='utf-8') as f:
    long_description = f.read()
setup(
    name                = 'bonorr',
    version             = '0.7.1',
    long_description    = long_description,
    long_description_content_type='text/markdown',
    description         = 'bonorr',
    license             = 'MIT',
    author              = 'bonorr',
    author_email        = 'ellen333@naver.com',
    url                 = 'https://github.com/jungahjo/bonorr',
    download_url        = 'https://github.com/jungahjo/bonorr/archive/0.0.tar.gz',
    install_requires    = [
        "numpy < 1.15"
    ],
    packages            = find_packages(exclude = []),
    keywords            = ['bonorr'],
    python_requires     = '>=3',
    package_data        = {},
    zip_safe            = False,
    classifiers         = [
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.2',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
    ],
)
