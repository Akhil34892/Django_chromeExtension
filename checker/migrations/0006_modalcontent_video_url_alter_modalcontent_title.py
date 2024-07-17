# Generated by Django 4.2.7 on 2024-07-15 15:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('checker', '0005_remove_question_modal_content_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='modalcontent',
            name='video_url',
            field=models.URLField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='modalcontent',
            name='title',
            field=models.CharField(max_length=200),
        ),
    ]
