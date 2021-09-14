from setuptools import setup

NAME = "BSiteDataAnalysis"

PACKAGES = ["BSiteDataAnalysis", "BSiteDataAnalysis.gui"]

DESCRIPTION = "BSiteDataAnalysis python execution environment"
KEYWORDS = ["BSiteDataAnalysis", "analysis"]
AUTHOR_EMAIL = "1@qq.com"
AUTHOR = 'b_site'

LICENSE = "MIT"

setup(
    name=NAME,
    version='0.1.0',
    description=DESCRIPTION,
    long_description='b_site',
    classifiers=[
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python',
        'Intended Audience :: Developers',
        'Operating System :: OS Independent',
    ],
    install_requires=['pika'],
    entry_points={
        'console_scripts': [
            'qatrader=TCTRADER.__init__:single_trade',
            'qatraderserver=TCTRADER.webhandler:webserver'
        ]
    },
    keywords=KEYWORDS,
    author=AUTHOR,
    author_email=AUTHOR_EMAIL,
    license=LICENSE,
    packages=PACKAGES,
    include_package_data=True,
    zip_safe=True
)