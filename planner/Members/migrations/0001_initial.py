# Generated by Django 4.2.5 on 2023-10-02 15:12

from django.db import migrations, models



class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Members',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Full_Name', models.CharField(max_length=255)),
                ('Email', models.EmailField(max_length=255)),
                ('AU_ID', models.CharField(max_length=255)),
                ('Private_Code', models.CharField(max_length=255)),
                ('D_O_B', models.DateField()),
                ('Gender', models.CharField(max_length=10)),
                ('Nationality', models.CharField(max_length=255)),
                ('Full_Address', models.TextField()),
                ('Phone_Number', models.CharField(max_length=15)),
                ('Travel_Interests', models.TextField()),
                ('Preferred_Travel_Destination', models.CharField(max_length=255)),
                ('Travel_Budget_Range', models.CharField(max_length=50)),
                ('Past_Trips', models.TextField()),
                ('Wishlist_For_Future_Plans', models.TextField()),
                ('Any_Special_Accommodations_or_Accessibility_Requirements', models.TextField()),
                ('Preferred_Language_for_App_Content', models.CharField(max_length=50)),
                ('Language_proficiency_Level', models.CharField(max_length=20)),
                ('Social_Media_Platform', models.CharField(max_length=255)),
                ('Email_To_Receive_Notifications', models.EmailField(max_length=254)),
                ('Public_or_Private_Account', models.BooleanField(default=True)),
                ('Two_Factor_Authentication', models.BooleanField(default=False)),
                ('App_Theme', models.CharField(max_length=10)),
                ('Notification_and_Sound_Preference', models.BooleanField(default=True)),
                ('Trip_Planning_and_Sharing', models.BooleanField(default=True)),
                ('About_Me', models.TextField()),
                ('Emergency_Contact_Name', models.CharField(max_length=255)),
                ('Emergency_Contact_Phone_Number', models.CharField(max_length=15)),
                ('Consent_to_Terms_And_Conditions', models.BooleanField(default=False)),
                ('Data_Usage_And_Privacy_Policy_Acceptance', models.BooleanField(default=False)),
            ],
        ),
    ]
