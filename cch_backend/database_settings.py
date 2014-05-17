DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2', # Add 'postgresql_psycopg2', 'mysql', 'sqlite3' or 'oracle'.
        'NAME': 'cch_database',                      # Or path to database file if using sqlite3.
        'USER': 'cch_user',
        'PASSWORD': 'cch_user_password',
        'HOST': 'localhost',
        'PORT': '',                      # Set to empty string for default.
    }
}