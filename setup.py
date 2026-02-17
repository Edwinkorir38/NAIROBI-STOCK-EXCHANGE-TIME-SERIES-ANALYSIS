from setuptools import setup, find_packages

setup(
    name='nse_keras_recommender',
    version='0.1.0',
    packages=find_packages(),
    include_package_data=True,
    install_requires=[
        'streamlit>=1.20.0',
        'pandas>=1.5.3',
        'numpy>=1.23.5',
        'keras>=2.12.0',
        'plotly>=5.15.0',
        'tensorflow>=2.12.0',
        'scikit-learn>=1.2.0',
        'joblib>=1.2.0',
         'prophet'
    ],
    entry_points={
        'console_scripts': [
            'nse-recommender = app:main',
        ],
    },
    author='Edwin Korir',
    author_email='ekorir99@gmail.com.com',
    description='Kenyan NSE stock recommender using Keras and Streamlit',
    keywords='nse keras stock streamlit recommender',
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
    ],
)