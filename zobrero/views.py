from __future__ import unicode_literals
from django.views import generic
from django.views.generic import View
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.contrib.auth.hashers import check_password , make_password
from django.views.generic.edit import FormView
from django.core.urlresolvers import reverse_lazy , reverse
from django.core.mail import EmailMessage
from django.core import serializers
from django.core.cache import cache
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render , redirect, get_object_or_404
from django.contrib.auth import authenticate , login
from django.http import JsonResponse
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Account, Category, Talent, Employee, WhatDoYouDo, WhatCanYouDo, RecentActivity, TopRated, WhatsNew, Chat, Messenger
from .serializers import AccountSerializer, AddAccountSerializer, SignInSerializer, CategorySerializer, TalentSerializer,EmployeeListSerializer, SearchSerializer, ErrorMessageSerializer, SuccessCodeSerializer, RecentActivitySerializer, TopRatedSerializer, WhatsNewSerializer, ChatClientSerializer, MessageSerializer


IMAGE_FILE_TYPES = ['png', 'jpg', 'jpeg']
VIDEO_FILE_TYPES = ['webm', 'mp4', 'ogg']



def index(request):

    return render(request ,'zobrero/index.html')













class AddAccount(APIView):

    def get(self,request):

        account = Account.objects.all()
        serializer = AddAccountSerializer(account, many=True)

        return Response(serializer.data)

    def post(self,request):
        serializer = AddAccountSerializer(data=request.data)
        if serializer.is_valid():


            firstname = serializer.data['firstname']
            lastname = serializer.data['lastname']
            email = serializer.data['email']
           

            try:

                Account.objects.get(email = email)

                message = 'Oops an account with that username already exist'
                err = {
                    'message' : message
                }
                serializer = ErrorMessageSerializer( err, many=False)

                return Response(serializer.data)

            except:

                pass


            password = serializer.data['password']
            raw_password = password
            password = make_password(password)
            

            user = User()
            user.username = email
            user.password = password
            user.first_name = firstname
            user.last_name = lastname
            user.email = email
            user.save()

            user = authenticate(username=email, password=raw_password)


            if user is not None and user.is_active:

                login(request, user)

                account = Account()
                account.firstname = firstname
                account.lastname = lastname
                account.email = email
                account.password = password
                account.save()


                email = serializer.data['email']
                request.session['email'] = email

                code = 11

                success = {
                    'code' : code
                }

                serializer = SuccessCodeSerializer(success , many = False)

                return Response(serializer.data)

            else:

                error_message = 'Oops login was unsuccesfull, please try again '
                err = {
                    'message' : message
                }
                serializer = ErrorMessageSerializer( err, many=False)

                return Response(serializer.data)





        message = 'hmmhm login was unsuccesfull, please try again '
        err = {
            'message' : message
        }
        serializer = ErrorMessageSerializer( err, many=False)

        return Response(serializer.data)























class SignIn(APIView):

    def get(self,request):
        pass

    def post(self,request):
        serializer = SignInSerializer(data=request.data)
        if serializer.is_valid():

            email = serializer.data['email']
            password = serializer.data['password']

            username = email

            user = authenticate(username=username, password=password)


            if user is not None and user.is_active:
                login(request, user)

                code = 11
                success = {
                    'code' : code
                }

                serializer = SuccessCodeSerializer(success, many = False)

                return Response(serializer)

            else:

                message = 'Oww! username and password did not match '
                err = {
                    'message' : message
                }
                serializer = ErrorMessageSerializer( err, many=False)

                return Response(serializer.data)


        message = 'Input in fields not valid, try again please '

        err = {
            'message' : message
        }
        serializer = ErrorMessageSerializer( err, many=False)

        return Response(serializer.data)














          



class AccountDetail(APIView):

    def get(self,request,account_id):

        try:
            account = Account.objects.get(id=account_id)
        except:
            return Response(status=status.HTTP_404_NOT_FOUND)

        #account = Account.objects.all()
        serializer = AccountSerializer(account, many=False)

        return Response(serializer.data)


    def put(self,request,account_id):
        try:
            account = Account.objects.get(id=account_id)
        except:
            return Response(status=status.HTTP_404_NOT_FOUND)


        serializer = AccountSerializer(account, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self,request,account_id):
        try:
            account = Account.objects.get(id=account_id)
        except:
            return Response(status=status.HTTP_404_NOT_FOUND)


        account.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


















