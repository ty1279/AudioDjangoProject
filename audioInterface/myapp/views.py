from django.shortcuts import render, HttpResponse
from .forms import ContactForm
from .forms import CsvModelForm
from .models import Attribute
import csv

import matplotlib.pyplot as plt
import io
import urllib, base64
import pandas as pd
import numpy as np

def home(request):
	if request.method == "POST" :
		form = ContactForm(request.POST)
		if form.is_valid():

			x_axis = form.cleaned_data['x_axis']
			y_axis = form.cleaned_data['y_axis']
			print(x_axis)
			print(y_axis)


	################################################################################################
	#######################################		 CSV File	 #######################################
	################################################################################################
	print("hmm")
	age = []
	accent_group = []
	sex_in_number = []

	with open('D:/4114_6391_bundle_archive/speakers_all.csv') as f:
		print("here")
		reader = csv.reader(f)
		next(f)
		for row in reader:
			_, created = Attribute.objects.get_or_create(
			age = row[0],
			accent_group = row[9],
			sex_in_number = row[11],
			)
			age.append(row[0])
			accent_group.append(row[9])
			sex_in_number.append(row[11])

	################################################################################################
	#############################	 PRESENTING PLOTS with Matplotlib	############################
	################################################################################################
	generated_data = []
	axis_values_x = []
	axis_values_y = []

	for (item1, item2) in zip(age, accent_group):
   		generated_data.append((item1, item2))

	# print(generated_data)
	for index, instance in enumerate(generated_data):
		coordinate_x, coordinate_y = instance
		axis_values_x.append(coordinate_x)
		axis_values_y.append(coordinate_y) 

	axis_values_x = np.array(axis_values_x, dtype=np.int)
	axis_values_y = np.array(axis_values_y, dtype=np.int)

	print(axis_values_x)
	print(axis_values_y)

	fig = plt.figure(figsize=(20, 16))
	ax = fig.add_subplot(1,1,1,picker=True)

	ax.scatter(
			axis_values_x,
			axis_values_y,
			picker=True
		)
	ax.set_title("Voice Samples")

	#convert graph into dtring buffer and then we convert 64 bit code into image
	buf = io.BytesIO()
	fig.savefig(buf,format='png')
	buf.seek(0)
	string = base64.b64encode(buf.read())
	uri =  urllib.parse.quote(string)
	
	# Select box form
	form = ContactForm()

	return render(request, 'home.html', {'aform': form, 'data': uri})

