# Install Wordpress via Bundlewrap

## Config
```python
    'wordpress': {
        'root': '/var/www/wordpress',
        'version': '4.9.7',
        'sha256sum': '8514274c5d5b27f8d7c5fb39947d8afc947396940a8a4daffd4fb56c8bbf3b69',
        'db': {
            'host': 'localhost',
            'user': 'wordpress',
            'db': 'wordpress',
            'password': '[generated]',
        },
    }
```