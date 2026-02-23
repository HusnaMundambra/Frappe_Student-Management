import frappe
from frappe.model.document import Document

class Enrollement(Document):
    def validate(self):
        # Check if student already enrolled in same course
        existing = frappe.db.exists("Enrollement", {
            "student": self.student,
            "course": self.course,
            "name": ("!=", self.name)
        })
        if existing:
            frappe.throw(f"Student is already enrolled in this course!")
