import frappe
from frappe.model.document import Document
from frappe.utils import today

class Attendance(Document):
    def validate(self):
        # Validate date is not in future
        if self.date > today():
            frappe.throw("Attendance date cannot be in the future!")
