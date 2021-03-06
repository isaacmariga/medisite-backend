from rest_framework import serializers
from .models import User, Supplier, Medicine, Donating, Purchasing, Prescription, Disease, MediUnits, CalculationUnits


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'email', 'password']
        extra_kwargs = {
            'password': {'write_only': True}
        }

    def create(self, validated_data):
        password = validated_data.pop('password', None)
        instance = self.Meta.model(**validated_data)
        if password is not None:
            instance.set_password(password)
        instance.save()
        return instance


class SupplierSerializer(serializers.ModelSerializer):
    class Meta:
      model = Supplier
      fields = ('name', 'email', 'location', 'phone_number','category','profile_pic','bio','password')

class MedicineSerializer(serializers.ModelSerializer):
    class Meta:
      model = Medicine
      fields = ('id','name', 'disease', 'description', 'picture')

class DonatingSerializer(serializers.ModelSerializer):
    class Meta:
      model = Donating
      fields = ('donation_amount', 'phone_number','email', 'donor','disease')

class PurchasingSerializer(serializers.ModelSerializer):
    class Meta:
      model = Purchasing
      fields = ('units_sold', 'buyer', 'medicine', 'phone_number','email', 'delivery_location')

class PrescriptionSerializer(serializers.ModelSerializer):
    class Meta:
      model = Prescription
      fields = ('picture', 'buyer', 'medicine')

class DiseaseSerializer(serializers.ModelSerializer):
    class Meta:
      model = Disease
      fields = ('id','name','picture')

class MediUnitsSerializer(serializers.ModelSerializer):
    class Meta:
      model = MediUnits
      fields = ('medicine','units', 'set_price')
class CalculationUnitsSerializer(serializers.ModelSerializer):
    class Meta:
      model = CalculationUnits
      fields = ('units_sold','units','medicine_id', 'set_price','disease_id', 'donation_amount')
