from django.db import models

# username, email, password, specilization , description, experience, profile, isAccountUpdated, address

# Create your models here.
class Doctor(models.Model):

    SPECIALIZATION_CHOICES = [
        ("General Physician", "General Physician"),
        ("Cardiologist", "Cardiologist"),
        ("Neurologist", "Neurologist"),
        ("Dermatologist", "Dermatologist"),
        ("Orthopedic", "Orthopedic"),
        ("Pediatrician", "Pediatrician"),
        ("Psychiatrist", "Psychiatrist"),
        ("Dentist", "Dentist"),
        ("Gynecologist", "Gynecologist"),
    ]

    username = models.CharField(max_length=20)
    email = models.EmailField(max_length=100, unique=True)
    password = models.CharField(max_length=100)
    phone = models.CharField(max_length=10, blank=True, null=True) #optional
    specialization = models.CharField(choices=SPECIALIZATION_CHOICES, max_length=20,blank=True, null=True)
    experience = models.PositiveIntegerField(default=0)
    description = models.TextField(blank=True, null=True)
    profile = models.ImageField(upload_to="doctor_profiles", blank=True, null=True, default='doctor_profiles/default.jpg')
    is_account_updated = models.BooleanField(default=False)
    address = models.TextField(blank=True, null=True)
    fees = models.PositiveBigIntegerField(default=0)

    created_at = models.DateTimeField(auto_now_add=True)  # track when added
    updated_at = models.DateTimeField(auto_now=True)      # track last update

    def __str__(self):
        return f"{self.username} ⚒️ ({self.specialization})"

