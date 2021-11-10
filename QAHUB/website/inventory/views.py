from django.shortcuts import render, HttpResponse

from django.template import loader
from django.shortcuts import redirect
from .models import *
from .forms import *



# Create your views here.
def inventory(request):
    items = materialForm.objects.all()
    #template = loader.get_template('website/inventory.html')
    #return HttpResponse(template.render({}, request))
    return render(request, 'website/inventory.html', {'items': items})

def home(request):
    template = loader.get_template('website/home.html')
    return HttpResponse(template.render({}, request))  

def entry(request):
	form = entryForm()
	if request.method == 'POST':
		#print('Printing POST:', request.POST)
		form = entryForm(request.POST)
		if form.is_valid():
			form.save()
			return redirect('/main')
	#upload to Material form???
	else:
		context = {'form':form}
		return render(request, 'website/entry.html', context)

def products(request, pk):
	products = materialForm.objects.get(id=pk)
	context = {'products':products }
	return render(request, 'website/receipt.html', context )
#id=pk
#{'product':products}


	orders = customer.order_set.all()
	order_count = orders.count()

	context = {'customer':customer, 'orders':orders, 'order_count':order_count}
	return render(request, 'accounts/customer.html',context)
