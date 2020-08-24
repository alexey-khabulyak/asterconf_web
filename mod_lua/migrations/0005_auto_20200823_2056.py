# Generated by Django 3.1 on 2020-08-23 17:56

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('mod_lua', '0004_remove_user_context'),
    ]

    operations = [
        migrations.CreateModel(
            name='IVR',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, verbose_name='IVR')),
                ('greet_long', models.CharField(default='ivr-welcome_to_freeswitch.wav', max_length=100, verbose_name='IVR')),
                ('greet_short', models.CharField(default='ivr-welcome_to_freeswitch.wav', max_length=100, verbose_name='IVR')),
                ('invalid_sound', models.CharField(default='ivr/ivr-that_was_an_invalid_entry.wav', max_length=100, verbose_name='IVR')),
                ('exit_sound', models.CharField(default='voicemail/vm-goodbye.wav', max_length=100, verbose_name='IVR')),
                ('timeout', models.IntegerField(default=10000, verbose_name='Timeout')),
                ('max_failures', models.IntegerField(default=3, verbose_name='Количество попыток')),
            ],
            options={
                'verbose_name': 'IVR',
                'verbose_name_plural': "IVR's",
            },
        ),
        migrations.AlterField(
            model_name='contextaction',
            name='condition_field',
            field=models.CharField(default='Caller-Destination-Number', max_length=255, verbose_name='Поле условия'),
        ),
        migrations.CreateModel(
            name='IVREntry',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('action', models.CharField(choices=[('menu-exit', 'Выход'), ('menu-sub', 'Sub-menu'), ('menu-exec-app', 'Приложение'), ('menu-play-sound', 'Звуковой файл'), ('menu-back', 'Назад'), ('menu-top', 'Top menu')], default='menu-exec-app', max_length=100, verbose_name='Действие')),
                ('digit', models.CharField(max_length=100, verbose_name='Цифры')),
                ('param', models.CharField(blank=True, max_length=100, null=True, verbose_name='Параметры')),
                ('IVR', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='mod_lua.ivr')),
            ],
            options={
                'verbose_name': 'Пункт меню',
                'verbose_name_plural': 'Пункты меню',
            },
        ),
    ]