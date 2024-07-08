# Generated by Django 5.0.6 on 2024-07-07 17:50

from django.db import migrations, models
from django.contrib.auth.hashers import make_password

def add_groups(apps, schema_editor):
    User = apps.get_model('myapp', 'User')
    Group = apps.get_model('myapp', 'Group')

    # Assumes users with specified emails already exist
    stu = User.objects.get(EmailAddress="stu@stu.com")
    cord = User.objects.get(EmailAddress="cord@cord.com")
    cli = User.objects.get(EmailAddress="cli@cli.com")
    admin = User.objects.get(EmailAddress="admin@admin.com")
    tut = User.objects.get(EmailAddress="tut@tut.com")

    # Creating groups
    group1 = Group.objects.create(GroupName='Group 1', GroupDescription='Description for Group 1', CreatedBy=stu)
    group2 = Group.objects.create(GroupName='Group 2', GroupDescription='Description for Group 2', CreatedBy=cord)
    group3 = Group.objects.create(GroupName='Group 3', GroupDescription='Description for Group 3', CreatedBy=cli)
    group4 = Group.objects.create(GroupName='Group 4', GroupDescription='Description for Group 4', CreatedBy=admin)
    group5 = Group.objects.create(GroupName='Group 5', GroupDescription='Description for Group 5', CreatedBy=tut)

    group1.save()
    group2.save()
    group3.save()
    group4.save()
    group5.save()

class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0008_remove_userpreferenceslink_projectid_and_more'),
    ]

    operations = [
        migrations.RunPython(add_groups),
    ]
