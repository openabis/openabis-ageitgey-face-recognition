from distutils.core import setup

setup(
    name='openabis-ageitgey-face-recognition',
    version='0.0.1',
    packages=['openabis_ageitgey_face_recognition'],
    url='https://github.com/newlogic42/openabis-ageitgey-face-recognition',
    license='Apache 2.0',
    author='newlogic42',
    author_email='',
    description='OpenAbis\' plugin for ageitgey/face-recognition ',
    install_requires=[
        'face-recognition',
    ],
    package_data={
        '': ['*'],
    }
)
