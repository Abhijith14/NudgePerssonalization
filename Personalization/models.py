from django.db import models
from django.utils import timezone
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin
# Create your models here.


class CustomerManager(BaseUserManager):
    def create_user(self, email, password=None, **extra_fields):
        if not email:
            raise ValueError('The Email Address field must be set')
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user
    
    def create_superuser(self, email, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        extra_fields.setdefault('is_admin', True)
        extra_fields.setdefault('Customer_Type', 'SuperUser')

        if extra_fields.get('is_staff') is not True:
            raise ValueError('Superuser must have is_staff=True.')
        if extra_fields.get('is_superuser') is not True:
            raise ValueError('Superuser must have is_superuser=True.')

        return self.create_user(email, password, **extra_fields)


class Customer(AbstractBaseUser):
    Customer_ID = models.BigAutoField(primary_key=True)
    Company_Name = models.CharField(max_length=200, default='') # registter
    email = models.EmailField(max_length=50, unique=True, default='')
    Main_Address = models.CharField(max_length=100, default='') # registter
    Primary_Contact = models.CharField(max_length=50, default='')
    Primary_Phone = models.CharField(max_length=50, default='') # registter
    Customer_Type = models.CharField(max_length=50, default='')
    Registration_Date = models.DateField(default=timezone.now)
    Services_Detail = models.CharField(max_length=100, default='abcdef')
    last_login = models.DateTimeField(verbose_name="last login", auto_now=True)
    is_active = models.BooleanField(default=True)
    is_admin = models.BooleanField(default=False)
    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)

    objects = CustomerManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    def __str__(self):
        return str(self.Customer_ID) + ". " + self.email
    
    def has_perm(self , perm , obj = None):
        return self.is_admin

    def has_module_perms(self , app_label ):
        return True


class DisplayDetail(models.Model):
    Display_ID = models.BigAutoField(primary_key=True)
    # Location_Identifier_ID = models.ForeignKey(LocationIdentifier, on_delete=models.CASCADE)
    #Hub_ID = models.ForeignKey(HubDetail, on_delete=models.CASCADE)
    Display_MAC = models.CharField(max_length=50)
    EPD_No = models.CharField(max_length=20)
    Activation_Date = models.DateField()
    Initial_IP = models.CharField(max_length=50)
    Current_IP = models.CharField(max_length=50)
    Is_Active = models.BooleanField()
    Display_Size = models.CharField(max_length=50)
    EPDs_Nos = models.CharField(max_length=20)  # here
    Temp_Sensor = models.BooleanField()
    Humidity_Sensor = models.BooleanField()
    Presence_Sensor = models.BooleanField()
    Light_Sensor = models.BooleanField()
    BLE_Receiver = models.BooleanField()
    Memory_Size = models.CharField(max_length=50)
    LoRa_Comms = models.CharField(max_length=50)
    Wifi_Comms = models.CharField(max_length=50)
    Last_Message = models.CharField(max_length=50)
    Last_Image = models.CharField(max_length=50)

    def __str__(self):
        return str(self.Display_ID)


class LocationIdentifier(models.Model):
    Location_Identifier_ID = models.BigAutoField(primary_key=True)
    Customer_ID = models.ForeignKey(Customer, on_delete=models.CASCADE)
    Branch_Name = models.CharField(max_length=100)
    Branch_Location = models.CharField(max_length=100)
    Specific_Location = models.CharField(max_length=100)
    DisplayDetails_ID = models.ForeignKey(DisplayDetail, on_delete=models.CASCADE, null=True)

    def __str__(self):
        return str(self.Location_Identifier_ID) + ". " + self.Branch_Name


class ViewerDetail(models.Model):
    Viewer_ID = models.BigAutoField(primary_key=True)
    Location_Identifier_ID = models.ForeignKey(LocationIdentifier, on_delete=models.CASCADE) #attribute 2 page
    Gender = models.CharField(max_length=20) #attribute 2 page
    Age = models.IntegerField()#attribute 2 page
    Nationality = models.CharField(max_length=50)#attribute 2 page
    Course = models.CharField(max_length=50)#attribute 2 page
    Accommodation_Type = models.CharField(max_length=50)
    
    def _str_(self):
        return str(self.Viewer_ID)


class Messages(models.Model):
    Message_ID = models.BigAutoField(primary_key=True)
    Age = models.IntegerField(blank=True, null=True)
    Gender = models.CharField(max_length=20, blank=True, null=True)
    Date = models.DateField(default=timezone.now)
    Nationality = models.CharField(max_length=50, blank=True, null=True)
    Course = models.CharField(max_length=50, blank=True, null=True)
    Time = models.TimeField(default=timezone.now)
    Message = models.CharField(max_length=50)
    Message_Parameters = models.CharField(max_length=50, default='20cm x 20cm')

    def __str__(self):
        return str(self.Message_ID)


class StaffCustomer(models.Model):
    User_ID = models.CharField(max_length=100, primary_key=True)
    Location_Identifier_ID = models.ForeignKey(LocationIdentifier, on_delete=models.CASCADE)
    Username = models.CharField(max_length=50)
    Password = models.CharField(max_length=50)
    First_Name = models.CharField(max_length=50)
    Last_Name = models.CharField(max_length=50)
    Email = models.EmailField(max_length=50)
    Address = models.CharField(max_length=50)
    Phone = models.CharField(max_length=11)
    Initial_IP = models.CharField(max_length=50)
    Current_IP = models.CharField(max_length=50)
    Is_Active = models.BooleanField()

    def __str__(self):
        return self.User_ID

class FTPAddress(models.Model):
    FTP_Address = models.BigAutoField(primary_key=True)
    Location_Identifier_ID = models.ForeignKey(LocationIdentifier, on_delete=models.CASCADE)
    Date = models.DateField()
    Time = models.TimeField()
    URL = models.CharField(max_length=100)  # Adjust the max_length as needed

    def __str__(self):
        return str(self.FTP_Address)


class Images(models.Model):
    Image_ID = models.BigAutoField(primary_key=True)
    FTP_Address = models.ForeignKey(FTPAddress, on_delete=models.CASCADE)
    Age = models.IntegerField(blank=True, null=True)
    Gender = models.CharField(max_length=20, blank=True, null=True)
    Nationality = models.CharField(max_length=50, blank=True, null=True)
    Course = models.CharField(max_length=50, blank=True, null=True)
    Image_Parameters = models.CharField(max_length=50)

    def __str__(self):
        return str(self.Image_ID)

