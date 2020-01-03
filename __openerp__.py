{
    # Theme information
    'name': "Tutorial theme",
    'description': """
        Tutorial de creación de temas.
    """,
    'category': 'Theme/Creative',
    'version': '1.0',
    'depends': ['website'],

    # templates
    'data': [
        'views/options.xml',
        'views/snippets.xml',
        'views/layout.xml',
        'views/pages.xml',
        'views/assets.xml',
    ],
    
    'js': ['static/src/js/tutorial_editor.js'],

    # demo pages
    'demo': [
        'demo/pages.xml',
    ],

    # Your information
    'author': "Quadit",
    'website': "https://www.quadit.io",
}