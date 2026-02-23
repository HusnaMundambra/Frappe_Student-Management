import frappe
from frappe.model.document import Document

class Marks(Document):
    def validate(self):
        if self.marks_obtained > self.total_marks:
            frappe.throw("Marks obtained cannot be greater than total marks!")
        
        percentage = (self.marks_obtained / self.total_marks) * 100
        
        if percentage >= 90:
            self.grade = "A+"
        elif percentage >= 80:
            self.grade = "A"
        elif percentage >= 70:
            self.grade = "B"
        elif percentage >= 60:
            self.grade = "C"
        elif percentage >= 50:
            self.grade = "D"
        else:
            self.grade = "F"
        
        frappe.msgprint(f"Grade: {self.grade} ({percentage:.1f}%)")
