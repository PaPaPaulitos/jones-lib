from setuptools import setup, find_packages

with open("README.md", "r") as arq:
    readme = arq.read()

setup(
    name='jones_lib',
    version='0.0.1',
    license='MIT License',
    author='Paulo Ricardo Mesquita',
    long_description=readme,
    long_description_content_type="text/markdown",
    author_email='pauloricardomrs2002@gmail.com',
    keywords='jones, stalking, jones lib, jones-lib',
    description=u'Explore Breached Data',
    packages=find_packages(),
    install_requires=[
        'colorama==0.4.6',
        'et-xmlfile==1.1.0',
        'iniconfig==2.0.0',
        'numpy==1.26.2',
        'openpyxl==3.1.2',
        'packaging==23.2',
        'pandas==2.1.4',
        'pluggy==1.3.0',
        'python-dateutil==2.8.2',
        'pytz==2023.3.post1',
        'six==1.16.0',
        'tzdata==2023.3'
    ],
)