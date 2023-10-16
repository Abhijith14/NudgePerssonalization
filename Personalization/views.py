
from django.shortcuts import render, redirect
from django.urls import reverse
import urllib.parse
from .models import Customer, ViewerDetail, LocationIdentifier, Messages, Images, DisplayDetail
from django.contrib.auth import authenticate, login, logout
from django.db.models import Q

def home(request):
    if request.user.is_authenticated:
        if request.method == 'POST':
            gender = request.POST.get('gender')
            minage = request.POST.get('min_age')
            maxage = request.POST.get('max_age')
            nationality = request.POST.get('nationality')
            course = request.POST.get('course')
            location = request.POST.get('location')

            # send a get request to data_view with the query parameters
            # Construct the query parameters
            query_params = urllib.parse.urlencode({
                'gender': gender,
                'min_age': minage,
                'max_age': maxage,
                'nationality': nationality,
                'course': course,
                'location': location,
            })

            print(query_params)

            # Get the URL for the data_view view using its name
            data_view_url = reverse('data_view')

            # Redirect to the data_view view with the query parameters
            return redirect(f'{data_view_url}?{query_params}')

        return render(request, 'home.html')
    else:
        return redirect('login')

 
def data_view(request):
    if request.user.is_authenticated:
        if request.method == 'GET':
            gender = request.GET.get('gender')
            minage = request.GET.get('min_age')
            maxage = request.GET.get('max_age')
            nationality = request.GET.get('nationality')
            course = request.GET.get('course')
            location = request.GET.get('location')

            # Create an initial query that matches all objects
            query = Q()

            # Check if each field is not empty and add it to the query
            if gender:
                query &= Q(Gender=gender)
             # Handle age filtering based on minage and maxage
            if minage and maxage:
                query &= Q(Age__range=(minage, maxage))
            elif minage:
                print(minage)
                query &= Q(Age__gte=minage)
            elif maxage:
                query &= Q(Age__lte=maxage)
            if nationality:
                query &= Q(Nationality=nationality)
            if course:
                query &= Q(Course=course)
            if location:
                query &= Q(Location_Identifier_ID__Branch_Location=location)

            print(query)
            # Get ViewerDetail objects that match the query
            viewer_details = ViewerDetail.objects.filter(query)

            # Handle the viewer_details as needed
            print(viewer_details)

            # <WSGIRequest: GET '/data_view/?gender=&min_age=24&max_age=&nationality=&course=&location='>

            getContents = "gender="+gender+"&min_age="+minage+"&max_age="+maxage+"&nationality="+nationality+"&course="+course+"&location="+location

            # Render a template with the filtered data
            return render(request, 'data_template.html', {'viewer_details': viewer_details, 'getContents': getContents})
        else:
            return redirect('home')

    else:
        return redirect('login')



def Message_view(request):
    if request.user.is_authenticated:
        if request.method == 'GET':
            gender = request.GET.get('gender')
            minage = request.GET.get('min_age')
            maxage = request.GET.get('max_age')
            nationality = request.GET.get('nationality')
            course = request.GET.get('course')
            # location = request.GET.get('location')

            # Create an initial query that matches all objects
            query = Q()

            # Check if each field is not empty and add it to the query
            if gender:
                query &= Q(Gender=gender)
             # Handle age filtering based on minage and maxage
            if minage and maxage:
                query &= Q(Age__range=(minage, maxage))
            elif minage:
                print(minage)
                query &= Q(Age__gte=minage)
            elif maxage:
                query &= Q(Age__lte=maxage)
            if nationality:
                query &= Q(Nationality=nationality)
            if course:
                query &= Q(Course=course)
            # if location:
            #     query &= Q(Location_Identifier_ID__Branch_Location=location)

            print(query)

            message_details = Messages.objects.filter(query)

            getContents = "gender="+gender+"&min_age="+minage+"&max_age="+maxage+"&nationality="+nationality+"&course="+course#+"&location="+location

            # Render a template with the filtered data
            return render(request, 'message.html', {'message_details': message_details, 'getContents': getContents})
        else:
            return redirect('home')

    else:
        return redirect('login')


