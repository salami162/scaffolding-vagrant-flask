import os

environment = os.environ.get('APPLICATION_ENV', 'development')
env_config = 'config.%s' % environment