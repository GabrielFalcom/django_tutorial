from django.forms import ModelForm
from projeto.models import UserProfile

class EditProfileForm(ModelForm):
    class Meta:
        model = UserProfile
        fields = (
            'usuario',
            'matricula',
            'cr',
            'nome',
            'cpf',
            'empresa',
            'email',
        )

    def save(self, commit=True):
        user = super(EditProfileForm, self).save(commit=False)
        UserProfile.save(user)
        return user
