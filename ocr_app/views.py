from django.shortcuts import render
from django.http import JsonResponse
from django.views import View
from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator
from PIL import Image
import pytesseract
import io

@method_decorator(csrf_exempt, name='dispatch')
class OCRView(View):
    def post(self, request, *args, **kwargs):
        if 'images' not in request.FILES:
            print(request.FILES)
            return JsonResponse({"error": "No image file uploaded"}, status=400)

        file = request.FILES['images']
        image = Image.open(io.BytesIO(file.read()))

        text = pytesseract.image_to_string(image)

        return JsonResponse({"text": text})