class TalentCategory(APIView):

    def get(self,request):

        category = Category.objects.all()
        serializer =CategorySerializer(category, many=True)

        return Response(serializer.data)

    def post(self,request):
        pass














class AllTalent(APIView):

    def get(self,request,category_id):

        talent = Talent.objects.filter(category_id = category_id)
        serializer = TalentSerializer(talent, many=True)

        return Response(serializer.data)

    def post(self,request):
        pass














class AddEmployeeAccount(APIView):

    def get(self,request):
        pass

    def post(self,request):

        firstname = request.POST.get("firstname","")
        lastname = request.POST.get("lastname","")
        email = request.POST.get("email","")
        password = request.POST.get("password","")
        whatdoyoudo = request.POST.get("whatdoyoudo","")
        whatcanyoudo = request.POST.getlist("whatcanyoudo","")

        try:

            Account.objects.get(email = email)

            message = 'Account with that username already exist'
            err = {
                'message' : message
            }
            serializer = ErrorMessageSerializer( err, many=False)

            return Response(serializer.data)

        except:

            pass

        
        password = serializer.data['password']
        raw_password = password
        password = make_password(password)
            

        user = User()
        user.username = email
        user.password = password
        user.first_name = firstname
        user.last_name = lastname
        user.email = email
        user.save()

        user = authenticate(username=email, password=raw_password)


        if user is not None and user.is_active:

            login(request, user)


            account = Account()
            account.firstname = firstname
            account.lastname = lastname
            account.email = email
            account.phone = "1001"
            account.password = password
            account.save()

            account = Account.objects.get(email = email)

            employee = Employee()
            employee.account = account
            employee.save()

            employee = Employee.objects.get(account=account)
            talent = Talent.objects.get(id = whatdoyoudo)

            whatDyd = WhatDoYouDo()
            whatDyd.employee = employee
            whatDyd.talent = talent
            whatDyd.save()

            for canyoudo in whatcanyoudo :

                talent = Talent.objects.get(id = canyoudo)
                whatCyd = WhatCanYouDo()

                whatCyd.employee = employee
                whatCyd.talent = talent
                whatCyd.save()


            code = 11

            success = {
                'code' : code
            }

            serializer = SuccessCodeSerializer(success , many = False)

            return Response(serializer.data)

















class TopRated(APIView):

    def get(self,request):

        employee = Employee.objects.all()[:4]

        employee_list = []

        for worker in employee :

            worker_account = worker.account_id
            employee_id = worker.id

            try:
                whatDyd = WhatDoYouDo.objects.get(employee_id = employee_id)
                talent_id = whatDyd.talent_id

                talent = Talent.objects.get(id = talent_id)
                talent = talent.adjective

            except:

                talent = "I can work"




            account = Account.objects.get(id = worker_account)
            firstname = account.firstname
            lastname = account.lastname

            context_list = {
                'firstname' : firstname,
                'lastname' : lastname,
                'talent' : talent
            }

            employee_list.append(context_list)

        serializer = EmployeeListSerializer(employee_list, many=True)

        return Response(serializer.data)


















