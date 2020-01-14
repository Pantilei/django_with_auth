from django.shortcuts import render,redirect
from django.contrib.auth.forms import UserCreationForm,AuthenticationForm
from django.contrib.auth import login,logout

# Create your views here.
def signup_view(request): # This function will be fired even with HTTP POST request in accounts/signup
    if request.method =='POST': # By doing this we check wheter it was a POST request or GET request
        form=UserCreationForm(request.POST) # Data is taken from POST request in order to be validated
        if form.is_valid():# is_valid is a method that we can use on form, which returns TRUE or FALSE
            user=form.save()# Save data to database if it is new user

            login(request, user)
            return redirect('articles:list')
    else: # in case if it is GET request send the blanck page of URL http://127.0.0.1:8000/articles/signup/
        form=UserCreationForm()

    return render(request,'accounts/signup.html', {'form':form}) # return yhis value in case of GET request
def login_view(request):
    if request.method == 'POST': #in case if we make a POST request(we send our user data,name and passward, to server)
        form = AuthenticationForm(data=request.POST)#data is taken from POST request and assigned to form
        if form.is_valid():# if user exists this condition is satisfied
            user=form.get_user()# form is instance of class AuthenticationForm which has method get_user
            login(request, user)# loges user in
            if 'next' in request.POST:
                #when we go to articles/create we are redirected to accounts/login , but in this case this URL appears (http://127.0.0.1:8000/accounts/login/?next=/articles/create/) instead of http://127.0.0.1:8000/accounts/login/
                # if there is next in POST request
                return redirect(request.POST.get('next'))# we will be redirected to /articles/create/
            else:
                return redirect('articles:list')# if we just wanna log in we will be redirected to articles:list URL

    else:#if we go directly to accounts/login/ empty form will be rendered (GET request)
        form = AuthenticationForm()
    return render(request, 'accounts/login.html',{'form':form})#if any other mistake happens empty from will render

def logout_view(request):
    if request.method=='POST':
        logout(request)
        return redirect('articles:list')
