import os
import django

# Set the DJANGO_SETTINGS_MODULE environment variable
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "NudgePerssonalization.settings")
django.setup()

# Now you can import and use your Django models
from Personalization.models import Customer

def main():
    all_customers = Customer.objects.all()
    for customer in all_customers:
        print(customer.Customer_ID, customer.Company_Name, customer.Primary_Contact)

main()
