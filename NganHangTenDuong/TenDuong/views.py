from django.http import HttpResponse, JsonResponse
from django.shortcuts import render, get_object_or_404, redirect
from .models import Street, Source, StreetType, StreetGroup, Address
from .models import CreateUserForm, UserProfile
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.urls import reverse_lazy
from .forms import UserProfileForm, YourStreetForm


def register(request):
    form = CreateUserForm()
    if request.method == 'POST':
        form = CreateUserForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Tài khoản đã được tạo thành công.')

    context = {'form': form}
    return render(request, 'TenDuong/register.html', context)

def login_view(request):
    if request.user.is_authenticated:
        return redirect(reverse_lazy('TenDuong:home'))

    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect(reverse_lazy('TenDuong:home'))
        else:
            messages.error(request, 'Tài khoản hoặc mật khẩu không đúng.')

    return render(request, 'TenDuong/login.html')

def logout_view(request):
    logout(request)
    return redirect(reverse_lazy('TenDuong:login'))

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
    if request.user.is_authenticated:
        context['user_authenticated'] = True
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
# @login_required
# def user_profile(request):
#     user = request.user
#     # Lấy thông tin user và hiển thị trang profile
#     context = {'user': user}
#     return render(request, 'TenDuong/profile.html', context)

# @login_required
def street_list(request):
    streets = Street.objects.all()
    context = {'streets': streets}
    if request.user.is_authenticated:
        context['user_authenticated'] = True
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
        if request.user.is_authenticated:
            context['user_authenticated'] = True
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

@login_required
def profile(request):
    # Truy cập thông tin tài khoản người dùng đã đăng nhập
    user = request.user

    # Kiểm tra xem có mô hình UserProfile liên kết với tài khoản người dùng không
    try:
        user_profile = UserProfile.objects.get(user=user)
    except UserProfile.DoesNotExist:
        user_profile = None

    context = {
        'user_profile': user_profile,
    }
    if request.user.is_authenticated:
        context['user_authenticated'] = True
    return render(request, 'TenDuong/profile.html', context)

@login_required
def edit_profile(request):
    if request.method == 'POST':
        form = UserProfileForm(request.POST, request.FILES, instance=request.user.userprofile)
        if form.is_valid():
            form.save()
            return redirect(reverse_lazy('TenDuong:profile'))  # Chuyển hướng đến trang profile sau khi lưu thành công
    else:
        form = UserProfileForm(instance=request.user.userprofile)

    return render(request, 'TenDuong/edit_profile.html', {'form': form})

@login_required
def edit_allStreet(request):
    streets = Street.objects.all()  # Lấy tất cả các đường

    if request.method == 'POST':
        print("đã post dữ liệu thành công")
        forms = [YourStreetForm(request.POST, instance=street) for street in streets]
        if all(form.is_valid() for form in forms):
            print("FORM HỢP LỆ")
            for form in forms:
                form.save()
                print("LƯU DỮ LIỆU form TC ")
            return redirect(reverse_lazy('TenDuong:street_list'))  # Chuyển hướng đến danh sách đường sau khi lưu thành công
        else:
            print("FORM KHÔNG HỢP LỆ:")
    else:
        forms = [YourStreetForm(instance=street) for street in streets]

    return render(request, 'TenDuong/edit_allStreet.html', {'forms': forms})

@login_required
def edit_search_result(request, street_name):
    street = get_object_or_404(Street, street_name=street_name)

    if request.method == 'POST':
        form = YourStreetForm(request.POST, instance=street)
        if form.is_valid():
            form.save()
            return redirect(reverse_lazy('TenDuong:street_list'))  # Chuyển hướng đến trang chi tiết sau khi lưu thành công
    else:
        form = YourStreetForm(instance=street)

    return render(request, 'TenDuong/edit_street.html', {'form': form})
