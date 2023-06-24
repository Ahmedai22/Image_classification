
import setuptools

setuptools.setup(
    include_package_data=True,
    name='cnnClassifier',
    version='0.1',
    discription='Image classifier',
    author='Ahmed Abdullah',
    author_email='ai22mtech11004@iith.ac.in',
    package_dir= {"":"src"},
    packages=setuptools.find_packages(where='src')

)