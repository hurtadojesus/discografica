# -*- coding: utf-8 -*-
{
    'name': 'Gestión de una tienda de discos    ',
    'summary':"Gestión de una tienda de discos",
    'description':"""
    Módulo para la gestión de una tienda de disco.
    Permite gestionar discos, artistas y géneros musicales.Educación.
    """,
    'author': "SGE2023",
    'website': "http://ead.murciaeduca.es",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/14.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'tools',
    'version': '0.2',
    # any module necessary for this one to work correctly
    'depends': ['base'],

    # always loaded
    'data': [
        'security/groups.xml',
        'security/ir.model.access.csv',
        'views/views.xml',
        'views/templates.xml',
        'demo/demo.xml',
    ],
    
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
    # Pendiente de añadir datos de demo así como de data de artistas y estilos musicales.
    # Pendiente de añadir un report Qweb.
    
}
