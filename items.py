global node

wordpress = node.metadata.get('wordpress', {})
defaultRoot = '/var/www/wordpress'

directories = {
    '{}'.format(wordpress.get('root', defaultRoot)): {
    }
}

downloads = {
    '{}/wp.tar.gz'.format(wordpress.get('root', defaultRoot)): {
        'url': 'https://wordpress.org/wordpress-{}.tar.gz'\
            .format(wordpress.get('version', '4.9.7')),
        'sha256': wordpress.get('sha256sum',
            '8514274c5d5b27f8d7c5fb39947d8afc947396940a8a4daffd4fb56c8bbf3b69'),
        'needs': [
            'directory:{}'.format(wordpress.get('root', defaultRoot)),
        ],
    },
}

actions = {
    'unpack_wordpress': {
        'command': 'cd {} && ' \
                   'tar xfvz wp.tar.gz'.format(
                        wordpress.get('root', defaultRoot)),
        'unless': 'test -d {}/wordpress',
        'needs': [
            'download:{}/wp.tar.gz'.format(wordpress.get('root', defaultRoot)),
        ],
    }
}

files = {
    '{}/wordpress/wp-config.php'.format(wordpress.get('root', defaultRoot)): {
        'source': 'wp-config.php',
        'content_type': 'mako',
        'context': {
            'mysql_user': node.metadata.get('wordpress', {}).get('db', {}) \
                .get('user', 'wordpress'),
            'mysql_db': node.metadata.get('wordpress', {}).get('db', {}) \
                .get('db', 'wordpress'),
            'mysql_host': node.metadata.get('wordpress', {}).get('db', {}) \
                .get('host', 'localhost'),
            'mysql_password': node.metadata.get('wordpress', {}).get('db', {}). \
                get('password', repo.vault.password_for("mysql_{}_user_{}" \
                .format(
                node.metadata.get('wordpress', {}).get('db', {}) \
                    .get('db', 'wordpress'),
                node.name))),
        },
        'needs': [
            'action:unpack_wordpress',
        ],
    },
}