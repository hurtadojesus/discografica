# -*- coding: utf-8 -*-

from odoo import models, fields, api
from odoo.exceptions import ValidationError
import re

class genero(models.Model):
    _name = 'discografica.genre'
    _description = 'discografica.genre'
    name = fields.Char(string='Género',help='Género',required=True)

class artist(models.Model):
    _name = 'discografica.artist'
    _description = 'discografica.artist'

    name = fields.Char(string='Artista/grupo',help='Artista/grupo',required=True)

    genre_ids = fields.Many2many('discografica.genre',ondelete='cascade',required=True,string='Estilos')

class disco(models.Model):
    _name = 'discografica.disc'
    _description = 'discografica.disc'

    def accion_boton(self):
        for record in self:
	        record.write({'qty':0})


    name = fields.Char(string='Título del disco',help='Título',required=True)
    """ Si usamos directamente default=fields.Datetime.now, la fecha se cálcula la primera vez 
            pero no se actualiza cada vez que pulsamos crear. De ahí usar una función"""
    enrollment_date = fields.Datetime(
        string='Fecha de alta',
        default=lambda self: fields.Datetime.now(),
    )
    artist_id = fields.Many2one(string='Grupo/Banda',
        comodel_name='discografica.artist',
        ondelete='set null',
        help='Grupo/Banda')
    '''ondelete admite los valores "restrict", "set null", "cascade"
    '''
    genre_id = fields.Many2one(
        string='Estilo',
        comodel_name='discografica.genre',
        ondelete='restrict',
        help='Estilo'
    )
    year = fields.Char(string='Año',help='Año',size=4)

    cover = fields.Image(max_width=200,max_height=200)
    qty = fields.Integer(string='Cantidad', help='Número de copias disponibles',default=0)
    price = fields.Float(string='Precio', help='Precio')
    format = fields.Selection(string='Formato',help='Formato de disco',
        selection=[('1', 'CD'), ('2', 'DVD'),('3','Vinilo')]
    )
    available = fields.Boolean(
        string='Disponible', help='Disponibilidad de copias',
        compute='_is_available',store=True 
    )
    """available  es un campo calculado que depende de la cantidad de discos en existencia.
        usando store=True, le indicamos que se guarde en base de datos para posibles búsquedas."""    
    @api.depends('qty')
    def _is_available(self):
        for record in self:
            if record.qty > 0:
                record.available = True
            else:
                record.available = False
    """ Esta es una forma de obtener valores de otros modelos del sistema: res.partner, res.currency ...  
    currency_id = fields.Many2one('res.currency','Currency',required=True, readonly=True)
    """  

    """
    Algunas restricciones. 
    Si rellenamos el campo year, que sea con 4 dígitos (aunque no sea año válido)
    Indicamos que el nombre del disco junto al formato sea único.
    """
    @api.constrains('year')
    def _check_year(self):
        regex = re.compile('[0-9]{4}\Z',re.I)
        """ \Z indica que sea fin de palabra 
            re.I indica que ignorecase - aquí sin uso
        """
        for record in self:
            if record.year:
                print(f"REGISTRO:{record.year}")
                if not regex.match(record.year):
                    raise ValidationError('Error. Indique el año con 4 dígitos')
    
    _sql_constraints = [('disco_formato_unico','unique(name,format)','No se puede repetir disco en el mismo formato.' )  ]


    
    
    
    
    
    
