from django.db import models

class Candidate(models.Model):
    STATUS_CHOICES = [
        ('selected', 'Selected'),
        ('not_selected', 'Not Selected'),
        ('hold', 'Hold'),
    ]

    stuid = models.CharField(max_length=20, unique=True)  # Temporary student ID
    name = models.CharField(max_length=100)
    email = models.EmailField()
    phone = models.CharField(max_length=15)
    date_of_interview = models.DateField()
    round1_status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='hold')
    round2_status = models.CharField(max_length=20, choices=[('selected', 'Selected'), ('not_selected', 'Not Selected')], blank=True, null=True)
    remarks = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.name
