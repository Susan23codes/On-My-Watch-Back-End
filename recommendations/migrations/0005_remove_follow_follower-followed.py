# Generated by Django 4.0.6 on 2022-08-18 15:11

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('recommendations', '0004_recommendation_actors_recommendation_keywords_and_more'),
    ]

    operations = [
        migrations.RemoveConstraint(
            model_name='follow',
            name='follower-followed',
        ),
    ]
