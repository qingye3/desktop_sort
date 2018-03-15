from distutils.core import setup

setup(
    name='desktop_sort',
    version='0.0.1',
    packages=['desktop_sort'],
    url='',
    license='MIT',
    author='Qing Ye',
    author_email='qingye3device@gmail.com',
    description='For automatic file sorting',
    scripts=['sort.py'],
    install_requires=['pyyaml']
)
