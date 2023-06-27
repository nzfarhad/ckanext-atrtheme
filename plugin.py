# encoding = utf-8
from ckan.common import CKANConfi
import ckan.plugins as plugins
import ckan.plugins.toolkit as toolkit

class AtrthemePlugin(plugins.SingletonPlugin):
    '''Atrtheme theme plugin.'''
    plugins.implements(plugins.IConfigurer)

    # IConfigurer
    def update_config(self, config: CKANConfi):
        '''Update plugin config'''
        toolkit.add_template_directory(config, 'templates')
        #toolkit.add_public_directory(config, 'public')
        #toolkit.add_resource('public', 'ckanext-atrtheme')

# hide social media links

