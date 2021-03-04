# Copyright 2021 Isabelle RICHARD
# License LGPL-3.0 or later (http://www.gnu.org/licenses/lgpl).

import graphene

from odoo.addons.graphql_base import OdooObjectType

from .country import Country


class Partner(OdooObjectType):
    name = graphene.String(required=True)
    street = graphene.String()
    street2 = graphene.String()
    city = graphene.String()
    zip = graphene.String()
    country = graphene.Field(Country)
    email = graphene.String()
    phone = graphene.String()
    is_company = graphene.Boolean(required=True)
    contacts = graphene.List(graphene.NonNull(lambda: Partner), required=True)

    @staticmethod
    def resolve_country(root, info):
        return root.country_id or None

    @staticmethod
    def resolve_contacts(root, info):
        return root.child_ids
