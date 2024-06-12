# Generated by Django 5.0.6 on 2024-06-05 19:25

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cadastros', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customuser',
            name='cargo',
            field=models.ForeignKey(default=1, help_text='Selecione o cargo...', on_delete=django.db.models.deletion.CASCADE, to='cadastros.cargo'),
        ),
        migrations.AlterField(
            model_name='customuser',
            name='celular',
            field=models.CharField(default='', max_length=15),
        ),
        migrations.AlterField(
            model_name='customuser',
            name='observacoes',
            field=models.TextField(blank=True, default='', help_text='Adicione quaisquer observações adicionais sobre o usuário', null=True),
        ),
        migrations.AlterField(
            model_name='customuser',
            name='orgao',
            field=models.ForeignKey(default=1, help_text='Selecione o orgão...', on_delete=django.db.models.deletion.CASCADE, to='cadastros.orgao'),
        ),
        migrations.AlterField(
            model_name='customuser',
            name='setor',
            field=models.CharField(default='', max_length=100),
        ),
        migrations.AlterField(
            model_name='customuser',
            name='tipo_acesso',
            field=models.ForeignKey(default=1, help_text='Selecione o tipo de acesso...', on_delete=django.db.models.deletion.CASCADE, to='cadastros.tipoacesso'),
        ),
    ]
