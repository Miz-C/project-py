from setuptools import setup, find_packages

with open("README.md", "r") as readme_file:
	readme = readme_file.read()

requirements = ["ipython>=6", "nbformat>=4", "nbconvert>=5", "requests>=2"]

setup(
	name="project-py",
	version="0.0.1",
	author="Chelsea Penner",
	author_email="miz.cpenner@remedizinc.ca",
	description="A test package",
	long_description=readme,
	long_description_content_type="text/markdown",
	url="https://github.com/miz-c/project-py/",
	packages=find_packages(),
	install_requires=requirements,
	classifiers=[
		"Programming Language :: Python :: 3.5",
		"License :: OSI Approved :: GNU Affero General Public License v3.0 (AGPLv3)",
	],
)
