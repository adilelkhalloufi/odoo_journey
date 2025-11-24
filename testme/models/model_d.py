from odoo import models

# this model is used to test the _log_access = False feature in Odoo models
# to show that no log of create, write, unlink operations are kept in the ir.model.access table
class ModalD(models.Model):
    _name = 'test.model.d'
    _description = 'Modèle D de TestMe'
    _log_access = False

