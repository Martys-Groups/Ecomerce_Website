# Generated by Django 4.1.7 on 2023-04-01 16:15

from django.db import migrations, models


class Migration(migrations.Migration):
    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Products",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("Product_name", models.CharField(max_length=150)),
                ("category", models.CharField(default="", max_length=50)),
                ("sub_category", models.CharField(max_length=50)),
                ("price", models.IntegerField()),
                ("desc", models.TextField()),
                ("image", models.ImageField(upload_to="shop/images")),
                ("pub_date", models.DateField()),
            ],
        ),
    ]
