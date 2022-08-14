from django.contrib.auth.forms import UserCreationForm
from .models import User

class SignUpForm(UserCreationForm):
    class Meta:
        model = User 
        fields = ['username','password1','password2','i_am', 'first_name','last_name','dob','year_of_passing','course_studied','additional_qualifications',
        'present_position_held','special_contribution','profile_pic']