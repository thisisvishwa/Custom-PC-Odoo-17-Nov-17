```python
from odoo import models, fields

class ProductCategory(models.Model):
    _name = 'product.category'
    _description = 'Product Category'

    name = fields.Char('Category Name', required=True)
    description = fields.Text('Description')

class GamingPC(models.Model):
    _name = 'gaming.pc'
    _description = 'Gaming PC'
    _inherit = 'product.category'

    cpu_model = fields.Char('CPU Model', required=True)
    gpu = fields.Char('GPU', required=True)
    ram = fields.Char('RAM', required=True)
    storage_type = fields.Selection([('HDD', 'HDD'), ('SSD', 'SSD'), ('NVMe', 'NVMe')], 'Storage Type', required=True)
    storage_capacity = fields.Integer('Storage Capacity', required=True)

class Laptop(models.Model):
    _name = 'laptop'
    _description = 'Laptop'
    _inherit = 'product.category'

    brand = fields.Char('Brand', required=True)
    processor = fields.Char('Processor', required=True)
    screen_size = fields.Float('Screen Size', required=True)
    gpu = fields.Char('GPU', required=True)

class PCComponent(models.Model):
    _name = 'pc.component'
    _description = 'PC Component'
    _inherit = 'product.category'

    component_type = fields.Selection([('CPU', 'CPU'), ('GPU', 'GPU'), ('Motherboard', 'Motherboard'), ('RAM', 'RAM'), ('Storage', 'Storage'), ('Cooling Solution', 'Cooling Solution'), ('PC Case', 'PC Case')], 'Component Type', required=True)
    specs = fields.Text('Specifications', required=True)

class GamingConsole(models.Model):
    _name = 'gaming.console'
    _description = 'Gaming Console'
    _inherit = 'product.category'

    generation = fields.Char('Generation', required=True)
    accessories = fields.Text('Accessories')
    games = fields.Text('Games')

class Accessory(models.Model):
    _name = 'accessory'
    _description = 'Accessory'
    _inherit = 'product.category'

    accessory_type = fields.Selection([('Monitor', 'Monitor'), ('Keyboard', 'Keyboard'), ('Mouse', 'Mouse'), ('Headset', 'Headset'), ('Controller', 'Controller')], 'Accessory Type', required=True)
    specs = fields.Text('Specifications', required=True)
```