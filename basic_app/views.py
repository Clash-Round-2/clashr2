from django.shortcuts import render
from basic_app.models import Questions,UserProfileInfo
from basic_app.models import User
from django.urls import reverse
import os


from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponseRedirect, HttpResponse

path='/home/elliot/PycharmProjects/proj/basic_app/Users_code'
from django.contrib.auth.decorators import login_required



def index(request):
    return render(request,'basic_app/index.html')
def test():
    a=UserProfileInfo.objects.get(user=user_login.user)

    print(a)
    total=(a.quest1test+a.quest2test+a.quest3test+a.quest4test+a.quest5test)//5
    return total


def questions(request,id=0):#abcd

    a = Questions.objects.all()
    questions.s=int(id)
    Q = a[questions.s]
    q = Q.questions
    dict = {'q': q}

    if request.method =="POST":
        some_text = request.POST.get('text')
        option= request.POST.get('lang')
        os.chdir(path)
        print(os.system('pwd'))
        os.system('mkdir {}'.format(user_login.user))



        fo = open('{}/{}.{}'.format(user_login.user,user_login.user,option), 'w')
        fo.write(some_text)
        fo.close()
        os.chdir(path+'/{}'.format(user_login.user))
        if os.path.exists('{}.c'.format(user_login.user)):
            os.system('cc -o {} {}.c'.format(user_login.user,user_login.user))
            os.system('./{} < input.txt > output.txt'.format(user_login.user))
            foo = open('output.txt', 'r')
            output=foo.readlines()
            user_output=list(output)
            fool = open('expected_output.txt', 'r')
            output2=fool.readlines()
            expected_output=list(output2)
            score=0
            a=0
            print(expected_output)
            for i in user_output:

                if int(i)==int(expected_output[a]):
                    print(int(i))
                    a+=1
                    score+=10
                else:a+=1

            if int(id)==0:
                ans1= UserProfileInfo.objects.get(user=user_login.user)
                ans1.quest1test=score
                ans1.totaltest=test()
                ans1.save()
            elif (id)==1:
                ans2=UserProfileInfo(quest2test = score)
                ans2.save()

            elif (id)==2:
                ans3=UserProfileInfo(quest3test = score)
                ans3.save()
            elif (id)==3:
                ans4=UserProfileInfo(quest4test=score)
                ans4.save()
            elif (id)==4:
                ans5=UserProfileInfo(quest5test=score)
                ans5.save()



            print(score)







        dictt={'c':some_text,'q':q,'s':score}

        return render(request, 'basic_app/codingpage.html',context=dictt)
    return render(request, 'basic_app/codingpage.html', context=dict)


def question_panel(request):
    return render(request,'basic_app/questions.html')




def leader(request):
    a=UserProfileInfo.objects.order_by("score")
    b=a.reverse()
    dict={'list':b}
    return render(request,'basic_app/leader.html',context=dict)









def user_logout(request):

    logout(request)

    return render(request,'basic_app/index.html')

def register(request):




    if request.method == 'POST':
        username = request.POST.get('name')
        password= request.POST.get('password')
        a= User.objects.create_user( username=username, password=password)


        a.save()
        b=UserProfileInfo()
        b.user=a
        b.save()

        return render(request,'basic_app/page_after_registration.html')

    return render(request,'basic_app/registration.html')


def user_login(request):

    if request.method == 'POST':

        username = request.POST.get('name')
        password= request.POST.get('password')
        user_login.user=authenticate(username=username,password=password)







        if user_login.user is not None:
            if user_login.user.is_active:
                login(request, user_login.user)

            return HttpResponseRedirect(reverse('basic_app:questions'))

        else:


            return HttpResponse("Invalid login details supplied.")

    else:

        return render(request, 'basic_app/login.html', {})

