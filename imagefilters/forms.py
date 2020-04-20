from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.forms import ModelForm


from .models import UserOriginalImage, UserEditedImage

class CreateUserForm(UserCreationForm):

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']


class UploadImagesForm(ModelForm):

    class Meta:
        model = UserOriginalImage
        fields = '__all__'


class EditImagesForm(ModelForm):

    class Meta:
        model = UserEditedImage
        fields = ['filter_type']