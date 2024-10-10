     
# from django.conf import settings
# from django.shortcuts import render
# from django.http import JsonResponse, HttpResponse
# from rest_framework.decorators import api_view
# from django.views.decorators.csrf import csrf_exempt
# import pickle
# import numpy as np
# import os


# # Load the RandomForestClassifier model
# filename = os.path.join(settings.BASE_DIR, 'D:/Brain Stroke Analysis_Project/RandomForestClassifier-model.pkl')
# with open(filename, 'rb') as model_file:
#     model = pickle.load(model_file)

# # Django view for rendering the main page
# @api_view(['GET'])
# def home(request):
#     return render(request, 'main.html')

# # Django view for handling predictions
# @csrf_exempt  # Disable CSRF token verification for simplicity (use cautiously)
# @api_view(['POST'])
# def predict(request):
#     if request.method == 'POST':
#         try:
#             # Get the form data from the request
#             gender = request.POST.get('gender')
#             age = request.POST.get('age')
#             hypertension = request.POST.get('hypertension')
#             heart_disease = request.POST.get('heart_disease')
#             ever_married = request.POST.get('ever_married')
#             work_type = int(request.POST.get('work_type'))  # Assuming this is a categorical variable
#             Residence_type = request.POST.get('Residence_type')
#             avg_glucose_level = float(request.POST.get('avg_glucose_level'))
#             bmi = float(request.POST.get('bmi'))
#             smoking_status = int(request.POST.get('smoking_status'))

#             # Prepare the input data for prediction
#             data = np.array([[gender, age, hypertension, heart_disease, ever_married, work_type,
#                               Residence_type, avg_glucose_level, bmi, smoking_status]])

#             # Perform the prediction using the loaded model
#             # my_prediction = model.predict(data)[0]
#             my_prediction = model.predict(data)
            
            
#             insert_query = "INSERT INTO predict_brain (gender, age, hypertension, heart_disease, ever_married, work_type, Residence_type, avg_glucose_level, bmi, smoking_status) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"

#             cur.execute(insert_query, tuple(data[0]))
#             mysql.connection.commit()
#             cur.close()

#             cur = mysql.connection.cursor()
#             cur.execute("SELECT * FROM predict_brain")
#             fetched_data = cur.fetchall()
#             cur.close()

#             # Render result.html and pass the prediction result as context
#             return render(request, 'result.html', {'prediction': my_prediction})

#         except Exception as e:
#             return JsonResponse({'error': str(e)}, status=400)

#     return JsonResponse({'error': 'Invalid request method'}, status=405)
















from django.conf import settings
from django.shortcuts import render
from django.http import JsonResponse, HttpResponse
from rest_framework.decorators import api_view
from django.views.decorators.csrf import csrf_exempt
import pickle
import numpy as np
import os

# Load the RandomForestClassifier model
filename = os.path.join(settings.BASE_DIR, 'D:/Brain Stroke Analysis_Project/RandomForestClassifier-model5.pkl')
with open(filename, 'rb') as model_file:
    model = pickle.load(model_file)

# Django view for rendering the main page
@api_view(['GET'])
def home(request):
    return render(request, 'main.html')

# Django view for handling predictions
@csrf_exempt  # Disable CSRF token verification for simplicity (use cautiously)
@api_view(['POST'])
def predict(request):
    if request.method == 'POST':
        try:
            # Get the form data from the request
            gender = request.POST.get('gender')
            age = request.POST.get('age')
            hypertension = request.POST.get('hypertension')
            heart_disease = request.POST.get('heart_disease')
            ever_married = request.POST.get('ever_married')
            work_type = int(request.POST.get('work_type'))  # Assuming this is a categorical variable
            Residence_type = request.POST.get('Residence_type')
            avg_glucose_level = float(request.POST.get('avg_glucose_level'))
            bmi = float(request.POST.get('bmi'))
            smoking_status = int(request.POST.get('smoking_status'))

            # Prepare the input data for prediction
            data = np.array([[gender, age, hypertension, heart_disease, ever_married, work_type,
                              Residence_type, avg_glucose_level, bmi, smoking_status]])

            # Perform the prediction using the loaded model
            # my_prediction = model.predict(data)[0]
            my_prediction = model.predict(data)

            # Render result.html and pass the prediction result as context
            return render(request, 'result.html', {'prediction': my_prediction})

        except Exception as e:
            return JsonResponse({'error': str(e)}, status=400)

    return JsonResponse({'error': 'Invalid request method'}, status=405)








# Data base code


# from django.shortcuts import render
# from django.http import JsonResponse
# from rest_framework.decorators import api_view
# from django.views.decorators.csrf import csrf_exempt
# import pickle
# import numpy as np
# import os
# from django.conf import settings
# from .models import Predict_brain  # Import the model


