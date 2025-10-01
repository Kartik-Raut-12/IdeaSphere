# from django.http import HttpResponse
# from rest_framework import status
# from rest_framework.decorators import api_view
# from rest_framework.response import Response
#
# @api_view(['GET'])
# def hello(request):
#     name = request.GET.get('name', 'guest')
#     data = {
#         'name': name,
#         'message': f"Hello {name}, your first API endpoint has been created successfully!"
#     }
#     return Response(data, status=status.HTTP_200_OK)
# def hello1(request):
#     name = request.GET.get('name')
#     return HttpResponse(f"Hello World! {name}")

from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_POST
import json
import sqlite3
import os
from dotenv import load_dotenv
from openai import OpenAI


# Load .env
load_dotenv()


@csrf_exempt  # Disable CSRF protection for this example (see note below)
def my_api_endpoint(request):
    if request.method == 'POST':
        try:
            data = json.loads(request.body)  # Parse JSON data from the request body
            # Process the data (e.g., save to database, perform calculations)
            received_data = data.get('myData', None)  # Access a specific field

            if received_data:
                response_data = {'status': 'success', 'message': 'Data received', 'received_data': received_data}
            else:
                response_data = {'status': 'error', 'message': 'myData field missing'}

            return JsonResponse(response_data)

        except json.JSONDecodeError:
            return JsonResponse({'status': 'error', 'message': 'Invalid JSON data'}, status=400)
    else:
        return JsonResponse({'status': 'error', 'message': 'Method not allowed'}, status=405)
    
@csrf_exempt
@require_POST
def getFromOpenAI(request):
    try:
        data = json.loads(request.body)
        received_data = data.get('myData', None)

        if received_data:
            # client = OpenAI(
            #     api_key="REMOVED
            # )
            client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))
            print("Loaded API KEY:", os.getenv("OPENAI_API_KEY"))

            
            completion = client.chat.completions.create(
                model="gpt-4o-mini",
                messages=[{"role": "user", "content": received_data}]
            )

            ans = completion.choices[0].message.content

            response_data = {
                'status': 'success',
                'message': 'Data received',
                'received_data': ans
            }
        else:
            response_data = {'status': 'error', 'message': 'myData field missing'}

        return JsonResponse(response_data)

    except json.JSONDecodeError:
        return JsonResponse({'status': 'error', 'message': 'Invalid JSON data'}, status=400)


@csrf_exempt
@require_POST
def saveInDatabase(request):
    try:
        data = json.loads(request.body)
        name_arg = data.get('name', None)
        age_arg = data.get('age', None)
        db = sqlite3.connect('db.sqlite3')
        cursor = db.cursor()
        cursor.execute("insert into testTable values('"+name_arg+"','"+str(age_arg)+"')")
        db.commit()


        response_data = {'status': 'error', 'message': 'Record Save in Database'}
        return JsonResponse(response_data)

    except json.JSONDecodeError:
        return JsonResponse({'status': 'error', 'message': 'Invalid JSON data'}, status=400)



@csrf_exempt
@require_POST
def getAddition(request):
    try:
        data = json.loads(request.body)
        val1 = data.get('number1', None)
        val2 = data.get('number2', None)
        ans=float(val1) + float(val2)
        response_data = {
                'status': 'success',
                'message': 'Data received',
                'received_data': ans
            }
        return JsonResponse(response_data)
    except json.JSONDecodeError:
        return JsonResponse({'status': 'error', 'message': 'Invalid JSON data'}, status=400)
    