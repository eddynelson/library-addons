from odoo import models, fields

class LibraryBook(models.Model):
    _name = 'library.book'
    
    name = fields.Char(string='Name')
    active = fields.Boolean('Is active')
    image = fields.Binary()
    pages = fields.Intenger(string='# Pages')
    isbn = fields.Char(string='ISBN', size=13)
