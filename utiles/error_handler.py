from django.http import JsonResponse

def handler404(request,exception):
    messege = 'path not found check your url'
    response = JsonResponse(data={'error':messege})
    response.status_code = 404
    return response

def handler500(request):
    message = 'server error check the server first'
    response = JsonResponse(data={'error':message})
    response.status_code = 500
    return response