# # Load the RandomForestClassifier model
# filename = os.path.join(settings.BASE_DIR, 'D:/Brain Stroke Analysis_Project/RandomForestClassifier-model.pkl')
# with open(filename, 'rb') as model_file:
#     model = pickle.load(model_file)

# # Django view for rendering the main page
# @api_view(['GET'])
# def home(request):
#     return render(request, 'main.html')

# # Django view for handling predictions
# @csrf_exempt  # Disable CSRF token verification for simplicity (use cautiously)
# @api_view(['POST'])
# def predict(request):
#     if request.method == 'POST':
#         try:

            
            
#             gender = request.POST.get('gender')
#             age = int(request.POST.get('age'))
#             hypertension = bool(int(request.POST.get('hypertension')))
#             heart_disease = bool(int(request.POST.get('heart_disease')))
#             ever_married = bool(int(request.POST.get('ever_married')))
#             work_type = request.POST.get('work_type')
#             residence_type = request.POST.get('Residence_type')
#             avg_glucose_level = float(request.POST.get('avg_glucose_level'))
#             bmi = float(request.POST.get('bmi'))
#             smoking_status = request.POST.get('smoking_status')


#             # Prepare the input data for prediction
#             data = np.array([[gender, age, hypertension, heart_disease, ever_married, work_type,
#                               residence_type, avg_glucose_level, bmi, smoking_status]])

#             # Perform the prediction using the loaded model
#             my_prediction = model.predict(data)

#             # Save the prediction and form data into the database using Django's ORM
#             Predict_brain.objects.create(
#                 gender=gender,
#                 age=age,
#                 hypertension=hypertension,
#                 heart_disease=heart_disease,
#                 ever_married=ever_married,
#                 work_type=work_type,
#                 residence_type=residence_type,
#                 avg_glucose_level=avg_glucose_level,
#                 bmi=bmi,
#                 smoking_status=smoking_status
#             )
            
#             # Render result.html and pass the prediction result as context
#             return render(request, 'result.html', {'prediction': my_prediction[0]})

#         except Exception as e:
#             return JsonResponse({'error': str(e)}, status=400)

#     return JsonResponse({'error': 'Invalid request method'}, status=405)



















# from django.conf import settings
# from django.shortcuts import render
# from django.http import JsonResponse
# from rest_framework.decorators import api_view
# from django.views.decorators.csrf import csrf_exempt
# import pickle
# import numpy as np
# import os
# from .models import predict_brain  # Import your model

# # Load the RandomForestClassifier model
# filename = os.path.join(settings.BASE_DIR, 'D:/Brain Stroke Analysis_Project/RandomForestClassifier-model5.pkl')
# with open(filename, 'rb') as model_file:
#     model = pickle.load(model_file)

# # Django view for rendering the main page
# @api_view(['GET'])
# def home(request):
#     return render(request, 'main.html')

# # Django view for handling predictions
# @csrf_exempt  # Disable CSRF token verification for simplicity (use cautiously)
# @api_view(['POST'])
# def predict(request):
#     if request.method == 'POST':
#         try:
#             # Get the form data from the request
#             gender = (request.POST.get('gender'))  # Convert to integer
#             age = (request.POST.get('age'))  # Convert age to float for consistency
#             hypertension = (request.POST.get('hypertension'))
#             heart_disease = (request.POST.get('heart_disease'))
#             ever_married = (request.POST.get('ever_married'))
#             work_type = int(request.POST.get('work_type'))  # Assuming this is a categorical variable
#             residence_type = (request.POST.get('residence_type'))  # Changed variable name to match
#             avg_glucose_level = float(request.POST.get('avg_glucose_level'))
#             bmi = float(request.POST.get('bmi'))
#             smoking_status = (request.POST.get('smoking_status'))

#             # Prepare the input data for prediction
#             data = np.array([[gender, age, hypertension, heart_disease, ever_married, work_type,
#                               residence_type, avg_glucose_level, bmi, smoking_status]])

#             # Perform the prediction using the loaded model
#             my_prediction = model.predict(data)

#             # Save the prediction to the database
#             stroke_prediction = predict_brain(
#                 gender=bool(gender),
#                 age=int(age),
#                 hypertension=bool(hypertension),
#                 heart_disease=bool(heart_disease),
#                 ever_married=bool(ever_married),
#                 work_type=work_type,
#                 residence_type=bool(residence_type),
#                 avg_glucose_level=avg_glucose_level,
#                 bmi=bmi,
#                 smoking_status=smoking_status,
#                 prediction=bool(my_prediction)
#             )
#             stroke_prediction.save()

#             # Render result.html and pass the prediction result as context
#             return render(request, 'result.html', {'prediction': my_prediction})

#         except Exception as e:
#             return JsonResponse({'error': str(e)}, status=400)

#     return JsonResponse({'error': 'Invalid request method'}, status=405)
