# Generated by Django 5.0.6 on 2024-05-25 14:14

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("bookcat", "0001_initial"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="book",
            name="title",
        ),
        migrations.AddField(
            model_name="book",
            name="call_num",
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name="book",
            name="genre",
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name="book",
            name="image_loc",
            field=models.FileField(blank=True, null=True, upload_to="bookcat_images/"),
        ),
        migrations.AddField(
            model_name="book",
            name="image_str",
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name="book",
            name="subject",
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name="book",
            name="title_description",
            field=models.TextField(default="TBD"),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name="book",
            name="contributors",
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name="book",
            name="date",
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name="book",
            name="language",
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name="book",
            name="place_origin",
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name="book",
            name="publisher",
            field=models.TextField(blank=True, null=True),
        ),
    ]
