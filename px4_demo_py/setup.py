from setuptools import find_packages
from setuptools import setup

package_name = 'px4_demo_py'

setup(
    name=package_name,
    version='0.1.3',
    packages=[package_name],
    data_files=[
        ('share/ament_index/resource_index/packages',
            ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),
    ],
    install_requires=['setuptools'],
    zip_safe=True,
    author='Beniamino Pozzan',
    author_email='beniamino.pozzan@gmail.com',
    maintainer='Beniamino Pozzan',
    maintainer_email='beniamino.pozzan@gmail.com',
    keywords=['ROS','PX4'],
    description=(
        'Python demo nodes for interfacing with PX4'
    ),
    license='BSD 3-Clause',
    tests_require=['pytest'],
    entry_points={
        'console_scripts': [
            'offboard_example = px4_demo_py.offboard_control:main'
        ],
    },
)