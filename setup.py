from setuptools import find_packages, setup

with open("requirements.txt", encoding="utf-8") as f:
	install_requires = f.read().strip().split("\n")

# get version from __version__ variable in frappe_tsx/__init__.py
from frappe_tsx import __version__ as version

setup(
	name="frappe_tsx",
	version=version,
	description="Typescript type definition generator for Frappe DocTypes",
	author="DHia A. SHalabi",
	author_email="hi@dhiashalabi.com",
	packages=find_packages(),
	zip_safe=False,
	include_package_data=True,
	install_requires=install_requires,
)
