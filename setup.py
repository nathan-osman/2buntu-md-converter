#!/usr/bin/env python3

from distutils.core import setup


setup(
    name='2bconverter',
    version='0.1',
    description="An HTML and WP shortcode to markdown conversion script.",
    author='Nitin Venkatesh',
    author_email='nitin@technizns.com',
    url='https://github.com/nathan-osman/2buntu-md-converter',
    license='MIT',
    packages=['twobuntu.markdown'],
    scripts=['scripts/2bconverter'],
    classifiers=[
        'Development Status :: 3 - Alpha',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ]
)
