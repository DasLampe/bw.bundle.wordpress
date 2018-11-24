@metadata_processor
def wordpress_add_php_extension(metadata):
    if node.has_bundle('php-fpm'):
        if 'php-fpm' not in metadata:
            metadata['php-fpm'] = {}
        if 'extensions' not in metadata['php-fpm']:
            metadata['php-fpm']['extensions'] = []
        if 'php-mysql' not in metadata['php-fpm']['extensions']:
            metadata['php-fpm']['extensions'].append('php-mysql')

    return metadata, DONE