def Image_view(request):
    if request.user.is_authenticated:
        if request.method == 'GET':
            gender = request.GET.get('gender')
            minage = request.GET.get('min_age')
            maxage = request.GET.get('max_age')
            nationality = request.GET.get('nationality')
            course = request.GET.get('course')
            # location = request.GET.get('location')

            # Create an initial query that matches all objects
            query = Q()

            # Check if each field is not empty and add it to the query
            if gender:
                query &= Q(Gender=gender)
             # Handle age filtering based on minage and maxage
            if minage and maxage:
                query &= Q(Age__range=(minage, maxage))
            elif minage:
                print(minage)
                query &= Q(Age__gte=minage)
            elif maxage:
                query &= Q(Age__lte=maxage)
            if nationality:
                query &= Q(Nationality=nationality)
            if course:
                query &= Q(Course=course)
            # if location:
            #     query &= Q(Location_Identifier_ID__Branch_Location=location)

            print(query)
      
            # get the message details with the viewer details

            Image_details = Images.objects.filter(query)

            print(Image_details)

            getContents = "gender="+gender+"&min_age="+minage+"&max_age="+maxage+"&nationality="+nationality+"&course="+course#+"&location="+location

            # Render a template with the filtered data
            return render(request, 'images.html', {'image_details': Image_details, 'getContents': getContents})
        else:
            return redirect('home')

    else:
        return redirect('login')



def login_view(request):
    if request.user.is_authenticated:
        return redirect('home')
    else:
        if request.method == 'POST':
            email_address = request.POST.get('username')
            password = request.POST.get('password')

            user = authenticate(request, email=email_address, password=password)

            if user is not None:
                login(request, user)
                return redirect('home')
            else:
                # Authentication failed
                # You can add an error message here
                print("Authentication failed")
                pass

        return render(request, 'login.html')


def register_view(request):
    if request.user.is_authenticated:
        return redirect('home')
    else:
        if request.method == 'POST':
            company_name = request.POST.get('companyname')
            email_address = request.POST.get('emailaddress')
            phone_number = request.POST.get('phone')
            password = request.POST.get('password')

            print(company_name, email_address, phone_number, password)

            user = Customer.objects.create_user(email_address, password=password)

            user.Company_Name = company_name
            user.Primary_Phone = phone_number
            user.save()

            return redirect('login')

        return render(request, 'register.html')

def logout_view(request):
    logout(request)
    return redirect('login')



