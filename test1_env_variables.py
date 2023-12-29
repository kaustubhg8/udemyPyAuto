# import os
from os import environ
print(environ.get('NEXUS_ENVIRONMENT'))
environ.pop('NEXUS_ENVIRONMENT')
print(environ.get('NEXUS_ENVIRONMENT'))
environ['NEXUS_ENVIRONMENT'] = 'dev'
print(environ.get('NEXUS_ENVIRONMENT'))

# environ['Kaustubh'] = 'garud'
