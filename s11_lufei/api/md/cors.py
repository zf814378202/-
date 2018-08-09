from django.utils.deprecation import MiddlewareMixin
from django.conf import settings
class CorsMiddleware(MiddlewareMixin):
    def process_response(self,request,response):
        response['Access-Control-Allow-Origin'] = 'http://localhost:8080'
        if request.method == "PUT,DELETE":
            response["Access-Control-Allow-Methods"] = "PUT,DELETE"
            response["Access-Control-Allow-Headers"] = "Content-Type,xxxxx"
        return response
