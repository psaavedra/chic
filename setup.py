from setuptools import setup, find_packages

version = "0.0.1"

long_description = ""
try:
    long_description=file('README.md').read()
except Exception:
    pass

license = ""
try:
    license=file('LICENSE').read()
except Exception:
    pass


setup(
    name = 'chips',
    version = version,
    description = 'Checks for Inputs, Protocols and Services',
    author = 'Pablo Saavedra',
    author_email = 'saavedra.pablo@gmail.com',
    url = 'http://github.com/psaavedra/chips',
    packages = find_packages(),
    package_data={
    },
    scripts=[
        "tools/chips-checker",
        "tools/chips-get",
    ],
    zip_safe=False,
    install_requires=[
        "httplib2",
        "urllib2",

    ],
    # data_files=[
    #     ('/etc/', ['cfg/data.cfg']),
    #     ('/etc/init.d', ['init-script'])
    # ],

    download_url= 'https://github.com/psaavedra/chips/zipball/master',
    classifiers=[
        "Development Status :: 2 - Pre-Alpha",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Programming Language :: Python",
        "Topic :: Internet :: WWW/HTTP :: Dynamic Content",
        "Topic :: Software Development :: Libraries :: Python Modules",
    ],
    long_description=long_description,
    license=license,
    keywords = "python check streaming udp sources",
)
