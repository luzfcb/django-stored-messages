from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('stored_messages', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='message',
            name='url',
            field=models.URLField(blank=True, null=True),
        ),
    ]
