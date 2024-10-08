# Generated by Django 4.2.7 on 2024-10-04 08:20

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0009_alter_chap_truyen'),
    ]

    operations = [
        migrations.AlterField(
            model_name='chap',
            name='truyen',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='chap', to='myapp.truyen'),
        ),
        migrations.AlterField(
            model_name='trang',
            name='chap',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='chap', to='myapp.chap'),
        ),
        migrations.AlterField(
            model_name='truyen',
            name='anhbia',
            field=models.FileField(upload_to='anhbia/'),
        ),
        migrations.AlterField(
            model_name='truyen',
            name='anhnen',
            field=models.FileField(upload_to='anhnen/'),
        ),
    ]
