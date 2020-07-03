# Generated by Django 2.0 on 2019-10-24 17:26

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('csdn', '0012_blogtype'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='csdnblog',
            name='blog_type',
        ),
        migrations.AddField(
            model_name='csdnblog',
            name='blog_id',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='csdn.BlogType', verbose_name='博客类别id'),
        ),
    ]