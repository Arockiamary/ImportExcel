from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import ImportExl
from myapp.forms import ImportExlForm
from django.contrib import messages
import csv,io
from django.contrib.auth.decorators import permission_required


# Create your views here.
def index(request):
	return render(request,'index.html')


def upload(request):
	if request.method =="POST":
		form=ImportExlForm(request.POST, request.FILES)
		if form.is_valid():
			form.save()
			return render(request, "base.html",{'form':form})
	else:
		form=ImportExlForm()
	return render(request,'base.html')


@permission_required('admin.can_add_log_entry')
def contact_upload(request):
	template="base.html"
	prompt={
		'order': 'Order of the CSV should be name, age'
	}
	if request.method=="GET":
		return render(request, template, prompt)
	csv_file=request.FILES['files']

	if not csv_file.name.endswith('.csv'):
		messages.error(request,'This is not a csv file')

	data_set =csv_file.read().decode('UTF-8')
	io_string=io.String(data_set)
	next(io_string)
	for column in csv.reader(io_string, delimiter=',',quotechar="|"):
		_, created=Contact.objects.update_or_create(
			name=column[0],
			age=column[1],
								
		)

		context={}
		return render(request, template, context)

