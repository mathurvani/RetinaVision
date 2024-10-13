from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login as auth_login
from django.contrib.auth.forms import UserCreationForm
from django.core.files.storage import default_storage
from django.core.files.base import ContentFile

# Login view
def login_view(request):
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            auth_login(request, user)
            return redirect('home')  # Redirect to home page after successful login
        else:
            # Return an 'invalid login' error message
            return render(request, 'login.html', {'login_error': 'Invalid username or password'})
    
    return render(request, 'login.html')

# Register view
def register_view(request):
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')  # Redirect to login page after successful registration
    else:
        form = UserCreationForm()

    # Pass the form and a context variable to indicate registration form should be shown
    return render(request, 'login.html', {'form': form, 'show_registration': True})

# Image upload view
def upload_image_view(request):
    if request.method == "POST" and request.FILES.get('imageUpload'):
        image = request.FILES['imageUpload']
        file_name = default_storage.save(image.name, ContentFile(image.read()))
        # Process the uploaded image (e.g., save to database, analyze, etc.)
        return redirect('preview')  # Redirect after successful upload

    return render(request, 'upload_image.html')  # Update to the appropriate template for image upload

# Home view
def home_view(request):
    return render(request, 'index.html')

# Preview view
def preview_view(request):
    return render(request, 'preview.html')

# Performance analysis view
def performance_analysis_view(request):
    return render(request, 'performance_analysis.html')
