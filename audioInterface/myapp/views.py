from django.shortcuts import render, HttpResponse
from .forms import ContactForm
from .forms import CsvModelForm
from .models import Csv
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
	####################################### PRESENTING PLOTS #######################################
	################################################################################################
	# Loading dataset
	#df = pd.read_csv('D:/4114_6391_bundle_archive/speakers_all.csv')

	
	#axis_values_x = np.array(axis_values_x, dtype=np.int)
	#axis_values_y = np.array(axis_values_y, dtype=np.int)

	# matpotlib
	fig = plt.figure(figsize=(20, 16))
	fig.clear()
	ax = fig.add_subplot(1,1,1,picker=True)
	axis_values_x = [ 1,2,3,4]
	axis_values_y = [ 10,20,30 ]
	ax.scatter(
			axis_values_x[0],
			axis_values_y[0],
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
	# CSV File form
	form2 = CsvModelForm(request.POST or None, request.FILES or None)

	################################################################################################
	#######################################		 CSV File	 #######################################
	################################################################################################
	if form2.is_valid():
		form2 = CsvModelForm()
		# obj = Csv.objects.get(activated=False)
		# with open(obj.file_name.path, 'r') as f:
		# 	reader = csv.reader(f)
		# 	for i, row in enumerate(reader):
		# 		if i==0:
		# 			pass
		# 		else:
		# 			print (row)

	return render(request, 'home.html', {'aform': form, 'bform': form2, 'data': uri})





# def upload_file_view(request):
# 	form2 = CsvModelForm(request.POST or None, request.FILES or None)
# 	# obj = Csv.objects.get(activated=False)
# 	# with open(obj.file_name.path, 'r') as f:
# 	# 	reader = csv.reader(f)
# 	# 	for i, row in enumerate(reader):
# 	# 		if i==0:
# 	# 			pass
# 	# 		else:
# 	# 			print (row)

# 	return render(request, 'home.html', {'form': form2})
