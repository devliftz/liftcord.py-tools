from setuptools import find_packages, setup

packages = [
    'liftcord',
    'liftcord.py_gui',
    'liftcord.py_logger',
    'liftcord.py_mobile',
    'liftcord.py_console',
    'liftcord.py_replit',
    'liftcord.py_replit.templates'
]


setup(
    name="liftcord.py-tools",
    version="2.0.1",
    packages=packages,
    include_package_data=True,
    license="MIT License",
    description="liftcord.py Utils",
    keywords="liftcord.py Utils",
    url="https://github.com/bytebuildz/liftcord.py-tools/",
    author=".drmr",
    author_email="hi@icey.fr",
    classifiers=[
        "Programming Language :: Python",
        "Programming Language :: Python :: 2",
        "Programming Language :: Python :: 2.7",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.5",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
    ]
)