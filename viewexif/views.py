from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
from exif import Image
from PIL import Image as PILImage
import os
from django.shortcuts import render

# Global variable for height threshold
alt_threshold = 75
@csrf_exempt
def render_index(request):
    return render(request, 'index.html')


###############################################
#Multiple Files#
###############################################

def process_images(request):
    if request.method == 'POST' and request.FILES.getlist('images'):
        # Get the list of uploaded image files
        uploaded_images = request.FILES.getlist('images')

        # List to store results for each image
        results = []
        # results2 = []

        for uploaded_image in uploaded_images:
            # Read the image data path
            image_path = uploaded_image.temporary_file_path()
            with open(image_path, 'rb') as file:
        # Read the EXIF data
                image_data = Image(file)
            # print(dir(image_data))
            if image_data.gps_altitude > alt_threshold:
                flag = "Rejected: Height above allowed threshold"
            else:
                flag = "Accepted: Height within threshold"

        # Append result to the list
            results.append({'filename': image_data.image_description, 'flag': flag, 'altitude in meters': image_data.gps_altitude, 'allowed altitude' : alt_threshold})
            # results2.append(dir(image_data))
        # Return the results as JSON response
        return JsonResponse({'results': results})
    # return JsonResponse(results2, safe = False)



    