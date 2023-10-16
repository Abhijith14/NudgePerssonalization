from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager
from django.utils import timezone
# Create your models here.


class CustomerManager(BaseUserManager):
    def create_user(self, Main_Address, Customer_ID, Company_Name, Primary_Contact, Primary_Phone, Customer_Type, Registration_Date, Services_Detail, password=None):
        if not Main_Address:
            raise ValueError("Email Mandatory")

        user = self.model(
            Main_Address=Main_Address,
            Customer_ID=Customer_ID,
            Company_Name=Company_Name,
            Primary_Contact=Primary_Contact,
            Primary_Phone=Primary_Phone,
            Customer_Type=Customer_Type,
            Registration_Date=Registration_Date,
            Services_Detail=Services_Detail,
        )

        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, Main_Address, password, Customer_ID):
        user = self.create_user(
            password=password,
            Main_Address=Main_Address,
            Customer_ID=Customer_ID,
        )

        user.is_admin = True
        user.is_customer = False
        user.is_active = True
        user.is_superuser = True
        user.save(using=self._db)
        return user

class Customer(AbstractBaseUser):
    Customer_ID = models.CharField(max_length=100, unique=True)
    Company_Name = models.CharField(max_length=200, default='') # registter
    Main_Address = models.CharField(max_length=100, unique=True) # registter
    Primary_Contact = models.CharField(max_length=50, default='')
    Primary_Phone = models.CharField(max_length=50, default='') # registter
    Customer_Type = models.CharField(max_length=50, default='')
    Registration_Date = models.DateField(default=timezone.now)
    Services_Detail = models.CharField(max_length=100, default='')
    last_login = models.DateTimeField(verbose_name="last login", auto_now=True)
    is_admin = models.BooleanField(default=False)
    is_customer = models.BooleanField(default=True)
    is_active = models.BooleanField(default=True)
    is_superuser = models.BooleanField(default=False)

    USERNAME_FIELD = 'Main_Address'

    objects = CustomerManager()

    def __str__(self):
        return self.Main_Address

    def has_perm(self, perm, obj=None):
        return self.is_admin

    def has_module_perms(self, app_label):
        return True

    def __str__(self):
        return self.Customer_ID


class LocationIdentifier(models.Model):
    Location_Identifier_ID = models.CharField(max_length=100, primary_key=True)
    Customer_ID = models.ForeignKey(Customer, on_delete=models.CASCADE)
    Branch_Name = models.CharField(max_length=100)
    Branch_Location = models.CharField(max_length=100)
    Specific_Location = models.IntegerField()

    def __str__(self):
        return self.Location_Identifier_ID

class DisplayDetail(models.Model):
    Display_ID = models.CharField(max_length=100, primary_key=True)
    Location_Identifier_ID = models.ForeignKey(LocationIdentifier, on_delete=models.CASCADE)
    #Hub_ID = models.ForeignKey(HubDetail, on_delete=models.CASCADE)
    Display_MAC = models.CharField(max_length=50)
    EPD_No = models.CharField(max_length=20)
    Activation_Date = models.DateField()
    Initial_IP = models.CharField(max_length=50)
    Current_IP = models.CharField(max_length=50)
    Is_Active = models.BooleanField()
    Display_Size = models.CharField(max_length=50)
    EPDs_Nos = models.CharField(max_length=20)
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
        return self.Display_ID

class Messages(models.Model):
    Message_ID = models.CharField(max_length=50, primary_key=True)
    Location_Identifier_ID = models.ForeignKey(LocationIdentifier, on_delete=models.CASCADE)
    Date = models.DateField()
    Time = models.TimeField()
    Age = models.IntegerField()
    Gender = models.CharField(max_length=10)
    Message = models.CharField(max_length=50)
    Message_Parameters = models.CharField(max_length=50)
    Display_ID = models.ForeignKey(DisplayDetail, on_delete=models.CASCADE)
    def __str__(self):
        return self.Message_ID
    

class ViewerDetail(models.Model):
    Viewer_ID = models.CharField(max_length=50, primary_key=True)
    Location_Identifier_ID = models.ForeignKey(LocationIdentifier, on_delete=models.CASCADE) #attribute 2 page
    Gender = models.CharField(max_length=20) #attribute 2 page
    Age = models.IntegerField()#attribute 2 page
    Nationality = models.CharField(max_length=50)#attribute 2 page
    Course = models.CharField(max_length=50)#attribute 2 page
    Accommodation_Type = models.CharField(max_length=50)
    def _str_(self):
        return self.Viewer_ID


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
    FTP_Address = models.CharField(max_length=50, primary_key=True)
    Location_Identifier_ID = models.ForeignKey(LocationIdentifier, on_delete=models.CASCADE)
    Date = models.DateField()
    Time = models.TimeField()
    URL = models.CharField(max_length=100)  # Adjust the max_length as needed

    def __str__(self):
        return self.FTP_Address

class Images(models.Model):
    Image_ID = models.CharField(max_length=50, primary_key=True)
    FTP_Address = models.ForeignKey(FTPAddress, on_delete=models.CASCADE)
    Display_ID = models.ForeignKey(DisplayDetail, on_delete=models.CASCADE)
    Age = models.IntegerField()
    Gender = models.CharField(max_length=50)
    Image_Parameters = models.CharField(max_length=50)
    URL = models.CharField(max_length=100) 
    def __str__(self):
        return self.Image_ID

