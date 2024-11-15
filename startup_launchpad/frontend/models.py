from django.db import models

class StudentReport(models.Model):
    student_id = models.CharField(max_length=10)
    title = models.CharField(max_length=50)
    timestamp = models.DateTimeField(auto_now_add=True)
    strengths = models.JSONField()
    weakness = models.JSONField()
    opportunity = models.JSONField()
    threat = models.JSONField()
    improvements = models.JSONField(null=True, blank=True)
    addons = models.JSONField(null=True, blank=True)

    def __str__(self):
        return self.title

    class Meta:
        db_table = 'swotanalysis'  # Specify custom table name here
