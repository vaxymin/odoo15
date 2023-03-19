from odoo import api, fields, models


class HospitalAppointment(models.Model):
    _name = "hospital.appointment"
    _description = "Hospital Appointment"

    patient_id = fields.Many2one('hospital.patient', string="Patient")
    patient_age = fields.Integer(related='patient_id.age')
    patient_priority = fields.Char(string="Priority", compute='compute_priority')
    pharmacy_line_ids = fields.One2many('appointment.pharmacy.lines', 'appointment_id', string="Pharmacy Lines")

    def compute_priority(self):
        if self.patient_age > 65 or self.patient_age < 13:
            return "High"
        else:
            return "Low"


class AppointmentPharmacyLines(models.Model):
    _name = "appointment.pharmacy.lines"
    _description = "Appointment Pharmacy Lines"

    product_id = fields.Many2one('product.product', required=True)
    price_unit = fields.Float(related='product_id.list_price')
    price_discount = fields.Float(string="Final Price", compute='compute_discount')
    qty = fields.Integer(string="Quantity", default=1)
    appointment_id = fields.Many2one('hospital.appointment', string="Appointment")

    def compute_discount(self):
        return self.price_unit - self.price_unit * 0.1