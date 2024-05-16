from setuptools import setup, find_packages

setup(
    name='flappybird',
    version='0.1.0',
    packages=find_packages(),
    include_package_data=True,
    install_requires=[
        'pygame',
    ],
    package_data={
        '': ['assets/*.png'],
    },
    description='A Flappy Bird game implemented in Pygame.',
    author='Hizal',
    author_email='your.email@example.com',
    url='https://github.com/Yaekirua/flappybird',  # Change this to your repository URL
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.6',
)
