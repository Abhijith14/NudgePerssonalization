import os
import sys
import django 
import csv
# Add your project directory to the Python path
project_dir = r'D:\projects\NudgePerssonalization'  # Use the 'r' prefix
sys.path.append(project_dir)

# Now import your models
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "NudgePerssonalization.settings")
django.setup()

from Personalization.models import Customer, LocationIdentifier, DisplayDetail, Messages, ViewerDetail, StaffCustomer, FTPAddress, Images
from datetime import datetime

import sqlite3

# csv_file = "customer_data.csv"

# with open(csv_file, "r") as file:
#     reader = csv.DictReader(file)
#     for row in reader:
#         print('successs')
#         customer = Customer(
#             Customer_ID=row["Customer_ID"],
#             Company_Name=row["Company_Name"],
#             Main_Address=row["Main_Address"],
#             Primary_Contact=row["Primary_Contact"],
#             Primary_Phone=row["Primary_Phone"],
#             Customer_Type=row["Customer_Type"],
#             Registration_Date=datetime.strptime(row["Registration_Date"], "%Y-%m-%d").date(),
#             Services_Detail=row["Services_Detail"],
#         )
#         customer.save()
# print('successs')



# print(Customer.objects.all())


def LocationIdentifierModel(data):
    for row in data:
        print(row)
        customerid =int(row[1]) + 1
        customer_instance = Customer.objects.get(pk=customerid)
        locationidentifier = LocationIdentifier(
            Location_Identifier_ID=int(row[0]),
            Customer_ID = customer_instance,
            Branch_Name=row[2],
            Branch_Location=row[3],
            Specific_Location=row[4],
        )
        locationidentifier.save()


def DisplayDetailModel(data):
    for row in data:
        print(row)
        activeBool, tempbool, humiditybool, presencebool, lightbool, blebool = False, False, False, False, False, False
        locationidentifierid=int(row[1])
        locationidentifier_instance = LocationIdentifier.objects.get(pk=locationidentifierid)
        activeBool = row[8]
        tempbool = row[11]
        humiditybool = row[12]
        presencebool = row[13]
        lightbool = row[14]
        blebool = row[15]

        if (row[8] == 'True'):
            activeBool = 1
        elif (row[8] == 'False'):
            activeBool = 0

        if (row[11] == 'True'):
            tempbool = 1
        elif (row[11] == 'False'):
            tempbool = 0

        if (row[12] == 'True'):
            humiditybool = 1
        elif (row[12] == 'False'):
            humiditybool = 0

        if (row[13] == 'True'):
            presencebool = 1
        elif (row[13] == 'False'):
            presencebool = 0

        if (row[14] == 'True'):
            lightbool = 1
        elif (row[14] == 'False'):
            lightbool = 0

        if (row[15] == 'True'):
            blebool = 1
        elif (row[15] == 'False'):
            blebool = 0

        displaydetail = DisplayDetail(
            Display_ID=int(row[0]),
            Location_Identifier_ID=locationidentifier_instance,
            Display_MAC = row[3],
            EPD_No = row[4],
            Activation_Date = datetime.strptime(row[5], "%Y-%m-%d").date(),
            Initial_IP = row[6],
            Current_IP = row[7],
            Is_Active = int(activeBool),
            Display_Size = row[9],
            EPDs_Nos = row[10],
            Temp_Sensor = int(tempbool),
            Humidity_Sensor = int(humiditybool),
            Presence_Sensor = int(presencebool),
            Light_Sensor = int(lightbool),
            BLE_Receiver = int(blebool),
            Memory_Size = row[16],
            LoRa_Comms = row[17],
            Wifi_Comms = row[18],
            Last_Message = row[19],
            Last_Image = row[20],
        )
        displaydetail.save()



def MessageModel(data):
    for row in data:
        print(row)
        locationidentifierid=int(row[1])
        locationidentifier_instance = LocationIdentifier.objects.get(pk=locationidentifierid)
        displayid = int(row[8])
        displaydetail_instance = DisplayDetail.objects.get(pk=displayid)
        message = Messages(
            Message_ID = int(row[0]),
            Location_Identifier_ID = locationidentifier_instance,
            Date = datetime.strptime(row[2], "%Y-%m-%d").date(),
            Time = datetime.strptime(row[3], "%H:%M").time(),
            Age = int(row[4]),
            Gender = row[5],
            Message = row[6],
            Message_Parameters = row[7],
            Display_ID = displaydetail_instance,
        )
        message.save()


def ViewerDataModel(data):
    for row in data:
        print(row)
        locationidentifier = LocationIdentifier.objects.get(pk=int(row[1]))
        viewerdetail = ViewerDetail(
            Viewer_ID = int(row[0]),
            Location_Identifier_ID = locationidentifier,
            Gender = row[2],
            Age = int(row[3]),
            Nationality = row[4],
            Course = row[5],
            Accommodation_Type = row[6],
        )
        viewerdetail.save()


def FTPModel(data):
    for row in data:
        print(row)
        locationidentifier = LocationIdentifier.objects.get(pk=int(row[1]))
        ftpaddress = FTPAddress(
            FTP_Address = int(row[0]),
            Location_Identifier_ID = locationidentifier,
            Date = datetime.strptime(row[2], "%Y-%m-%d").date(),
            Time = datetime.strptime(row[3], "%H:%M").time(),
            URL = row[4],
        )

        ftpaddress.save()


def ImageModel(data):
    for row in data:
        print(row)
        ftpadd = FTPAddress.objects.get(pk=int(row[1]))
        displaydetail = DisplayDetail.objects.get(pk=int(row[2]))
        image = Images(
            Image_ID = int(row[0]),
            FTP_Address = ftpadd,
            Display_ID = displaydetail,
            Age = int(row[3]),
            Gender = row[4],
            Image_Parameters = row[5],
            URL = row[6],
        )
        image.save()



# Step 1: Connect to the SQLite database
conn = sqlite3.connect("test_database.db")

# Step 2: Create a cursor object
cursor = conn.cursor()

# Step 3: Execute a SQL query to select data from the table
cursor.execute("SELECT * FROM Messages")

# Execute a SQL query to retrieve table names
# cursor.execute("SELECT name FROM sqlite_master WHERE type='table';")

# Step 4: Fetch and print the data
data = cursor.fetchall()

# LocationIdentifierModel(data)
# DisplayDetailModel(data)
# MessageModel(data)
# ViewerDataModel(data)
# FTPModel(data)
# ImageModel(data)

for row in data:
    print(row)

# Step 5: Close the database connection when you're done
conn.close()