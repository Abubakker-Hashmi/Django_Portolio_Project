# Generated by Django 4.2.2 on 2023-06-22 12:45

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Employee",
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
                ("employee_number", models.IntegerField(max_length=20, unique=True)),
                ("name", models.CharField(max_length=100)),
                ("department", models.CharField(max_length=100)),
                ("role", models.CharField(max_length=100)),
                ("salary", models.DecimalField(decimal_places=2, max_digits=10)),
                ("working_experience", models.IntegerField()),
            ],
        ),
    ]
