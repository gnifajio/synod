import setuptools

with open('README_EN.md', 'r') as fh:
	long_description = fh.read()

setuptools.setup(
	name = "synod",
	version = "1.1",
	author = "Gnifajio None",
	author_email = "gnifajio@gmail.com",
	description = "Python dictionary with synonyms",
	long_description = long_description,
	long_description_content_type = "text/markdown",
	url = "https://github.com/gnifajio/synod",
	packages = setuptools.find_packages(),
	# install_requires = requirements,
	classifiers = [
		"Programming Language :: Python :: 3.10",
		"License :: OSI Approved :: MIT License",
		"Operating System :: OS Independent",
	],
	python_requires = '>=3.7',
)