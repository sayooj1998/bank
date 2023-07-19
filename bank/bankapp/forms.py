import self as self
from django import forms
from .models import details, Person, City



class PersonCreationForm(forms.ModelForm):
    name = forms.CharField()
    dob = forms.DateField()
    age = forms.CharField(max_length=2)
    phone = forms.CharField(max_length=12)
    email = forms.EmailField()
    address = forms.CharField(max_length=150)
    GENDER_CHOICES = (
        ('M', 'Male'),
        ('F', 'Female'),
        ('O', 'Other'),
    )

    gender= forms.ChoiceField(choices=GENDER_CHOICES, widget=forms.RadioSelect)

    MATERIAL_CHOICES = (
        ('D', 'Debit Card'),
        ('C', 'Credit Card'),
        ('Ch', 'Cheque book'),
    )

    material = forms.ChoiceField(choices=MATERIAL_CHOICES, widget=forms.RadioSelect)

    class Meta:
        model = Person
        fields = '__all__'



    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['city'].queryset = City.objects.none()

        if 'country' in self.data:
            try:
                country_id = int(self.data.get('country'))
                self.fields['city'].queryset = City.objects.filter(country_id=country_id).order_by('name')
            except (ValueError, TypeError):
                pass  # invalid input from the client; ignore and fallback to empty City queryset
        elif self.instance.pk:
            self.fields['city'].queryset = self.instance.country.city_set.order_by('name')