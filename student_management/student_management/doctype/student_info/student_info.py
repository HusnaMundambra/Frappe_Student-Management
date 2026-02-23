import frappe
from frappe.model.document import Document

class StudentInfo(Document):
    def before_insert(self):
        # Auto generate Student ID
        count = frappe.db.count("Student_Info")
        self.student_id = f"STU-{count + 1:04d}"
        frappe.msgprint(f"Student ID assigned: {self.student_id}")
    
    def validate(self):
        if self.age and self.age < 5:
            frappe.throw("Age cannot be less than 5!")
        if not self.email:
            frappe.throw("Email is required!")
