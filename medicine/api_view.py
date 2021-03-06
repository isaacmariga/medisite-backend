from django.shortcuts import render, redirect
from .models import User, Supplier, Medicine, Donating, Purchasing, Prescription, Disease, MediUnits, CalculationUnits
from .serializer import  SupplierSerializer, MedicineSerializer, DonatingSerializer, PurchasingSerializer, PrescriptionSerializer, DiseaseSerializer, MediUnitsSerializer, CalculationUnitsSerializer
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status

# class ProfileList(APIView):
# 		def get(self, request, format=None):
# 				profile = Profile.get_all_profiles()
# 				serializers = ProfileSerializer(profile, many=True)
# 				return Response(serializers.data)
# 		def post(self, request, format=None):
# 				serializers = ProfileSerializer(data=request.data)
# 				if serializers.is_valid():
# 						serializers.save()
# 						return Response(serializers.data, status=status.HTTP_201_CREATED)
# 				return Response(serializers.errors, status=status.HTTP_400_BAD_REQUEST)
				
class SupplierList(APIView):
		def get(self, request, format=None):
				suppliers = Supplier.get_all_suppliers()
				serializers = SupplierSerializer(suppliers, many=True)
				return Response(serializers.data)
		def post(self, request, format=None):
				serializers = SupplierSerializer(data=request.data)
				if serializers.is_valid():
						serializers.save()
						return Response(serializers.data, status=status.HTTP_201_CREATED)
				return Response(serializers.errors, status=status.HTTP_400_BAD_REQUEST)
				
class MedicineList(APIView):
		def get(self, request, format=None):
				medicines = Medicine.get_all_medicines()
				serializers = MedicineSerializer(medicines, many=True)
				print(serializers.data)

				return Response(serializers.data)
		def post(self, request, format=None):
				serializers = MedicineSerializer(data=request.data)
				if serializers.is_valid():
						serializers.save()
						return Response(serializers.data, status=status.HTTP_201_CREATED)
				return Response(serializers.errors, status=status.HTTP_400_BAD_REQUEST)
				
class DonatingList(APIView):
		def get(self, request, format=None):
				donations = Donating.get_all_donations()
				serializers = DonatingSerializer(donations, many=True)
				return Response(serializers.data)
		def post(self, request, format=None):
				serializers = DonatingSerializer(data=request.data)
				if serializers.is_valid():
						serializers.save()
						return Response(serializers.data, status=status.HTTP_201_CREATED)
				return Response(serializers.errors, status=status.HTTP_400_BAD_REQUEST)
				
class PurchasingList(APIView):
		def get(self, request, format=None):
				purchase = Purchasing.get_all_purchases()
				serializers = PurchasingSerializer(purchase, many=True)
				return Response(serializers.data)
		def post(self, request, format=None):
				serializers = PurchasingSerializer(data=request.data)
				if serializers.is_valid():
						serializers.save()
						return Response(serializers.data, status=status.HTTP_201_CREATED)
				return Response(serializers.errors, status=status.HTTP_400_BAD_REQUEST)
				
class PrescriptionList(APIView):
		def get(self, request, format=None):
				prescription = Prescription.get_all_prescriptions()
				serializers = PrescriptionSerializer(prescription, many=True)
				return Response(serializers.data)
		def post(self, request, format=None):
				serializers = PrescriptionSerializer(data=request.data)
				if serializers.is_valid():
						serializers.save()
						return Response(serializers.data, status=status.HTTP_201_CREATED)
				return Response(serializers.errors, status=status.HTTP_400_BAD_REQUEST)
				
class DiseaseList(APIView):
		def get(self, request, format=None):
				disease = Disease.get_all_diseases()
				serializers = DiseaseSerializer(disease, many=True)
				return Response(serializers.data)

		def post(self, request, format=None):
				serializers = DiseaseSerializer(data=request.data)
				if serializers.is_valid():
						serializers.save()
						return Response(serializers.data, status=status.HTTP_201_CREATED)
				return Response(serializers.errors, status=status.HTTP_400_BAD_REQUEST)
class MediUnitsList(APIView):
		def get(self,request,  format=None):
				mediunit = MediUnits.get_all_units()
				serializers = MediUnitsSerializer(mediunit, many=True)
				return Response(serializers.data)

		def post(self, request, format=None):
				serializers = MediUnitsSerializer(data=request.data)
				if serializers.is_valid():
						serializers.save()
						return Response(serializers.data, status=status.HTTP_201_CREATED)
				return Response(serializers.errors, status=status.HTTP_400_BAD_REQUEST)
				

class UnitsByMedicine(APIView):
		def get(self,request,  id, format=None):
				mediunit = MediUnits.filter_by_medicine(id)
				serializers = MediUnitsSerializer(mediunit, many=True)
				return Response(serializers.data)

class MedicineByDisease(APIView):
		def get(self, request, disease, format=None):
			medicine_disease = Medicine.filter_by_disease(disease)
			serializers = MedicineSerializer(medicine_disease, many=True)
			print(serializers.data)

			return Response(serializers.data)

class MedicineById(APIView):
		def get(self, request, id, format=None):
			medicine_id = Medicine.get_by_id(id)
			serializers = MedicineSerializer(medicine_id)

			# print()

			return Response(serializers.data)



class CalculationUnitsList(APIView):
		def get(self,request,  format=None):
				calculation_units = CalculationUnits.get_all()
				serializers = CalculationUnitsSerializer(calculation_units, many=True)
				return Response(serializers.data)

		def post(self, request, format=None):
				serializers = CalculationUnitsSerializer(data=request.data)
				if serializers.is_valid():
						serializers.save()
						return Response(serializers.data, status=status.HTTP_201_CREATED)
				return Response(serializers.errors, status=status.HTTP_400_BAD_REQUEST)



class CalculationUnitsLatest(APIView):
		def get(self,request,  format=None):
				calculation_units = CalculationUnits.get_latest()
				serializers = CalculationUnitsSerializer(calculation_units)
				return Response(serializers.data)

class DonatingByDisease(APIView):
		def get(self,request,  id,format=None):
				calculation_units = Donating.filter_by_disease(id)
				serializers = DonatingSerializer(calculation_units, many=True)
				return Response(serializers.data)


class DiscountedPrice(APIView):
		def get(self, request, id):
			discount_price = CalculationUnits.calculations(id)
			return Response({"discounted_price":discount_price})

class UnitsRemaining(APIView):
		def get(self, request, id):
			units_calculated = CalculationUnits.units_calculated(id)
			return Response({"units_calculated":units_calculated})



class LatestPriceByMedicine(APIView):
		def get(self,request,  id, format=None):
				mediunit = MediUnits.filter_by_medicine(id).last()
				serializers = MediUnitsSerializer(mediunit)
				return Response(serializers.data)