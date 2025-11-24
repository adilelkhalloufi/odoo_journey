# python
{
    "name": "TestMe",
    "version": "1.0.0",
    "summary": "Module de test pour démonstration",
    "description": """
TestMe — module d'exemple contenant des modèles, vues et données de démonstration.
""",
    "author": "Adev",
    "website": "https://adev.ma",
    "category": "Tools",
    "license": "LGPL-3",
    "depends": [
        "base",
    ],
    "data": [
      'security/ir.model.access.csv',
      'views/base_menu.xml',
      'views/property_view.xml',
    ],

    "qweb": [
        # fichiers qweb si nécessaire
    ],
    "installable": True,
    "application": True,

}
