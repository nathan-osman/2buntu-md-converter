## 2buntu-md-converter

A Python script to convert HTML and WP Shortcodes into Markdown.
Uses [BeautifulSoup 4](https://pypi.python.org/pypi/beautifulsoup4/4.3.2).
Written for [2buntu](http://2buntu.com).

### Requirements

The following requirements must be met in order to use the markdown converter:

 - [Python 3](https://www.python.org)
 - [PyQt 5](http://www.riverbankcomputing.co.uk/software/pyqt/download5)
 - [BeautifulSoup 4](http://www.crummy.com/software/BeautifulSoup/)

### Installation

**Via `apt-get`**

	$ sudo apt-get install python3-pyqt5 python3-bs4

### Running the script

Once installed, the script can be run as follows:

    2bconverter

In the future, the application will accept a command-line parameter that specifies a file to convert.
