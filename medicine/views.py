from django.shortcuts import render, redirect
from django.core.mail import send_mail

import medicine
from .models import Disease, User, Supplier, Medicine, Donating, Purchasing, Prescription, CalculationUnits
from .forms import PrescriptionForm, MedicineForm


# Create your views here.



def welcome(request):
	# medicine = Medicine.get_by_id(id)
	# calc = CalculationUnits.get_test()

	return render(request, 'test.html')


def home(request, disease):
	medicines = Medicine.filter_by_disease(disease) 

	return render(request, 'home.html',{'medicines':medicines, })

def play(request):
	test = Disease.get_medicine_number()

	return render(request, 'home2.html',{'test':test })

def details(request, id):
	# calc = CalculationUnits.unit_sum(id)
	# calc2 = CalculationUnits.units_sold_sum(id)
	# calc3 = CalculationUnits.set_price_latest(id)
	# calc4 = CalculationUnits.set_donations_sum(id)
	# calc5 = CalculationUnits.calculations(id)
	calc5 = CalculationUnits.calculations(id)
	
	return render(request, 'details.html', {'calc5':calc5,})

# def profile(request, id):
# 	profile = Profile.get_by_i
# 	return render(request, 'profile.html',{'profile':profile})d(id) 
	

def donor(request, donor):
	donations = Donating.filter_by_donor(donor) 
	
	return render(request, 'userdonations.html',{'donations':donations})

def celebration(request):
	
	return render(request, 'form_pages/congratulations.html')

# @login_required(login_url='/accounts/login/')
def prescription(request, id):
	medicine = Medicine.get_by_id(id)
	if request.method == 'POST':
		form = PrescriptionForm(request.POST, request.FILES)
		if form.is_valid():
			name = form.save(commit=False)
			name.medicine = medicine
			name.save()
			send_mail('Welcome' , 'Good to have you on board', 'inmariga@gmail.com',['nimariga@gmail.com'], fail_silently=False)
		return redirect( prescription,  medicine.id)
	else:
		form = PrescriptionForm()
	return render(request ,'form_pages/prescription.html', {'form': form , 'medicine': medicine})


def medicine_upload(request):
	if request.method == 'POST':
		form = MedicineForm(request.POST, request.FILES)
		if form.is_valid():
			name = form.save(commit=False)
			name.save()
		return redirect( medicine_upload)
	else:
		form = MedicineForm()
			
	return render(request ,'form_pages/medicine_upload.html', {'form': form })
