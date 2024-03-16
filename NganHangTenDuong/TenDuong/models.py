from django.db import models
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.conf import settings
from django import forms

class CreateUserForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'email', 'first_name', 'last_name', 'password1', 'password2']

    def clean_username(self):
        # Kiểm tra tính duy nhất của tên người dùng
        username = self.cleaned_data['username']
        if User.objects.filter(username=username).exists():
            raise forms.ValidationError('Tên người dùng đã tồn tại.')
        return username

    def clean_email(self):
        # Kiểm tra tính duy nhất của địa chỉ email
        email = self.cleaned_data['email']
        if User.objects.filter(email=email).exists():
            raise forms.ValidationError('Email đã tồn tại.')
        return email

    # def clean(self):
    #     cleaned_data = super().clean()
    #     password1 = cleaned_data.get("password1")
    #     password2 = cleaned_data.get("password2")
    #
    #     if password1 != password2:
    #         raise forms.ValidationError("Mật khẩu và Mật khẩu xác nhận không khớp.")
    def clean_password2(self):
        # Kiểm tra tính hợp lệ của "Mật khẩu xác nhận"
        password1 = self.cleaned_data.get("password1")
        password2 = self.cleaned_data.get("password2")
        if password1 and password2 and password1 != password2:
            raise forms.ValidationError("Mật khẩu và Mật khẩu xác nhận không khớp.")
        return password2

# @receiver(post_save, sender=User)
# def create_user_profile(sender, instance, created, **kwargs):
#     if created:
#         UserProfile.objects.create(user=instance)
#         # Kiểm tra xem avatar đã được thiết lập hay chưa
#         if not UserProfile.avatar:
#             # Đặt avatar bằng hình ảnh mặc định
#             UserProfile.avatar = settings.MEDIA_URL + 'avatars/ava.jpg'
#             UserProfile.save()
@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        user_profile = UserProfile.objects.create(user=instance)
        # Kiểm tra xem avatar đã được thiết lập hay chưa
        if not user_profile.avatar:
            # Đặt avatar bằng hình ảnh mặc định
            user_profile.avatar = 'avatars/ava.jpg'
            user_profile.save()

@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
    instance.userprofile.save()

class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    full_name = models.CharField(max_length=100)
    birthdate = models.DateField(null=True, blank=True)
    avatar = models.ImageField(upload_to='avatars/', null=True, blank=True)

    def __str__(self):
        return self.user.username

class Source(models.Model):
    source_docID = models.CharField(max_length=10, primary_key=True)
    source_name = models.CharField(max_length=250)
    abstract_source = models.TextField()
    history = models.TextField()
    image = models.CharField(max_length=200)
    note = models.CharField(max_length=400)

class StreetType(models.Model):
    type_streetID = models.CharField(max_length=10, primary_key=True)
    type_name = models.CharField(max_length=250)
    abstract_type = models.TextField()
    document_regulation = models.CharField(max_length=300)
    note = models.CharField(max_length=400)

class StreetGroup(models.Model):
    group_streetID = models.CharField(max_length=10, primary_key=True)
    group_name = models.CharField(max_length=250)
    number_member = models.IntegerField()
    description = models.TextField()
    note = models.CharField(max_length=400)

class Address(models.Model):
    id_address = models.CharField(max_length=10, primary_key=True)
    ward_name = models.CharField(max_length=200)
    district_name = models.CharField(max_length=200)
    square = models.CharField(max_length=50)
    population = models.CharField(max_length=15)
    description = models.TextField()
    note = models.CharField(max_length=400)

class Street(models.Model):
    street_name = models.CharField(max_length=250, primary_key=True)
    abstract = models.TextField()
    content = models.CharField(max_length=450)
    source_docID = models.ForeignKey(Source, on_delete=models.CASCADE)
    type_streetID = models.ForeignKey(StreetType, on_delete=models.CASCADE)
    group_streetID = models.ForeignKey(StreetGroup, on_delete=models.CASCADE)
    id_address = models.ForeignKey(Address, on_delete=models.CASCADE)
    position = models.CharField(max_length=100)
    # length = models.IntegerField()
    # width = models.IntegerField()
    length = models.FloatField()  # Thay đổi IntegerField thành FloatField
    width = models.FloatField()   # Thay đổi IntegerField thành FloatField
    lane_number = models.IntegerField()
    google_map = models.CharField(max_length=200)
    note = models.CharField(max_length=400)
    image1 = models.ImageField(upload_to='image/', null=True, blank=True)
    street_mapid = models.CharField(max_length=100, null=True)

class Permission(models.Model):
    active_status = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    role = models.CharField(max_length=20)

    def __str__(self):
        return f"{self.user.username} - {self.role}"

