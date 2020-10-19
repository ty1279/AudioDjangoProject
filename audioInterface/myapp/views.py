from django.shortcuts import render, HttpResponse
from .forms import ContactForm
from .forms import CsvModelForm
from .models import Attribute
import csv

import matplotlib.pyplot as plt
from plotly.offline import plot
from plotly.graph_objs import Scatter

import io
import urllib, base64
import pandas as pd
import numpy as np

def home(request):
	x_axis = ""
	y_axis = ""
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
	age = []
	accent_group = []
	sex_in_number = []

	with open('D:/4114_6391_bundle_archive/speakers_all.csv') as f:
		print("Start loading csv file ...")
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

	if (x_axis == "age") & (y_axis == "age") :
		for (item1, item2) in zip(age, age):
   			generated_data.append((item1, item2))
	elif (x_axis == "age") & (y_axis == "gender") :
		for (item1, item2) in zip(age, sex_in_number):
   			generated_data.append((item1, item2))
	elif (x_axis == "age") & (y_axis == "accent") :
		for (item1, item2) in zip(age, accent_group):
   			generated_data.append((item1, item2))
	elif (x_axis == "gender") & (y_axis == "age") :
		for (item1, item2) in zip(sex_in_number, age):
   			generated_data.append((item1, item2))
	elif (x_axis == "gender") & (y_axis == "gender") :
		for (item1, item2) in zip(sex_in_number, sex_in_number):
   			generated_data.append((item1, item2))
	elif (x_axis == "gender") & (y_axis == "accent") :
		for (item1, item2) in zip(sex_in_number, accent_group):
   			generated_data.append((item1, item2))
	elif (x_axis == "accent") & (y_axis == "age") :
		for (item1, item2) in zip(accent_group, age):
   			generated_data.append((item1, item2))
	elif (x_axis == "accent") & (y_axis == "gender") :
		for (item1, item2) in zip(accent_group, sex_in_number):
   			generated_data.append((item1, item2))
	elif (x_axis == "accent") & (y_axis == "accent") :
		for (item1, item2) in zip(accent_group, accent_group):
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


	plot_div  = plot([Scatter(x=axis_values_x, y=axis_values_y,
                        mode='markers', name='test',
                        opacity=0.8, marker_color='green')],
               output_type='div')

	# Select box form
	form = ContactForm()
	
	return render(request, 'home.html', {'aform': form, 'plot_div': plot_div})




##################################################################################################################################

def home2(request):
	x_axis = ""
	y_axis = ""
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
	age = []
	accent_group = []
	sex_in_number = []

	with open('D:/4114_6391_bundle_archive/speakers_all.csv') as f:
		print("Start loading csv file ...")
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

	if (x_axis == "age") & (y_axis == "age") :
		for (item1, item2) in zip(age, age):
   			generated_data.append((item1, item2))
	elif (x_axis == "age") & (y_axis == "gender") :
		for (item1, item2) in zip(age, sex_in_number):
   			generated_data.append((item1, item2))
	elif (x_axis == "age") & (y_axis == "accent") :
		for (item1, item2) in zip(age, accent_group):
   			generated_data.append((item1, item2))
	elif (x_axis == "gender") & (y_axis == "age") :
		for (item1, item2) in zip(sex_in_number, age):
   			generated_data.append((item1, item2))
	elif (x_axis == "gender") & (y_axis == "gender") :
		for (item1, item2) in zip(sex_in_number, sex_in_number):
   			generated_data.append((item1, item2))
	elif (x_axis == "gender") & (y_axis == "accent") :
		for (item1, item2) in zip(sex_in_number, accent_group):
   			generated_data.append((item1, item2))
	elif (x_axis == "accent") & (y_axis == "age") :
		for (item1, item2) in zip(accent_group, age):
   			generated_data.append((item1, item2))
	elif (x_axis == "accent") & (y_axis == "gender") :
		for (item1, item2) in zip(accent_group, sex_in_number):
   			generated_data.append((item1, item2))
	elif (x_axis == "accent") & (y_axis == "accent") :
		for (item1, item2) in zip(accent_group, accent_group):
   			generated_data.append((item1, item2))


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

	plt.xlabel(x_axis)
	plt.ylabel(y_axis)
	#Save the plot as an image
	plt.savefig('static/images/new_file.png')

	# Select box form
	form = ContactForm()

	return render(request, 'home2.html', {'aform': form})


