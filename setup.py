from setuptools import setup, find_packages

with open("requirements.txt") as f:
	install_requires = f.read().strip().split("\n")

# get version from __version__ variable in fabitive/__init__.py
from fabitive import __version__ as version

setup(
	name="fabitive",
	version=version,
	description="Personalizacion de ERPNEXT para Fabitive",
	author="Fabitive",
	author_email="info@fabitive.es",
	packages=find_packages(),
	zip_safe=False,
	include_package_data=True,
	install_requires=install_requires
)
