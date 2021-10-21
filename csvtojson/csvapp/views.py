from django.shortcuts import render
from django.http import HttpResponse,HttpResponseRedirect
from django.urls import reverse
from django.contrib import messages
import csv
import pandas as pd
from  .csv_to_json import CsvToJson
import time

""" Create view to upload csv file"""
def uploadCsvView(request):
    return render(request, 'index.html')


def uploadCsv(request):
	""" Handle GET request"""

	if "GET" == request.method:
		return render(request, "index.html")

	try:
		""" Get the csv request file"""
		csv_file = request.FILES["csv_file"]

		""" Check valid csv file here"""

		if not csv_file.name.endswith('.csv'):
			messages.error(request,'File is not CSV type')
			return HttpResponseRedirect(reverse("upload_csv"))

		""" Read csv file here with pandas module"""

		df = pd.read_csv(csv_file)
		df.dropna(how ='all')

		""" Call the custom CsvToJson class to create nested json data """
		csv_object = CsvToJson(df)
		out_json = csv_object.tree_create()
		""" Generate output.json file to the browser"""
		response = HttpResponse(out_json, content_type='application/json')
		response['Content-Disposition'] = 'attachment; filename=output.json'
		return response

	except Exception as e:
		""" Generate the exception if any"""
		raise(e)
