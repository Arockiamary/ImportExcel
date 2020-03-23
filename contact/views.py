from django.shortcuts import render, redirect
from django.http import HttpResponse
from contact.forms import ContactModelForm
from django.core.mail import send_mail, BadHeaderError
import csv,io
from django.contrib.auth.decorators import permission_required

def emailView(request):
    if request.method =="POST":
        form=ContactModelForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return render(request, "callusform.html",{'form':form})
       
    else:
        form=ContactModelForm()
    return render(request,"callusform.html",{'form':form}) 

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
			from_email=column[0],
			subject=column[1],
			message=column[2],
								
		)

		context={}
		return render(request, template, context)      



