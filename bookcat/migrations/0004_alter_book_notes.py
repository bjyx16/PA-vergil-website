# Generated by Django 5.0.6 on 2024-07-07 04:07

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("bookcat", "0003_rename_subject_book_category_book_bm_cat_and_more"),
    ]

    operations = [
        migrations.AlterField(
            model_name="book",
            name="notes",
            field=models.TextField(blank=True, null=True),
        ),
    ]
