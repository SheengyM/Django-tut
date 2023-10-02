from datetime import date
from Members.models import Members  # Import the Members model
import os
import django

# Set the DJANGO_SETTINGS_MODULE environment variable to your project's settings
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "planner.settings")  # Replace "your_project_name" with your actual project name

# Initialize Django
django.setup()


# Create an instance of the Members class
member = Members(
    Full_Name='Smish',
    Email='sm3965a@american.edu',
    AU_ID='5393965',
    Private_Code='Password123',
    D_O_B=date(1997, 12, 6),  # Use the date function to create a date object
    Gender='Male',
    Nationality='Zimbabwe',  # Fixed the capitalization
    Full_Address='1204 Lawler dr USA',
    Phone_Number='+2409784399',
    Travel_Interests='DMV Only',
    Preferred_Travel_Destination='Washington DC',
    Travel_Budget_Range='70 to 250',
    Past_Trips='Virginia',
    Wishlist_For_Future_Plans='Maryland',
    Any_Special_Accommodations_or_Accessibility_Requirements='No',
    Preferred_Language_for_App_Content='English',
    Language_proficiency_Level='99',
    Social_Media_Platform='SheengyM',
    Email_To_Receive_Notifications='wefixcmdshft3@gmail.com',
    Public_or_Private_Account=True,
    Two_Factor_Authentication=False,
    App_Theme='dark',
    Notification_and_Sound_Preference=True,
    Trip_Planning_and_Sharing=True,
    About_Me='Introvert student',
    Emergency_Contact_Name='Mwofer Sheengy',
    Emergency_Contact_Phone_Number='2402175725',
    Consent_to_Terms_And_Conditions=True,
    Data_Usage_And_Privacy_Policy_Acceptance=True
)

# Save the instance to the database
member.save()