def final_view(request):
    if request.user.is_authenticated:

        selected_data =  request.POST.get('selected_data')
        selected_mode = request.POST.get('mode')

        getContents = request.POST.get('getContents').split('&amp;')

        print(getContents)
        
        gender = getContents[0].split("=")[-1]
        minage = getContents[1].split("=")[-1]
        maxage = getContents[2].split("=")[-1]
        nationality = getContents[3].split("=")[-1]
        course = getContents[4].split("=")[-1]


       # Create an initial query that matches all objects
        query = Q()

        # Check if each field is not empty and add it to the query
        if gender:
            query &= Q(Gender=gender)
        
        # Handle age filtering based on minage and maxage
        if minage and maxage:
            query &= Q(Age__range=(minage, maxage))
        elif minage:
            print(minage)
            query &= Q(Age__gte=minage)
        elif maxage:
            query &= Q(Age__lte=maxage)
        if nationality:
            query &= Q(Nationality=nationality)
        if course:
            query &= Q(Course=course)
        
        print(query)

        final_mode = ""

        # Apply the filter to the ViewerDetail table and get the id
        viewerdetails = ViewerDetail.objects.filter(query).values('Viewer_ID')
        print(viewerdetails)

        if selected_mode == "message":
            data_cont = Messages.objects.filter(Message_ID=selected_data).values('Message')[0]['Message']
            data_param = Messages.objects.filter(Message_ID=selected_data).values('Message_Parameters')[0]['Message_Parameters']
            final_mode = "Message"
        
        elif selected_mode == "image":
            data_cont = Images.objects.filter(Image_ID=selected_data).values('FTP_Address__URL')[0]['FTP_Address__URL']
            data_param = Images.objects.filter(Image_ID=selected_data).values('Image_Parameters')[0]['Image_Parameters']
            final_mode = "Image"

        company, branch_name, branch_loc, specific_loc, age, gender, nationality, course, acc, display_mac, epd_no, Activation_date, Initial_IP, Current_IP, Is_Active, Display_Size, EPDs_Nos = [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], []

        for viewer in viewerdetails:
            Vid = viewer['Viewer_ID']
                    
            company.append(ViewerDetail.objects.filter(Viewer_ID=Vid).values('Location_Identifier_ID__Customer_ID__Company_Name')[0]['Location_Identifier_ID__Customer_ID__Company_Name'])
            branch_name.append(ViewerDetail.objects.filter(Viewer_ID=Vid).values('Location_Identifier_ID__Branch_Name')[0]['Location_Identifier_ID__Branch_Name'])
            branch_loc.append(ViewerDetail.objects.filter(Viewer_ID=Vid).values('Location_Identifier_ID__Branch_Location')[0]['Location_Identifier_ID__Branch_Location'])
            specific_loc.append(ViewerDetail.objects.filter(Viewer_ID=Vid).values('Location_Identifier_ID__Specific_Location')[0]['Location_Identifier_ID__Specific_Location'])
            age.append(ViewerDetail.objects.filter(Viewer_ID=Vid).values('Age')[0]['Age'])
            gender.append(ViewerDetail.objects.filter(Viewer_ID=Vid).values('Gender')[0]['Gender'])
            nationality.append(ViewerDetail.objects.filter(Viewer_ID=Vid).values('Nationality')[0]['Nationality'])
            course.append(ViewerDetail.objects.filter(Viewer_ID=Vid).values('Course')[0]['Course'])
            acc.append(ViewerDetail.objects.filter(Viewer_ID=Vid).values('Accommodation_Type')[0]['Accommodation_Type'])

            display_mac.append(ViewerDetail.objects.filter(Viewer_ID=Vid).values('Location_Identifier_ID__DisplayDetails_ID__Display_MAC')[0]['Location_Identifier_ID__DisplayDetails_ID__Display_MAC'])
            epd_no.append(ViewerDetail.objects.filter(Viewer_ID=Vid).values('Location_Identifier_ID__DisplayDetails_ID__EPD_No')[0]['Location_Identifier_ID__DisplayDetails_ID__EPD_No'])
            Activation_date.append(ViewerDetail.objects.filter(Viewer_ID=Vid).values('Location_Identifier_ID__DisplayDetails_ID__Activation_Date')[0]['Location_Identifier_ID__DisplayDetails_ID__Activation_Date'])
            Initial_IP.append(ViewerDetail.objects.filter(Viewer_ID=Vid).values('Location_Identifier_ID__DisplayDetails_ID__Initial_IP')[0]['Location_Identifier_ID__DisplayDetails_ID__Initial_IP'])
            Current_IP.append(ViewerDetail.objects.filter(Viewer_ID=Vid).values('Location_Identifier_ID__DisplayDetails_ID__Current_IP')[0]['Location_Identifier_ID__DisplayDetails_ID__Current_IP'])
            Is_Active.append(ViewerDetail.objects.filter(Viewer_ID=Vid).values('Location_Identifier_ID__DisplayDetails_ID__Is_Active')[0]['Location_Identifier_ID__DisplayDetails_ID__Is_Active'])
            Display_Size.append(ViewerDetail.objects.filter(Viewer_ID=Vid).values('Location_Identifier_ID__DisplayDetails_ID__Display_Size')[0]['Location_Identifier_ID__DisplayDetails_ID__Display_Size'])
            EPDs_Nos.append(ViewerDetail.objects.filter(Viewer_ID=Vid).values('Location_Identifier_ID__DisplayDetails_ID__EPDs_Nos')[0]['Location_Identifier_ID__DisplayDetails_ID__EPDs_Nos'])

        # Create a list of dictionaries with key-value pairs
        data = []

        for i in range(len(viewerdetails)):  # You can use any of your lists for the length since they should have the same length
            data_dict = {
                'company': company[i],
                'branch_name': branch_name[i],
                'branch_loc': branch_loc[i],
                'specific_loc': specific_loc[i],
                'age': age[i],
                'gender': gender[i],
                'nationality': nationality[i],
                'course': course[i],
                'acc': acc[i],
                'data_cont': data_cont,
                'data_param': data_param,
                'display_mac': display_mac[i],
                'epd_no': epd_no[i],
                'Activation_date': Activation_date[i],
                'Initial_IP': Initial_IP[i],
                'Current_IP': Current_IP[i],
                'Is_Active': Is_Active[i],
                'Display_Size': Display_Size[i],
                'EPDs_Nos': EPDs_Nos[i]
            }
            data.append(data_dict)

        print(data)  # Final Result !!

        return render(request, 'final.html', {'final_data':data, 'final_mode':final_mode})
    
    else:
        return redirect('login')


