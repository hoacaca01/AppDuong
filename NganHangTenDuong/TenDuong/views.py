from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404, redirect
from .models import User, Street, Source, StreetType, StreetGroup, Address, Permission
from django.contrib.auth.decorators import login_required
from django.contrib import messages

def home(request):
    streets = Street.objects.all()
    sources = Source.objects.all()
    street_types = StreetType.objects.all()
    street_groups = StreetGroup.objects.all()
    addresses = Address.objects.all()

    context = {
        'streets': streets,
        'sources': sources,
        'street_types': street_types,
        'street_groups': street_groups,
        'addresses': addresses,
    }
    return render(request, 'TenDuong/home.html', context)
def chitiet(request):
    streets = Street.objects.all()
    sources = Source.objects.all()
    street_types = StreetType.objects.all()
    street_groups = StreetGroup.objects.all()
    addresses = Address.objects.all()

    context = {
        'streets': streets,
        'sources': sources,
        'street_types': street_types,
        'street_groups': street_groups,
        'addresses': addresses,
    }
    return render(request, 'TenDuong/chitiet.html', context)
@login_required
def user_profile(request):
    user = request.user
    # Lấy thông tin user và hiển thị trang profile
    context = {'user': user}
    return render(request, 'TenDuong/profile.html', context)

# @login_required
def street_list(request):
    streets = Street.objects.all()
    context = {'streets': streets}
    return render(request, 'TenDuong/street_list.html', context)

# @login_required
def street_detail(request, street_id):
    street = get_object_or_404(Street, id=street_id)
    context = {'street': street}
    return render(request, 'TenDuong/street_detail.html', context)


# @login_required
def search(request):
    if request.method == 'POST':
        query_street_name = request.POST.get('ten-duong')
        query_source = request.POST.get('source')
        query_street_type = request.POST.get('street-type')
        query_street_group = request.POST.get('street-group')
        query_address = request.POST.get('address')

        streets = Street.objects.all()

        if query_street_name:
            streets = streets.filter(street_name__icontains=query_street_name)
        if query_source:
            streets = streets.filter(source_docID=query_source)
        if query_street_type:
            streets = streets.filter(type_streetID=query_street_type)
        if query_street_group:
            streets = streets.filter(group_streetID=query_street_group)
        if query_address:
            streets = streets.filter(id_address=query_address)

        sources = Source.objects.all()
        street_types = StreetType.objects.all()
        street_groups = StreetGroup.objects.all()
        addresses = Address.objects.all()

        context = {
            'streets': streets,
            'sources': sources,
            'street_types': street_types,
            'street_groups': street_groups,
            'addresses': addresses,
        }
        return render(request, 'TenDuong/search_results.html', context)
    return render(request, 'TenDuong/home.html')
# @login_required
def source_list(request):
    sources = Source.objects.all()
    context = {'sources': sources}
    return render(request, 'TenDuong/source_list.html', context)

# @login_required
def source_detail(request, source_id):
    source = get_object_or_404(Source, source_docID=source_id)
    context = {'source': source}
    return render(request, 'TenDuong/source_detail.html', context)

# @login_required
def street_type_list(request):
    street_types = StreetType.objects.all()
    context = {'street_types': street_types}
    return render(request, 'TenDuong/street_type_list.html', context)

# @login_required
def street_type_detail(request, type_id):
    street_type = get_object_or_404(StreetType, type_streetID=type_id)
    context = {'street_type': street_type}
    return render(request, 'TenDuong/street_type_detail.html', context)

# @login_required
def street_group_list(request):
    street_groups = StreetGroup.objects.all()
    context = {'street_groups': street_groups}
    return render(request, 'TenDuong/street_group_list.html', context)

# @login_required
def street_group_detail(request, group_id):
    street_group = get_object_or_404(StreetGroup, group_streetID=group_id)
    context = {'street_group': street_group}
    return render(request, 'TenDuong/street_group_detail.html', context)

# @login_required
def address_list(request):
    addresses = Address.objects.all()
    context = {'addresses': addresses}
    return render(request, 'TenDuong/address_list.html', context)

# @login_required
def address_detail(request, address_id):
    address = get_object_or_404(Address, id_address=address_id)
    context = {'address': address}
    return render(request, 'TenDuong/address_detail.html', context)