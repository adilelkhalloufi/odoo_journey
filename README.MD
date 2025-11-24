# What i learn from Odoo Custom Addons Development
## Configuration Files
- __manifest__.py: This file contains metadata about the module, such as its name,
- version, author, dependencies, and data files to be loaded.
- __init__.py: This file is used to initialize the module and import necessary Python files.
- Other configuration files may include security rules, access control lists, and data files.
- ## Module Structure 
- Different types of models can be created in Odoo, including:
- Transient Models: Used for temporary data storage, such as wizards.
- Abstract Models: Serve as base classes for other models and cannot be instantiated directly.
- Regular Models: Represent standard database tables and can be instantiated.
##  Model Attributes
- _name: Defines the name of the model.
- _description: Provides a human-readable description of the model.
- _inherit: Specifies the parent model(s) from which to inherit fields and methods.
- log_access: A boolean indicating whether to log access to the model's records.
- _fields: A dictionary defining the fields of the model.
- _sql_constraints: A list of SQL constraints to enforce data integrity.
- _methods: A dictionary defining the methods of the model.
## Field Types
- Char: A string field for short text.
- Text: A field for longer text.
- Integer: A field for integer values.
- Float: A field for floating-point numbers.
- Boolean: A field for true/false values.
- Date: A field for date values.
- Datetime: A field for date and time values.
- Many2one: A field representing a many-to-one relationship with another model.
- One2many: A field representing a one-to-many relationship with another model.
- Many2many: A field representing a many-to-many relationship with another model.

 