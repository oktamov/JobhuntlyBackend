

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('company', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='workingatcompany',
            name='user',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='working_company', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='techstack',
            name='user',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='tech_stacks', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='sector',
            name='user',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='sectors', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='contact',
            name='company',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='contacts', to='company.company'),
        ),
        migrations.AddField(
            model_name='contact',
            name='user',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='contacts', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='company',
            name='benefits',
            field=models.ManyToManyField(related_name='companies', to='company.benefit'),
        ),
        migrations.AddField(
            model_name='company',
            name='sector',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='companies', to='company.sector'),
        ),
        migrations.AddField(
            model_name='company',
            name='tech_stacks',
            field=models.ManyToManyField(related_name='companies', to='company.techstack'),
        ),
        migrations.AddField(
            model_name='company',
            name='user',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='companies', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='benefit',
            name='user',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='benefits', to=settings.AUTH_USER_MODEL),
        ),
    ]
