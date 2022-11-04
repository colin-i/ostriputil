

pkname='ostriputil'

ver='1.0.0'

from setuptools import setup
setup(name=pkname,
	version=ver,
	packages=[pkname],
	#
	entry_points = {
		'console_scripts': [pkname+'='+pkname+'.main:main']
	}
)