class Search(APIView):

    def get(self,request):

        search_phrase = ""

        first_list = []
        second_list = []

        match_phrase = Talent.objects.filter(talent__icontains = search_phrase)

        for match in match_phrase :

            talent_id = match.id

            whatDyd = WhatDoYouDo.objects.filter(talent_id = talent_id)

            for talent in whatDyd :

                employee_id = talent.employee_id
                employee = Employee.objects.get(id = employee_id)
                account_id = employee.account_id

                account = Account.objects.get(id = account_id)
                firstname = account.firstname
                lastname = account.lastname



                try:
                    what = WhatDoYouDo.objects.get(employee_id = employee_id)
                    talent_id = what.talent_id

                    talent = Talent.objects.get(id = talent_id)
                    talent = talent.adjective

                except:

                    talent = "I can work"

                context_list = {
                    'firstname' : firstname,
                    'lastname' : lastname,
                    'talent' : talent
                }

                first_list.append(context_list)




            whatCyd = WhatCanYouDo.objects.filter(talent_id = talent_id)

            for talent in whatCyd :

                employee_id = talent.employee_id
                employee = Employee.objects.get(id = employee_id)
                account_id = employee.account_id

                account = Account.objects.get(id = account_id)
                firstname = account.firstname
                lastname = account.lastname



                try:
                    what = WhatCanYouDo.objects.get(employee_id = employee_id)
                    talent_id = what.talent_id

                    talent = Talent.objects.get(id = talent_id)
                    talent = talent.adjective

                except:

                    talent = "I can work"

                context_list = {
                    'firstname' : firstname,
                    'lastname' : lastname,
                    'talent' : talent
                }

                second_list.append(context_list)


        first_list += second_list

        serializer = EmployeeListSerializer(first_list, many=True)

        return Response(serializer.data)



    def post(self,request):

        search_phrase = request.POST.get("search_phrase", "")

        first_list = []
        second_list = []

        match_phrase = Talent.objects.filter(talent__icontains = search_phrase)

        for match in match_phrase :

            talent_id = match.id

            whatDyd = WhatDoYouDo.objects.filter(talent_id = talent_id)

            for talent in whatDyd :

                employee_id = talent.employee_id
                employee = Employee.objects.get(id = employee_id)
                account_id = employee.account_id

                account = Account.objects.get(id = account_id)
                firstname = account.firstname
                lastname = account.lastname



                try:
                    what = WhatDoYouDo.objects.get(employee_id = employee_id)
                    talent_id = what.talent_id

                    talent = Talent.objects.get(id = talent_id)
                    talent = talent.adjective

                except:

                    talent = "I can work"

                context_list = {
                    'firstname' : firstname,
                    'lastname' : lastname,
                    'talent' : talent
                }

                first_list.append(context_list)




            whatCyd = WhatCanYouDo.objects.filter(talent_id = talent_id)

            for talent in whatCyd :

                employee_id = talent.employee_id
                employee = Employee.objects.get(id = employee_id)
                account_id = employee.account_id

                account = Account.objects.get(id = account_id)
                firstname = account.firstname
                lastname = account.lastname



                try:
                    what = WhatCanYouDo.objects.get(employee_id = employee_id)
                    talent_id = what.talent_id

                    talent = Talent.objects.get(id = talent_id)
                    talent = talent.adjective

                except:

                    talent = "I can work"

                context_list = {
                    'firstname' : firstname,
                    'lastname' : lastname,
                    'talent' : talent
                }

                second_list.append(context_list)


        first_list += second_list

        serializer = EmployeeListSerializer(first_list, many=True)

        return Response(serializer.data)




class IsLoggedIn(APIView):

    def get(self, request):

        signed_in = False

        if request.user.is_authenticated:

            signed_in = True


        return Response(signed_in)




class GetAccount(APIView):

    def get(self,request):

        if request.user.is_authenticated:
            user = User.objects.get(username = request.user)
            email = user.username



        try:
            account = Account.objects.get(email=email)
            account_id = account.id
        except:
            return Response(status=status.HTTP_404_NOT_FOUND)

        return Response(account_id)

    def post(self, request):
        pass












class RecentActivityView(APIView):

    def get(self, request):

        recent = RecentActivity.objects.all()[:9]

        serializer = RecentActivitySerializer(recent, many=True)

        return Response(serializer.data)



    
    def post(self, request):
        pass




class TopRatedView(APIView):

    def get(self, request):

        top_rated = TopRated.objects.all()[:12]

        serializer = TopRatedSerializer(top_rated, many=True)

        return Response(serializer.data)



    
    def post(self, request):
        pass











class WhatsNewView(APIView):

    def get(self, request):

        whats_new = WhatsNew.objects.all()[:12]

        serializer = WhatsNewSerializer(whats_new, many=True)

        return Response(serializer.data)



    
    def post(self, request):
        pass










class IsMyProfile(APIView):

    def get(self, request, profile_id):

        my_account = False

        if request.user.is_authenticated:
            user = User.objects.get(username = request.user)
            email = user.username

        account = Account.objects.get(email=email)
        account_id = account.id

        if account_id == int(profile_id) :
            my_account = True


        return Response(my_account)

    def post(self, request, profile_id):
        pass






class MyAccountID(APIView):

    def get(self, request):

        if request.user.is_authenticated:
            user = User.objects.get(username = request.user)
            email = user.username

        account = Account.objects.get(email=email)
        account_id = account.id

        return Response(account_id)

    def post(self, request):
        pass













