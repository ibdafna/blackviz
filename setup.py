from setuptools import setup

setup(name='blackviz',
      version='0.1',
      description='A black background-appropriate visualization setting for matplotlib',
      url='https://github.com/ibdafna/blackviz',
      author='Itay Dafna',
      author_email='i.b.dafna@gmail.com',
      license='MIT',
      packages=['blackviz'],
      install_requires=['matplotlib'],
      zip_safe=False)