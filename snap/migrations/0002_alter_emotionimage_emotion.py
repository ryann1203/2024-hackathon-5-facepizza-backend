# Generated by Django 5.0.7 on 2024-07-27 15:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('snap', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='emotionimage',
            name='emotion',
            field=models.CharField(choices=[('happy', 'Happy'), ('sad', 'Sad'), ('angry', 'Angry'), ('surprised', 'Surprised'), ('disgusted', 'Disgusted'), ('fearful', 'Fearful'), ('neutral', 'Neutral')], max_length=50),
        ),
    ]