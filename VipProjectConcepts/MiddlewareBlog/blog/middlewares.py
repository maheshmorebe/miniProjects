
# Function based middleware
#
# def my_middleware(get_response):
#     print("One time init")
#     def my_func(request):
#         print("Before view")
#         response = get_response(request)
#         print("after view")
#         return response
#     return my_func


# Class based single middleware

# class MyMiddleware(object):
#     def __init__(self,get_response):
#         # one time initialization
#         print("In init function---- one time initialization")
#         self.get_response = get_response
#
#     def __call__(self,request, *args, **kwargs):
#         print("Before view function called...")
#         response = self.get_response(request)
#         print("After view function called...")
#         return response

from django.shortcuts import HttpResponse

class MyProcessMiddleware(object):
    def __init__(self,get_response):
        self.get_response = get_response

    def __call__(self,request, *args, **kwargs):
        response = self.get_response(request)
        return response

    def process_view(self,request,*args,**kwargs):
        print("This is Process view before view")
        #return HttpResponse("This is before view")
        return None                        #if return None that means it will go to the view.py and exexute function

    def process_exception(self,request,exception):
        print(" exception...... ")
        msg = exception
        return HttpResponse(msg)








