from setuptools import find_packages, setup

setup(
    name='netbox-azure',
    version='1.0.0',
    description='Azure integration for NetBox',
    url='https://github.com/dafneb/netbox-plugin-azure',
    author='David Burel',
    author_email='david.burel@burelovi.eu',
    install_requires=[
        'azure-mgmt-resource==23.3.0',
        'azure-identity==1.20.0'
    ],
    packages=find_packages(),
    include_package_data=True,
    zip_safe=False,
)
