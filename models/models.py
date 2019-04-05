from odoo import models, fields, api
from odoo.exceptions import UserError, ValidationError

class Equipment (models.Model):
    
    _inherit = 'maintenance.equipment.category'
    reigon_no = fields.Integer()
    reference_no = fields.Text()
    Model_no = fields.Integer()
    serial_no = fields.Text()
    no_of_working_hours = fields.Integer()
    well_no = fields.Integer()
    Equipment_location = fields.Many2one('company.locations','location_name')

class company_locations (models.Model):
    _name = 'company.locations'
    location_name = fields.Text()

class maintenance (models.Model):
    
    _inherit = ['maintenance.request']
    maintenance_spare_parts = fields.Many2one('location_inventory','spare_parts')

class location_inventory (models.Model):
    _name = 'location_inventory'
    spare_parts = fields.Text()
    qty_spare_part = fields.Integer()
    inventory_location = fields.Many2one('company.locations','location_name')


    

