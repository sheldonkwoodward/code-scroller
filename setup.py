# sheldon woodward
# 4/24/18

from setuptools import setup

setup(name='code_scroller',
      version='1.0.0',
      packages=['code_scroller'],
      entry_points={
          'console_scripts': [
              'code_scroller = code_scroller.__main__:main'
          ]
      },
      )
