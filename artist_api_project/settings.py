# artist_api_project/settings.py
INSTALLED_APPS = [
    # ...
    'rest_framework',
    'artist_api',
]
DEBUG = True 
REST_FRAMEWORK = {
    'DEFAULT_AUTHENTICATION_CLASSES': [
        'rest_framework.authentication.TokenAuthentication',
    ],
    'DEFAULT_PERMISSION_CLASSES': [
        'rest_framework.permissions.IsAuthenticated',
    ],
}