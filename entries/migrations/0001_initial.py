# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.contrib.gis.db.models.fields


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Admin_cluster_results',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('type', models.CharField(default=b'CL', max_length=2, choices=[(b'TT', b'Traveling Team'), (b'CL', b'Clinic'), (b'HL', b'Hospital')])),
                ('date_start', models.DateTimeField(null=True)),
                ('date_end', models.DateTimeField(null=True)),
                ('default', models.NullBooleanField()),
                ('description', models.CharField(max_length=600, blank=True)),
                ('drupal_id', models.IntegerField(default=0)),
                ('provider_name', models.CharField(max_length=500)),
                ('nearby_points', models.IntegerField(null=True, blank=True)),
                ('point_checked', models.NullBooleanField()),
                ('latitude', models.CharField(max_length=15, null=True, blank=True)),
                ('longitude', models.CharField(max_length=15, null=True, blank=True)),
                ('geom', django.contrib.gis.db.models.fields.PointField(srid=4326, dim=3, null=True, geography=True, blank=True)),
            ],
            options={
                'abstract': False,
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='EffortInstance',
            fields=[
                ('type', models.CharField(default=b'CL', max_length=2, choices=[(b'TT', b'Traveling Team'), (b'CL', b'Clinic'), (b'HL', b'Hospital')])),
                ('date_start', models.DateTimeField(null=True)),
                ('date_end', models.DateTimeField(null=True)),
                ('default', models.NullBooleanField()),
                ('description', models.CharField(max_length=600, blank=True)),
                ('drupal_id', models.IntegerField(default=0)),
                ('effort_instance_id', models.IntegerField(serialize=False, primary_key=True)),
                ('updated_on', models.DateTimeField(null=True)),
                ('updated_by', models.CharField(max_length=100, blank=True)),
            ],
            options={
                'abstract': False,
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='EffortInstanceService',
            fields=[
                ('effort_instance_service_id', models.AutoField(serialize=False, primary_key=True)),
                ('effort_instance', models.ForeignKey(blank=True, to='entries.EffortInstance', null=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='haiti_adm1_minustah',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('id_adm1', models.FloatField()),
                ('adm1', models.CharField(max_length=45)),
                ('shape_leng', models.FloatField()),
                ('shape_area', models.FloatField()),
                ('geom', django.contrib.gis.db.models.fields.MultiPolygonField(srid=4326)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='haiti_adm2_minustah',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('id_adm1', models.FloatField()),
                ('adm1', models.CharField(max_length=45)),
                ('id_adm2', models.FloatField()),
                ('adm2', models.CharField(max_length=45)),
                ('shape_leng', models.FloatField()),
                ('shape_area', models.FloatField()),
                ('pop', models.IntegerField()),
                ('sq_miles', models.FloatField()),
                ('pop_sq_mi', models.FloatField()),
                ('geom', django.contrib.gis.db.models.fields.MultiPolygonField(srid=4326)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='haiti_adm3_minustah',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('id_adm1', models.FloatField()),
                ('adm1', models.CharField(max_length=45)),
                ('id_adm2', models.FloatField()),
                ('adm2', models.CharField(max_length=45)),
                ('id_adm3', models.FloatField()),
                ('nom_adm3', models.CharField(max_length=45)),
                ('adm3', models.CharField(max_length=45)),
                ('shape_leng', models.FloatField()),
                ('shape_area', models.FloatField()),
                ('geom', django.contrib.gis.db.models.fields.MultiPolygonField(srid=4326)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='haiti_adm4_minustah',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('shape_leng', models.FloatField()),
                ('shape_area', models.FloatField()),
                ('id_adm1', models.FloatField()),
                ('adm1', models.CharField(max_length=45)),
                ('id_adm2', models.FloatField()),
                ('adm2', models.CharField(max_length=45)),
                ('id_adm3', models.FloatField()),
                ('nom_adm3', models.CharField(max_length=45)),
                ('adm3', models.CharField(max_length=45)),
                ('no_adm4', models.FloatField()),
                ('id_adm4', models.CharField(max_length=45)),
                ('nom_adm4', models.CharField(max_length=45)),
                ('adm4', models.CharField(max_length=45)),
                ('shape_le_1', models.FloatField()),
                ('shape_ar_1', models.FloatField()),
                ('geom', django.contrib.gis.db.models.fields.MultiPolygonField(srid=4326)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Location',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('latitude', models.CharField(max_length=15, null=True, blank=True)),
                ('longitude', models.CharField(max_length=15, null=True, blank=True)),
                ('geom', django.contrib.gis.db.models.fields.PointField(srid=4326, null=True, blank=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Location_w_efforts',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('type', models.CharField(default=b'CL', max_length=2, choices=[(b'TT', b'Traveling Team'), (b'CL', b'Clinic'), (b'HL', b'Hospital')])),
                ('date_start', models.DateTimeField(null=True)),
                ('date_end', models.DateTimeField(null=True)),
                ('default', models.NullBooleanField()),
                ('description', models.CharField(max_length=600, blank=True)),
                ('drupal_id', models.IntegerField(default=0)),
                ('provider_name', models.CharField(max_length=500)),
                ('latitude', models.CharField(max_length=15, null=True, blank=True)),
                ('longitude', models.CharField(max_length=15, null=True, blank=True)),
                ('geom', django.contrib.gis.db.models.fields.PointField(srid=4326, dim=3, null=True, geography=True, blank=True)),
            ],
            options={
                'abstract': False,
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Location_w_efforts_temp',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('type', models.CharField(default=b'CL', max_length=2, choices=[(b'TT', b'Traveling Team'), (b'CL', b'Clinic'), (b'HL', b'Hospital')])),
                ('date_start', models.DateTimeField(null=True)),
                ('date_end', models.DateTimeField(null=True)),
                ('default', models.NullBooleanField()),
                ('description', models.CharField(max_length=600, blank=True)),
                ('drupal_id', models.IntegerField(default=0)),
                ('provider_name', models.CharField(max_length=500)),
                ('latitude', models.CharField(max_length=15, null=True, blank=True)),
                ('longitude', models.CharField(max_length=15, null=True, blank=True)),
                ('geom', django.contrib.gis.db.models.fields.PointField(srid=4326, dim=3, null=True, geography=True, blank=True)),
            ],
            options={
                'abstract': False,
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='ServiceProvider',
            fields=[
                ('service_provider_id', models.AutoField(serialize=False, primary_key=True)),
                ('provider_name', models.CharField(max_length=500)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='ServiceType',
            fields=[
                ('service_type_id', models.IntegerField(serialize=False, primary_key=True)),
                ('service_name_en', models.CharField(max_length=100, blank=True)),
                ('service_name_fr', models.CharField(max_length=100, blank=True)),
                ('service_name_cr', models.CharField(max_length=100, blank=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Similar_strings',
            fields=[
                ('similar_strings_id', models.AutoField(serialize=False, primary_key=True)),
                ('string_id', models.IntegerField(null=True, blank=True)),
                ('provider_name', models.CharField(max_length=500)),
                ('related_string_id', models.IntegerField(null=True, blank=True)),
                ('related_provider_name', models.CharField(max_length=500)),
                ('similarity_score', models.DecimalField(max_digits=15, decimal_places=13)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Spatial_cluster_results',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('type', models.CharField(default=b'CL', max_length=2, choices=[(b'TT', b'Traveling Team'), (b'CL', b'Clinic'), (b'HL', b'Hospital')])),
                ('date_start', models.DateTimeField(null=True)),
                ('date_end', models.DateTimeField(null=True)),
                ('default', models.NullBooleanField()),
                ('description', models.CharField(max_length=600, blank=True)),
                ('drupal_id', models.IntegerField(default=0)),
                ('effort_instance_id', models.IntegerField()),
                ('provider_name', models.CharField(max_length=500)),
                ('nearby_points', models.IntegerField(null=True, blank=True)),
                ('point_checked', models.NullBooleanField()),
                ('latitude', models.CharField(max_length=15, null=True, blank=True)),
                ('longitude', models.CharField(max_length=15, null=True, blank=True)),
                ('geom', django.contrib.gis.db.models.fields.PointField(srid=4326, dim=3, null=True, geography=True, blank=True)),
                ('service_provider', models.ForeignKey(blank=True, to='entries.ServiceProvider', null=True)),
            ],
            options={
                'abstract': False,
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='location_w_efforts_temp',
            name='service_provider',
            field=models.ForeignKey(blank=True, to='entries.ServiceProvider', null=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='location_w_efforts',
            name='service_provider',
            field=models.ForeignKey(blank=True, to='entries.ServiceProvider', null=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='effortinstanceservice',
            name='effort_service_type',
            field=models.ForeignKey(blank=True, to='entries.ServiceType', null=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='effortinstance',
            name='adm_1',
            field=models.ForeignKey(blank=True, to='entries.haiti_adm1_minustah', null=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='effortinstance',
            name='adm_2',
            field=models.ForeignKey(blank=True, to='entries.haiti_adm2_minustah', null=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='effortinstance',
            name='adm_3',
            field=models.ForeignKey(blank=True, to='entries.haiti_adm3_minustah', null=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='effortinstance',
            name='location',
            field=models.OneToOneField(null=True, blank=True, to='entries.Location'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='effortinstance',
            name='service_provider',
            field=models.ForeignKey(blank=True, to='entries.ServiceProvider', null=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='admin_cluster_results',
            name='service_provider',
            field=models.ForeignKey(blank=True, to='entries.ServiceProvider', null=True),
            preserve_default=True,
        ),
    ]
