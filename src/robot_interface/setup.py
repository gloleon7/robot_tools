from setuptools import setup

package_name = 'robot_interface'

setup(
    name=package_name,
    version='0.0.0',
    packages=[package_name],
    data_files=[
        ('share/ament_index/resource_index/packages', ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),
    ],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='gloria leon',
    maintainer_email='leonlagog@gmail.com',
    description='proyecto tools',
    license='Apache License 2.0',
    tests_require=['pytest'],
    entry_points={
        'console_scripts': [
            'robot_control = robot_interface.robot_control:main',
        ],
    },
)

