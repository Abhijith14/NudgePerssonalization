from django.contrib import admin
from .models import Customer, LocationIdentifier, DisplayDetail, Messages, ViewerDetail, StaffCustomer, FTPAddress, Images

# Register your models here.
admin.site.register(StaffCustomer)

from django.contrib.auth.models import Group

admin.site.unregister(Group)


class CustomerAdmin(admin.ModelAdmin):
    list_display = ('Customer_ID', 'email', 'Company_Name', 'Main_Address', 'Primary_Contact', 'Primary_Phone', 'Customer_Type', 'Registration_Date', 'last_login', 'is_active', 'is_superuser')
    list_filter = ('Customer_Type',)  # Add any filters you want
    ordering = ('Customer_ID',)  # Specify the ordering by Customer_ID

# Register the Customer model with the custom admin class
admin.site.register(Customer, CustomerAdmin)


class LocationIdentifierAdmin(admin.ModelAdmin):
    list_display = ('Location_Identifier_ID', 'DisplayDetails_ID', 'Customer_ID', 'Branch_Name', 'Branch_Location', 'Specific_Location')
    list_filter = ('Customer_ID',)  # Add any filters you want
    ordering = ('Location_Identifier_ID',)  # Specify the ordering by Location_Identifier_ID

# Register the LocationIdentifier model with the custom admin class
admin.site.register(LocationIdentifier, LocationIdentifierAdmin)


class DisplayDetailAdmin(admin.ModelAdmin):
    list_display = ('Display_ID', 'Display_MAC', 'EPD_No', 'Activation_Date', 'Is_Active', 'Last_Message', 'Last_Image')
    # list_filter = ('Location_Identifier_ID__Branch_Name',)  # Add any filters you want
    ordering = ('Display_ID',)  # Specify the ordering by Display_ID

# Register the DisplayDetail model with the custom admin class
admin.site.register(DisplayDetail, DisplayDetailAdmin)


class ViewerDetailModel(admin.ModelAdmin):
    list_display = ('Viewer_ID', 'Location_Identifier_ID', 'Gender', 'Age', 'Nationality', 'Course', 'Accommodation_Type')
    # list_display = ('Viewer_ID','Gender', 'Age', 'Nationality', 'Course', 'Accommodation_Type')
    list_filter = ('Location_Identifier_ID__Branch_Name',)  # Add any filters you want
    ordering = ('Viewer_ID',)  # Specify the ordering by Viewer_ID

# Register the ViewerDetail model with the custom admin class
admin.site.register(ViewerDetail, ViewerDetailModel)


class MessagesAdmin(admin.ModelAdmin):
    list_display = ('Message_ID', 'Age', 'Gender', 'Nationality', 'Course', 'Date', 'Time', 'Message', 'Message_Parameters')
    # list_filter = ('Location_Identifier_ID__Branch_Name',)  # Add any filters you want
    ordering = ('Message_ID',)  # Specify the ordering by Message_ID

# Register the Messages model with the custom admin class
admin.site.register(Messages, MessagesAdmin)


class FTPAddressModel(admin.ModelAdmin):
    list_display = ('FTP_Address', 'Location_Identifier_ID', 'Date', 'Time', 'URL')
    list_filter = ('Location_Identifier_ID__Branch_Name',)  # Add any filters you want
    ordering = ('FTP_Address',)  # Specify the ordering by FTP_Address

# Register the FTPAddress model with the custom admin class
admin.site.register(FTPAddress, FTPAddressModel)


class ImagesModel(admin.ModelAdmin):
    list_display = ('Image_ID', 'FTP_Address', 'Age', 'Gender', 'Nationality', 'Course', 'Image_Parameters')
    list_filter = ('FTP_Address',)  # Add any filters you want
    ordering = ('FTP_Address',)  # Specify the ordering by Image_ID

# Register the Images model with the custom admin class
admin.site.register(Images, ImagesModel)
