from setuptools import setup

setup(name='eeai',
      version='0.1',
      description='Affection: Learning Affective Explanations for Real-World Visual Data',
      packages=['eeai'],
      install_requires=['pandas',                        
                        'numpy',
                        'jupyter',
                        'Pillow', 
                        'pyyaml'
                        ],
      python_requires='>=3',
      zip_safe=False)