#!/usr/bin/env python
from setuptools import setup, find_packages

setup(
    name="nasa-weather-insights",
    version="1.0.0",
    description="NASA Weather Insights - Weather prediction using NASA data and machine learning",
    author="NASA Space Apps Challenge Team",
    packages=find_packages(),
    install_requires=[
        "Django>=4.2.7",
        "requests>=2.31.0",
        "joblib>=1.3.2",
        "numpy>=1.24.3",
        "pandas>=2.0.3",
        "tensorflow>=2.13.0",
        "scikit-learn>=1.3.0",
        "matplotlib>=3.7.2",
    ],
    python_requires=">=3.8",
)