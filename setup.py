from setuptools import setup

setup(
    name='RedisLive',
    version='0.1',
    description='Visualize your redis instances, analyze query patterns and spikes.',
    url='https://github.com/nkrode/RedisLive',
    author='nkrode',
    author_email='',
    license='MIT',
    packages=['src'],
    install_requires=[
        'argparse==1.2.1',
        'python-dateutil==1.5',
        'redis',
        'tornado==2.1.1'
    ],
    entry_points={
        'redislive': [
            'api=src.api',
            'dataprovider=src.dataprovider'
        ],
        'console_scripts': [
            'redismonitor=src.redis_monitor:main',
            'redislive=redis_live:main'
        ]
    },
    zip_safe=False
)
