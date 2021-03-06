# Copyright 2019 Creu Blanca
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

from odoo.tests.common import TransactionCase


class TestEquipmentContract(TransactionCase):

    def setUp(self):
        super().setUp()
        self.equipment_id = self.env['maintenance.equipment'].create({
            'name': 'Equipment'
        })
        self.contract = self.env['account.analytic.account'].create({
            'name': 'Contract',
            'equipment_ids': [(4, self.equipment_id.id)]
        })

    def test_equipment_contract(self):
        self.assertEqual(self.equipment_id.contract_count, 1)
        action = self.equipment_id.action_view_contracts()
        self.assertEqual(action['res_id'], self.contract.id)

        self.env['account.analytic.account'].create({
            'name': 'Contract 2',
            'equipment_ids': [(4, self.equipment_id.id)]
        })
        self.assertEqual(self.equipment_id.contract_count, 2)
        action = self.equipment_id.action_view_contracts()
        self.assertIn('domain', action.keys())
