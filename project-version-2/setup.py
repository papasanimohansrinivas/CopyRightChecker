from setuptools import setup, find_packages
 
 
 
setup(name='CopyRightChecker',
 
      version='0.0.1',
 
      # url='https://github.com/papasanimohansrinivas/IBM-CopyRightChecker',
      url='https://pypi.python.org/pypi/CopyRightChecker/',
 
      license='MIT',
 
      author='Papasani Mohan',
 
      author_email='papasani.mohansrinivas@gmail.com',
 
      description='AppendCopyRighttoSourceFiles',
 
      packages=find_packages(),
 
      long_description=open('README.txt').read(),
 
      zip_safe=True,
 
      setup_requires=['gitPython'],
      )