class ResetPhone(APIView):

    def get(self, request):
        pass


    def post(self, request):


        phone = request.POST.get("phone","")

        if request.user.is_authenticated:
            user = User.objects.get(username = request.user)
            email = user.username


        account = Account.objects.get(email=email)
        account.phone = phone
        account.save()

        code = 11

        success = {
            'code' : code
        }

        serializer = SuccessCodeSerializer(success, many = False)

        return Response(serializer.data)












class ResetDP(APIView):

    def get(self, request):
        pass


    def post(self, request):


        profile_pic = request.FILES.get("profile_pic","")

        if request.user.is_authenticated:
            user = User.objects.get(username = request.user)
            email = user.username


        account = Account.objects.get(email=email)
        account.profile_pic = profile_pic
        account.save()

        code = 11

        success = {
            'code' : code
        }

        serializer = SuccessCodeSerializer(success, many = False)

        return Response(serializer.data)














class UpdatePassword(APIView):

    def get(self, request):
        pass


    def post(self, request):


        old_password = request.POST.get("old_password", "")
        new_password = request.POST.get("new_password","")
        confirm_password = request.POST.get("confirm_password","")

        if new_password == confirm_password:

            if request.user.is_authenticated:
                user = User.objects.get(username = request.user)
                email = user.username


                account = Account.objects.get(email=email)
                password = account.password

                if old_password == int(password):

                    account.password = make_password(new_password)
                    account.save()

                    user = User.objects.get(username = email)
                    user.password = make_password(new_password)
                    user.save()

                    code = 11

                    success = {
                        'code' : code
                    }

                    serializer = SuccessCodeSerializer(success, many = False)

                    return Response(serializer.data)


                else:

                    message = 'Invalid old password'

                    err = {
                        'message' : message
                    }

                    serializer = ErrorMessageSerializer(err, many=False)

                    return Response(serializer.data)


        else:

            message = 'Passwords do not match'

            err = {
                'message' : message
            }

            serializer = ErrorMessageSerializer(err, many=False)

            return Response(serializer.data)






















class ChatClients(APIView):

    def get(self, request):

        if request.user.is_authenticated:
            user = User.objects.get(username = request.user)
            email = user.username


        account = Account.objects.get(email = email)
        account_id = account.id

        chats = Chat.objects.filter(account_1 = account_id) | Chat.objects.filter(account_2 = account_id)

        client_register = []
        if chats !=  0 :

            for client in chats:

                client_buffer = []

                if client.account_1_id == account_id :

                    account = Account.objects.get(id = client.account_2)
                    name = account.firstname + ' ' + account.lastname
                    client_id = account.id
                    chat_id = client.id

                    client_buffer = {
                        'name' : name,
                        'client_id' : client_id,
                        'chat_id' : chat_id
                    }

                    client_register.append(client_buffer)

                else:

                    account = Account.objects.get(id = client.account_1_id)
                    name = account.firstname + ' ' + account.lastname
                    client_id = account.id
                    chat_id = client.id

                    client_buffer = {
                        'name' : name,
                        'client_id' : client_id,
                        'chat_id' : chat_id
                    }

                    client_register.append(client_buffer)


        else :
            pass


        serializer = ChatClientSerializer(client_register, many=True)

        return Response(serializer.data)



    def post(self, request):
        pass













class NewChat(APIView):

    def get(self, request, client_id):

        if request.user.is_authenticated:
            user = User.objects.get(username = request.user)
            email = user.username


        try:

            account = Account.objects.get( email = email )
            account_id = account.id

            account_2 = Account.objects.get( id = client_id)

        except:

            message = 'Wrong turn'

            err = {
                'message' : message
            }

            serializer = ErrorMessageSerializer(err, many= False)

            return Response(serializer.data)


        try :

            chat_exist = Chat.objects.get(account_1_id = client_id, account_2 = account_id)
            chat_exist = Chat.objects.get(account_1_id = account_id, account_2 = client_id)

            code = 11

            success = {
                'code' : code
            }

            serializer = SuccessCodeSerializer(success, many= False)

            return Response(serializer.data)

        except :

            chat = Chat()
            chat.account_1 = account
            chat.account_2 = client_id
            chat.save()

            code = 11

            success = {
                'code' : code
            }

            serializer = SuccessCodeSerializer(success, many= False)

            return Response(serializer.data)


    def post(self, request, client_id):

        pass



















