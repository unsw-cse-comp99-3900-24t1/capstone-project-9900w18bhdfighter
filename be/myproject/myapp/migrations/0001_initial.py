import django.db.models.deletion
import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('contenttypes', '0002_remove_content_type_name'),
    ]

    operations = [
        migrations.CreateModel(
            name='Area',
            fields=[
                ('AreaID', models.AutoField(primary_key=True, serialize=False)),
                ('AreaName', models.CharField(max_length=255, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('ContactID', models.AutoField(primary_key=True, serialize=False)),
                ('IsFixed', models.BooleanField(default=False)),
            ],
        ),
        migrations.CreateModel(
            name='Group',
            fields=[
                ('GroupID', models.AutoField(primary_key=True, serialize=False)),
                ('GroupName', models.CharField(max_length=255, unique=True)),
                ('GroupDescription', models.TextField()),
                ('MaxMemberNumber', models.IntegerField(default=1)),
            ],
        ),
        migrations.CreateModel(
            name='GroupProjectsLink',
            fields=[
                ('GroupProjectsLinkID', models.AutoField(primary_key=True, serialize=False)),
                ('GroupID', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='myapp.group')),
            ],
        ),
        migrations.CreateModel(
            name='Notification',
            fields=[
                ('NotificationID', models.AutoField(primary_key=True, serialize=False)),
                ('sender_object_id', models.PositiveIntegerField(default=1)),
                ('Type', models.CharField(max_length=255)),
                ('Message', models.TextField()),
                ('AdditionalData', models.JSONField(blank=True, null=True)),
                ('CreatedAt', models.DateTimeField(default=django.utils.timezone.now)),
                ('sender_content_type', models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='contenttypes.contenttype')),
            ],
        ),
        migrations.CreateModel(
            name='NotificationReceiver',
            fields=[
                ('NotificationReceiverID', models.AutoField(primary_key=True, serialize=False)),
                ('IsRead', models.BooleanField(default=False)),
                ('Notification', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='myapp.notification')),
            ],
        ),
        migrations.CreateModel(
            name='Project',
            fields=[
                ('ProjectID', models.AutoField(primary_key=True, serialize=False)),
                ('ProjectName', models.CharField(max_length=255)),
                ('ProjectDescription', models.TextField()),
                ('ProjectOwner', models.CharField(max_length=255)),
                ('MaxNumOfGroup', models.IntegerField(default=1)),
                ('Groups', models.ManyToManyField(through='myapp.GroupProjectsLink', to='myapp.group')),
            ],
        ),
        migrations.AddField(
            model_name='groupprojectslink',
            name='ProjectID',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='myapp.project'),
        ),
        migrations.CreateModel(
            name='GroupPreference',
            fields=[
                ('PreferenceID', models.AutoField(primary_key=True, serialize=False)),
                ('Rank', models.IntegerField()),
                ('Group', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='myapp.group')),
                ('Preference', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='myapp.project')),
            ],
        ),
        migrations.AddField(
            model_name='group',
            name='Preferences',
            field=models.ManyToManyField(through='myapp.GroupPreference', to='myapp.project'),
        ),
        migrations.CreateModel(
            name='Skill',
            fields=[
                ('SkillID', models.AutoField(primary_key=True, serialize=False)),
                ('SkillName', models.CharField(max_length=255)),
                ('Area', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='myapp.area')),
            ],
        ),
        migrations.CreateModel(
            name='SkillProject',
            fields=[
                ('SkillProjectID', models.AutoField(primary_key=True, serialize=False)),
                ('Project', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='myapp.project')),
                ('Skill', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='myapp.skill')),
            ],
        ),
        migrations.CreateModel(
            name='StudentArea',
            fields=[
                ('StudentAreaID', models.AutoField(primary_key=True, serialize=False)),
                ('Area', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='myapp.area')),
            ],
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('UserID', models.AutoField(primary_key=True, serialize=False)),
                ('FirstName', models.CharField(max_length=50)),
                ('LastName', models.CharField(max_length=50)),
                ('EmailAddress', models.CharField(max_length=255, unique=True)),
                ('Passwd', models.CharField(max_length=255)),
                ('UserRole', models.IntegerField(blank=True, choices=[(1, 'student'), (2, 'client'), (3, 'tut'), (4, 'cord'), (5, 'admin')], default=1, null=True)),
                ('UserInformation', models.CharField(max_length=255)),
                ('Areas', models.ManyToManyField(through='myapp.StudentArea', to='myapp.area')),
                ('Contacts', models.ManyToManyField(through='myapp.Contact', to='myapp.user')),
                ('Notifications', models.ManyToManyField(through='myapp.NotificationReceiver', to='myapp.notification')),
            ],
        ),
        migrations.AddField(
            model_name='studentarea',
            name='User',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='myapp.user'),
        ),
        migrations.AddField(
            model_name='project',
            name='CreatedBy',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='created_projects', to='myapp.user'),
        ),
        migrations.AddField(
            model_name='notificationreceiver',
            name='ReceiverUser',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='received_notifications', to='myapp.user'),
        ),
        migrations.CreateModel(
            name='Message',
            fields=[
                ('MessageID', models.AutoField(primary_key=True, serialize=False)),
                ('Content', models.TextField()),
                ('CreatedAt', models.DateTimeField(default=django.utils.timezone.now)),
                ('IsRead', models.BooleanField()),
                ('Receiver', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='received_messages', to='myapp.user')),
                ('Sender', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='sent_messages', to='myapp.user')),
            ],
        ),
        migrations.CreateModel(
            name='GroupUsersLink',
            fields=[
                ('GroupUsersLinkID', models.AutoField(primary_key=True, serialize=False)),
                ('GroupID', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='myapp.group')),
                ('UserID', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='myapp.user')),
            ],
        ),
        migrations.CreateModel(
            name='GroupMessage',
            fields=[
                ('GroupMessageID', models.AutoField(primary_key=True, serialize=False)),
                ('Content', models.TextField()),
                ('CreatedAt', models.DateTimeField(default=django.utils.timezone.now)),
                ('ReceiverGroup', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='received_group_messages', to='myapp.group')),
                ('ReadBy', models.ManyToManyField(related_name='read_group_messages', to='myapp.user')),
                ('Sender', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='sent_group_messages', to='myapp.user')),
            ],
        ),
        migrations.CreateModel(
            name='GroupAssignProject',
            fields=[
                ('GroupID', models.AutoField(primary_key=True, serialize=False)),
                ('AllocatedAt', models.DateTimeField(default=django.utils.timezone.now)),
                ('ProgressStatus', models.CharField(choices=[('To Do', 'To Do'), ('In Progress', 'In Progress'), ('Done', 'Done')], default='To Do', max_length=20)),
                ('Project', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='myapp.project')),
                ('Allocated', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='myapp.user')),
            ],
        ),
        migrations.AddField(
            model_name='group',
            name='CreatedBy',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='groups_created', to='myapp.user'),
        ),
        migrations.AddField(
            model_name='group',
            name='GroupMembers',
            field=models.ManyToManyField(through='myapp.GroupUsersLink', to='myapp.user'),
        ),
        migrations.AddField(
            model_name='contact',
            name='Contact',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='contacts', to='myapp.user'),
        ),
        migrations.AddField(
            model_name='contact',
            name='ContactUser',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='myapp.user'),
        ),
        migrations.AlterUniqueTogether(
            name='contact',
            unique_together={('Contact', 'ContactUser')},
        ),
    ]
