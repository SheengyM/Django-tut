from django.db import models
from django import forms
from datetime import date


# Create your models here!
from django.db import models

class Members(models.Model):
    # Basic information
    Full_Name = models.CharField(max_length=255)
    Email = models.EmailField(max_length=255)  # Changed to EmailField
    AU_ID = models.CharField(max_length=255)
    Private_Code = models.CharField(max_length=255)

    # Personal information
    D_O_B = models.DateField()  # Changed to DateField
    Gender = models.CharField(max_length=10)  # Assuming values like 'Male' or 'Female'
    Nationality = models.CharField(max_length=255)
    Full_Address = models.TextField()  # Changed to TextField for longer addresses
    Phone_Number = models.CharField(max_length=15)  # Adjust length as needed

    # Traveller information
    Travel_Interests = models.TextField()  # Changed to TextField
    Preferred_Travel_Destination = models.CharField(max_length=255)
    Travel_Budget_Range = models.CharField(max_length=50)  # Adjust length as needed

    # Travel History
    Past_Trips = models.TextField()  # Changed to TextField
    Wishlist_For_Future_Plans = models.TextField()  # Changed to TextField

    # Accessibility requirements or needs
    Any_Special_Accommodations_or_Accessibility_Requirements = models.TextField()  # Changed to TextField

    # Language preference
    Preferred_Language_for_App_Content = models.CharField(max_length=50)
    Language_proficiency_Level = models.CharField(max_length=20)

    # Social Media Integration
    Social_Media_Platform = models.CharField(max_length=255)

    # Notification preferences
    Email_To_Receive_Notifications = models.EmailField()  # Changed to EmailField

    # Privacy and Security Preferences
    Public_or_Private_Account = models.BooleanField(default=True)  # Changed to BooleanField
    Two_Factor_Authentication = models.BooleanField(default=False)  # On/off button for 2FA

    # Preference and Settings customization
    App_Theme = models.CharField(max_length=10)  # 'dark' or 'light' theme
    Notification_and_Sound_Preference = models.BooleanField(default=True)  # On/off button
    Trip_Planning_and_Sharing = models.BooleanField(default=True)  # On/off button

    # Additional Information
    About_Me = models.TextField()  # Changed to TextField
    Emergency_Contact_Name = models.CharField(max_length=255)
    Emergency_Contact_Phone_Number = models.CharField(max_length=15)  # Adjust length as needed

    # Legal and Compliance
    Consent_to_Terms_And_Conditions = models.BooleanField(default=False)  # On/off button
    Data_Usage_And_Privacy_Policy_Acceptance = models.BooleanField(default=False)  # On/off button

    def __str__(self):
        return self.Full_Name

#class member(models.Model):
    #Basic information
 # Full_Name = models.CharField(max_length=255)
  #Email = models.CharField(max_length=255)
  #AU_ID = models.CharField(max_length=255)
  #Private_Code = models.CharField(max_length=255)
  #Personal information
#  D_O_B = models.CharField(max_length=255)
 # Gender = models.CharField(max_length=255)
  #Nationality = models.CharField(max_length=255)
#  Full_Address = models.CharField(max_length=255)
 # Phone_Number = models.CharField(max_length=255)
  #Traveller information
  #Travel_Interests = models.CharField(max_length=255)
#  Preferred_Travel_Destination = models.CharField(max_length=255)
 # Travel_Budget_Range = models.CharField(max_length=255)
  #Travel History
  #Past_Trips = models.CharField(max_length=255)
#  Wishlist_For_Future_Plans = models.CharField(max_length=255)
  #Accessibility requirements or needs
 # Any_Special_Accommodations_or_Accessibility_Requirements = models.CharField(max_length=255)
  #language preference
  #Preferred_Language_for_App_Content = models.CharField(max_length=255)
#  Language_proficiency_Level = models.CharField(max_length=255)
  #Social Media Intergration
 # Social_Media_Platform = models.CharField(max_length=255)
  #notification preferences
  #Email_To_Receive_Notifications = models.CharField(max_length=255)
  #Privacy and Security Preferences
#  Public_or_Private_Account = models.CharField(max_length=255)
  #Two factor authentication = models.CharField(max_length=255)
  #Preference and Settings customization
 # App_Theme = models.CharField(max_length=255)
  #Notification_and_Sound_Preference = models.CharField(max_length=255)
  #Additional Information
#  About_Me = models.CharField(max_length=255)
 # Emergency_Contact_Name = models.CharField(max_length=255)
  #Emergency_Contact_Full_Name = models.CharField(max_length=255)
  #Legal and Compliance
#  Consent_to_Terms_And_Conditions = models.CharField(max_length=255)
 # Data_Usage_And_privacy_Policy_Acceptance = models.CharField(max_length=255)

 