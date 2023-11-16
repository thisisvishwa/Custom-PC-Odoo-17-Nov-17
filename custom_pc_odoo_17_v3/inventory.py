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
    _inherits = {'product.category': 'category_id'}
    
    cpu_model = fields.Char('CPU Model', required=True)
    gpu = fields.Char('GPU', required=True)
    ram = fields.Integer('RAM', required=True)
    storage_type = fields.Selection([('HDD', 'HDD'), ('SSD', 'SSD'), ('NVMe', 'NVMe')], 'Storage Type', required=True)
    storage_capacity = fields.Integer('Storage Capacity', required=True)
    category_id = fields.Many2one('product.category', 'Category', required=True, ondelete='cascade')

class Laptop(models.Model):
    _name = 'laptop'
    _description = 'Laptop'
    _inherits = {'product.category': 'category_id'}
    
    brand = fields.Char('Brand', required=True)
    processor = fields.Char('Processor', required=True)
    screen_size = fields.Float('Screen Size', required=True)
    gpu = fields.Char('GPU', required=True)
    category_id = fields.Many2one('product.category', 'Category', required=True, ondelete='cascade')

class PCComponent(models.Model):
    _name = 'pc.component'
    _description = 'PC Component'
    _inherits = {'product.category': 'category_id'}
    
    component_type = fields.Selection([('CPU', 'CPU'), ('GPU', 'GPU'), ('Motherboard', 'Motherboard'), ('RAM', 'RAM'), ('Storage', 'Storage'), ('Cooling Solution', 'Cooling Solution'), ('PC Case', 'PC Case')], 'Component Type', required=True)
    specs = fields.Text('Specifications', required=True)
    category_id = fields.Many2one('product.category', 'Category', required=True, ondelete='cascade')

class GamingConsole(models.Model):
    _name = 'gaming.console'
    _description = 'Gaming Console'
    _inherits = {'product.category': 'category_id'}
    
    generation = fields.Char('Generation', required=True)
    accessories = fields.Text('Accessories')
    games = fields.Text('Games')
    category_id = fields.Many2one('product.category', 'Category', required=True, ondelete='cascade')

class Accessory(models.Model):
    _name = 'accessory'
    _description = 'Accessory'
    _inherits = {'product.category': 'category_id'}
    
    accessory_type = fields.Selection([('Monitor', 'Monitor'), ('Keyboard', 'Keyboard'), ('Mouse', 'Mouse'), ('Headset', 'Headset'), ('Controller', 'Controller')], 'Accessory Type', required=True)
    specs = fields.Text('Specifications', required=True)
    category_id = fields.Many2one('product.category', 'Category', required=True, ondelete='cascade')
```