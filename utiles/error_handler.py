from django.http import JsonResponse

def handler404(request,exception):
    messege = 'path not found check your url'
    response = JsonResponse(data={'error':messege})
    response.status_code = 404
    return response