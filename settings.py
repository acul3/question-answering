import os
from dotenv import load_dotenv

print('Loading environment variables...')
load_dotenv(verbose=True)
print('Environment variables loaded')

COLORIZE_CLUSTERS = False
PLOT_CLUSTERING_SPACE = False
ENVIRONMENT = os.environ.get('ENVIRONMENT')
DEBUG = bool(int(os.environ.get('DEBUG', 0)))
PORT = int(os.environ.get('PORT', 7979))
SENTRY_DSN = os.environ.get('SENTRY_DSN')