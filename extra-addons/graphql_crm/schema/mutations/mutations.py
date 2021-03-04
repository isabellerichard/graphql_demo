# Copyright 2021 Isabelle RICHARD
# License LGPL-3.0 or later (http://www.gnu.org/licenses/lgpl).

import graphene

from odoo import _
from odoo.exceptions import UserError

from ..models.partner import Partner


class CreatePartner(graphene.Mutation):
    class Arguments:
        name = graphene.String(required=True)
        email = graphene.String(required=True)
        is_company = graphene.Boolean()
        raise_after_create = graphene.Boolean()

    Output = Partner

    @staticmethod
    def mutate(
            self, info, name, email, is_company=False,
            raise_after_create=False):
        env = info.context["env"]
        partner = env["res.partner"].create(
            {"name": name, "email": email, "is_company": is_company}
        )
        if raise_after_create:
            raise UserError(_("as requested"))
        return partner


class Mutation(graphene.ObjectType):
    create_partner = CreatePartner.Field(
        description="Documentation of CreatePartner")
