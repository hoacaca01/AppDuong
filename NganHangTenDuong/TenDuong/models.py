from django.db import models

class User(models.Model):
    full_name = models.CharField(max_length=250)
    username = models.CharField(max_length=250)
    password = models.CharField(max_length=100)
    department = models.CharField(max_length=100)
    position = models.CharField(max_length=150)
    email = models.CharField(max_length=150)
    phone = models.CharField(max_length=20)
    usertype = models.CharField(max_length=200)
    active_status = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    language = models.CharField(max_length=200)
    style_id = models.IntegerField()
    verified = models.CharField(max_length=200)

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
    length = models.IntegerField()
    width = models.IntegerField()
    lane_number = models.IntegerField()
    google_map = models.CharField(max_length=200)
    note = models.CharField(max_length=400)

class Permission(models.Model):
    active_status = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    role = models.CharField(max_length=20)

    def __str__(self):
        return f"{self.user.username} - {self.role}"

