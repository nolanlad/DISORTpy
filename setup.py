import setuptools #enables develop
from numpy.distutils.core import setup,Extension

setup(name='disort',
      packages=['disort'],
      author='Nolan R. McCarthy',
      description='Model of transmission of light through gasses',
      url='https://github.com/scivision/lowtran',
      ext_modules=[Extension(name='disort',sources=['disort.f'],
                    f2py_options=['--quiet'])],
	  )
