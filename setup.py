#!/usr/bin/env python

try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

setup(name='apn_dot2tex',
      version='2.11.5',
      description='A Graphviz to LaTeX converter',
      long_description="""\
The purpose of dot2tex is to give graphs generated by the graph layout tool
Graphviz_, a more LaTeX friendly look and feel. This is accomplished by:

- Using native PSTricks_ and `PGF/TikZ`_ commands for drawing arrows,
  edges and nodes.
- Typesetting labels with LaTeX, allowing mathematical notation.
- Using backend specific styles to customize the output.

.. _Graphviz: http://www.graphviz.org/
.. _PSTricks: http://tug.org/PSTricks/main.cgi/
.. _PGF/TikZ: http://www.ctan.org/tex-archive/help/Catalogue/entries/pgf.html
""",
      author='Alexander Puck Neuwirth',
      author_email='alexander@neuwirth-informatik.de',
      url="https://github.com/APN-Pucky/dot2tex",
      py_modules=['apn_dot2tex.dot2tex', 'apn_dot2tex.dotparsing'],
      scripts=['apn_dot2tex/dot2tex'],
      classifiers=[
          'Development Status :: 4 - Beta',
          'Environment :: Console',
          'Intended Audience :: Science/Research',
          'License :: OSI Approved :: MIT License',
          'Natural Language :: English',
          'Operating System :: OS Independent',
          'Programming Language :: Python :: 2',
          'Programming Language :: Python :: 2.7',
          'Programming Language :: Python :: 3',
          'Programming Language :: Python :: 3.5',
          'Programming Language :: Python :: 3.6',
          'Programming Language :: Python :: 3.7',
          'Topic :: Scientific/Engineering :: Visualization',
          'Topic :: Text Processing :: Markup :: LaTeX',
          'Topic :: Utilities',
      ],
      install_requires=['pyparsing'],
      entry_points={
          'console_scripts': [
              'dot2tex = dot2tex.dot2tex:main',
          ]

      }
)
