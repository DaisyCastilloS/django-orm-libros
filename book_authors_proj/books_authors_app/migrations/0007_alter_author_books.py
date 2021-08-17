# Generated by Django 3.2.6 on 2021-08-16 01:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('books_authors_app', '0006_book_action'),
    ]

    operations = [
        migrations.AlterField(
            model_name='author',
            name='books',
            field=models.ManyToManyField(related_name='libros', to='books_authors_app.Book'),
        ),
    ]