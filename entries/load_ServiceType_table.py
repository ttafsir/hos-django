#!/usr/bin/env python
#coding: utf8 

# Full path and name to your csv file

#csv_filepathname="/Users/thomasgertin1/hos-django/entries/20140415_HAC_utf8.csv"
#csv_filepathname="./data/20140419_mmex_utf8.csv"

import django
django.setup()

# Full path to your django project directory

your_djangoproject_home="../"

import sys,os
sys.path.append(your_djangoproject_home)

os.environ['DJANGO_SETTINGS_MODULE'] = 'hos2.settings'
#os.environ.setdefault("DJANGO_SETTINGS_MODULE", "hos2.settings")
 
from entries.models import ServiceProvider,Location,EffortInstance,ServiceType,EffortInstanceService
 
import csv

#module used for regular expressions
import re

import random

#dataReader = csv.reader(open(csv_filepathname), delimiter=',', quotechar='"')
 
ServiceType = ServiceType()

#create list in english
services_en = ['Cardiovascular',
'Clinical services',
'Contagious diseases',
'Dental',
'Diabetes',
'Emergency', 
'Environmental health',
'EyeCare',
'Gender based violence',
'General consultation',
'HIV-SIDA infections',
'Hypertension',
'Infant health',
'Intensive care',
'Laboratory',
'Malaria',
'Maternity health',
'Nutrition',
'ObGyn',
'Obstetric care',
'Operating room',
'ORL', 
'Palliative care',
'Pediatrics',
'Pharmacy',
'Physical therapy',  
'Psychology service',
'Re-education',
'Surgery',
'Vaccination (PEV)',
'Other']

#create list in creole
services_cr = ['kadyo-vaskilè',
'Sèvis nan klinik',
'Maladi kontajye',
'Tretman Dantè',
'Dyabèt ou maladi sik',
'Ijans', 
'Sante anviwònman an',
'Swen Zye',
'Egalite  Sèks yo, ou fanm egal ak gason ',
'Konsiltasyon Jeneral',
'VIH-SIDA Enfeksyon',
'Tansyon wo',
'Sante timoun',
'Swen Entansif',
'laboratwa',
'Malarya',
'Matènite',
'Nitrisyon',
'OBGYN ou sante fanm yo',
'Swen Obstetrik',
'Chanm Operating',
'ORL ou sante pou zorèy, je ak gòj', 
'Swen palyatif',
'Pedyatri',
'Famasi',
'Terapi fizik',  
'Sèvis Sikoloji',
'Re-edikasyon / Sante Piblik',
'Operasyon',
'Vaksinasyon (PEV)',
'Lòt']

#create list in french
services_fr = ['Cardiovasculaire',
'Services de clinique',
'Maladies contagieuses',
'Dentaire',
'Diabète',
'Urgence',
'Santé Environnementale',
'Ophtalmologie',
'Violence basée sur les genres',
'Médecine Générale',
'HIV-SIDA Infections',
'Hypertension',
'Santé pour enfants en bas âge',
'Soins Intensifs',
'Laboratoire',
'Malaria',
'Soins pour femmes enceintes/obstétric',
'Nutrition',
'Gynécologie',
'Soins obstétriques',
'Bloc opératoire',
'ORL',
'Soins Palliatifs',
'Pédiatrie',
'Pharmacie',
'Thérapie Physique',
'Psychologie',
'Re-éducation (Santé Publique)',
'Chirurgie',
'Vaccination',
'Autre']

count = 1

for x in range(0,len(services_en)):

	ServiceType.service_type_id = count
	ServiceType.service_name_en = services_en[x]
	ServiceType.service_name_cr = services_cr[x]
	ServiceType.service_name_fr = services_fr[x]
	
	
	count = count + 1


	ServiceType.save()


