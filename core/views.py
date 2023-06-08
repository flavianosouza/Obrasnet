from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.models import User
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from django.utils.encoding import force_bytes, force_str
from . tokens import generate_token

# Create your views here.

# Home page for url '/'

def index(request):
    return render(request, 'index.html')

# Login, Logout, Register page

## Register
def signup(request, *args, **kwargs):
    if request.method == 'POST':
        username = request.POST['username']
        first_name = request.POST['fname']
        last_name = request.POST['lname']
        email = request.POST['email']
        pass1 = request.POST['pass1']
        pass2 = request.POST['pass2']

        if User.objects.filter(username=username):
            messages.error(request, 'Username already exist! Please try some other name.')
        
        if User.objects.filter(email=email):
            messages.error(request, 'Email already registered!')
        
        if len(username) > 20:
            messages.error(request, "Username must be under 20 characters")

        if pass1 != pass2:
            messages.error(request, "Passwords do not match")

        if not username.isalnum():
            messages.error(request, "Username must be Alpha-numeric")

        myuser = User.objects.create_user(username, email, pass1)
        myuser.first_name = first_name
        myuser.last_name = last_name
        myuser.is_active = True

        myuser.save()

        messages.success(request, "Your account has been successfully created. We have sent you a confirmation email, please confirm your email in order to activate your account.")

        # Welcome Email
        # subject = "Welcome to Obrasnet!"
        # message = "Hello " + myuser.first_name + "!! \n" + "Thank you for visiting our website. \n We have to also sent you a confirmation email, please confirm your email address in order to activate your account. \n\n Thank you. \n Flaviano Souza."

        # from_email = settings.EMAIL_HOST_USER
        # to_list = [myuser.email]

        # send_mail(subject, message, from_email, to_list, fail_silently=True)

        # Email Address Confirmation Address
        
        # current_site = get_current_site(request)
        # email_subject = "Confirm your email @ Obrasnet"
        # message2 = render_to_string('email_confirmation.html'), {
        #     'name': myuser.first_name,
        #     'domain': current_site.domain,
        #     'uid': urlsafe_base64_encode(force_bytes(myuser.pk)),
        #     'token': generate_token.make_token(myuser)
        # }

        # email = EmailMessage(
        #     email_subject,
        #     message2,
        #     settings.EMAIL_HOST_USER,
        #     [myuser.email]
        # )
        # email.fail_silently = True
        # email.send()
        
        return redirect('signin')

    return render(request, 'auth/signup.html')

## Activate Email
def activate(request, uid64, token):
    try:
        uid = force_str(urlsafe_base64_encode(uid64))
    except (TypeError, ValueError, OverflowError, User.DoesNotExist):
        myuser = None
    
    if myuser is not None and generate_token.check_token(myuser, token):
        myuser.is_active = True
        myuser.save()
        login(request, myuser)
        return redirect('home')
    else:
        return render(request, 'activation_failed.html')

## Login
def signin(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return render(request, 'index.html', {'username': user.username})
        else:
            messages.error(request, 'Invalid username or password')
        
    return render(request, 'auth/signin.html')

## Logout
def signout(request):
    logout(request)

    # messages.success(request, "Log out successfully")

    return redirect('home')

# Expert Management Page
def ExpertManagement(request):
    return render(request, 'expert_manage.html')