class MessengerView(APIView):

    def get(self, request, client_id):

        if request.user.is_authenticated:
            user = User.objects.get(username = request.user)
            email = user.username

      

        account = Account.objects.get(email = email)
        account_id = account.id

        evaluator = 0
        try:

            chat_exist = Chat.objects.get(account_1 = client_id, account_2 = account_id)
            evaluator = 1

        except:
            pass

        try:

            chat_exist = Chat.objects.get(account_1 = account_id, account_2 = client_id)
            evaluator = 1

        except:
            pass


        chat_register = []

        if evaluator == 1:

            try :
                chat = Chat.objects.get(account_1 = client_id, account_2 = account_id)
                chat_id = chat.id

            except :

                chat = Chat.objects.get(account_1 = account_id, account_2 = client_id)
                chat_id = chat.id


            messages = Messenger.objects.filter(chat_id = chat_id)

            for message in messages:

                from_or_to = True

                if int(message.messenger_id) == int(client_id):

                    msg = message.message
                    from_or_to = True

                    chat_buffer = {
                        'msg' : msg,
                        'from_or_to' : from_or_to,
                    }

                    chat_register.append(chat_buffer)

                else :

                    msg = message.message
                    from_or_to = False

                    chat_buffer = {
                        'msg' : msg,
                        'from_or_to' : from_or_to,
                    }

                    chat_register.append(chat_buffer)




            #messages_from = Messenger.objects.filter(ehaggler_id = ehaggler_id, messenger = client_id)
            #messages_to = Messenger.objects.filter(ehaggler_id = ehaggler_id, messenger = account_id)



        else :

           message = 'Oops something went wrong, mmhmm'
           err = {
               'message' : message
           }

           serializer = ErrorMessageSerializer(err, many= False)

           return Response(serializer.data)


        serializer = MessageSerializer(chat_register, many=True)

        return Response(serializer.data)


    def post(self, request, client_id):
        pass















class SendMessage(APIView):

    def get(self, request, client_id):
        pass

    def post(self, request, client_id):

        if request.user.is_authenticated:
            user = User.objects.get(username = request.user)
            email = user.username


        account = Account.objects.get(email = email)
        account_id = account.id

        status = 0

        try :

            chat = Chat.objects.get(account_2 = client_id, account_1_id = account_id)

            status = 1

        except:
            pass


        if status == 0:
            try:

                chat = Chat.objects.get(account_2 = account_id, account_1_id = client_id)
                status = 1

            except:
                pass



        msg = request.POST.get("message","")


        if msg:
            pass

        else:
            msg="Angel"

        messenger = Messenger()
        messenger.chat = chat
        messenger.message = msg
        messenger.messenger = account
        messenger.save()


        messages = Messenger.objects.filter(chat_id = chat.id)
        chat_register = []


        if True :
            for message in messages:

                from_or_to = True

                if message.messenger == client_id :

                    msg = message.message
                    from_or_to = True

                    chat_buffer = {
                        'msg' : msg,
                        'from_or_to' : from_or_to,
                    }

                    chat_register.append(chat_buffer)

                else :

                    msg = message.message
                    from_or_to = False

                    chat_buffer = {
                        'msg' : msg,
                        'from_or_to' : from_or_to,
                    }

                    chat_register.append(chat_buffer)

            else:
                pass

        serializer = MessageSerializer(chat_register, many=True)

        return Response(serializer.data)














class UnreadMessages(APIView):

    def get(self, request):

        if request.user.is_authenticated:
            user = User.objects.get(username = request.user)
            email = user.username

        else:
            email = 'dretzam@gmail.com'

        account = Account.objects.get( email = email )
        account_id = account.id


        unread_msg = Chat.objects.filter(account_1 = account_id) | Chat.objects.filter(account_2 = account_id)

        count = 0
        for msg in unread_msg :

            if Messenger.objects.filter(chat_id = msg.id, messenger_id = account_id).exists:
                pass

            else:

                unread = Messenger.objects.filter(chat_id = msg.id, seen = False).count

                count += unread



        code = count

        success = {
            'code' : code
        }

        serializer = SuccessCodeSerializer(success, many = False)

        return Response(serializer.data)


    def post(self, request):
        pass










