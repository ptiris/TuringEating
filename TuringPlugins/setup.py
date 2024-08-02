import os
from setuptools import setup, find_packages


setup(
    name='mkdocs-turing-plugins',
    version='0.0.0',
    author='ZJU Turing',
    description='A MkDocs plugin used in TuringEating',
    python_requires='>=3.5',
    install_requires=[
        'mkdocs',
        'GitPython'
    ],
    entry_points={
        'mkdocs.plugins': [
            'turing_comments = mkdocs_turing_plugins.comments:CommentsPlugin',
        ]
    },
    include_package_data=True,
    package_data={
        'src': [
            'templates/*.html'
        ]
    }
)