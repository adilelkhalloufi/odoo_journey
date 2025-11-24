from odoo import models,fields

class Property(models.Model):
  _name = 'testme.property'
  _description = 'TestMe Property Model'

  # Fields
  name = fields.Char()
  description = fields.Char()
  postcode = fields.Char()
  date_available = fields.Date( )
  expected_price = fields.Float( )
  selling_price = fields.Float( )
  bedrooms = fields.Integer()
  living_rooms = fields.Integer()
  facades = fields.Integer()
  garage = fields.Boolean()
  garden = fields.Boolean()
  garden_area = fields.Integer()
  garden_oreintation = fields.Selection([
    ('north', 'North'),
    ('south', 'South'),
    ('east', 'East'),
    ('west', 'West'),
  ])

