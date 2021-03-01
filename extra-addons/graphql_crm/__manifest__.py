# Copyright 2021 Isabelle RICHARD
# License LGPL-3.0 or later (http://www.gnu.org/licenses/lgpl).

{
    "name": "GraphQL CRM",
    "version": "13.0.1.0.0",
    "license": "LGPL-3",
    "author": "Isabelle RICHARD",
    "website": "https://www.linkedin.com/in/richardisabelle/",
    "description": """
This is just an example of of to implement GraphQL for Odoo.
Inspired by OCA and its module
[graphql_demo](https://github.com/OCA/rest-framework/tree/13.0/graphql_demo)
    """,
    "depends": [
        "graphql_base",
        "crm",
    ],
    "external_dependencies": {"python": ["graphene"]},
    "installable": True,
}
