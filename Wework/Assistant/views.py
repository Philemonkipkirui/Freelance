import json
#import os
import google.generativeai as genai
from django.conf import settings
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
# Create your views here.
try:
    API_KEY = settings.GEMINI_API_KEY
    if not API_KEY:
        raise ValueError("GEMINI_API_KEY is not set in Django settings.")
    genai.configure(api_key=API_KEY)
    print("Gemini API configured successfully.")
except (AttributeError, ValueError) as e:
    print(f"Configuration error: {e}")

def assistant_view(request):
    from django.shortcuts import render
    return render(request, 'assistant.html')
print("Assistant view rendered successfully.")

@csrf_exempt
def generate_content(request):
    """
    Handles POST requests to generate content using the Gemini API.
    Expects a JSON body with a 'prompt' key.
    """
    if request.method != 'POST':
        return JsonResponse({"error": "Only POST requests are allowed"}, status=405)

    try:
        # Parse the JSON data from the request body
        data = json.loads(request.body)
        prompt = data.get('prompt')
        print("Prompt received:", prompt)

        if not prompt:
            return JsonResponse({"error": "Prompt is required"}, status=400)
        model = genai.GenerativeModel('gemini-2.5-flash', generation_config=genai.types.GenerationConfig(
            temperature= 0.2,
            top_p=1.0,
            top_k=40,
            max_output_tokens=1024,
        ))


        # Generate content with the model
        print(f"Received prompt: '{prompt}'")
        response = model.generate_content(prompt)
        print("Successfully generated content.")

        # Extract the text from the response
        generated_text = response.text
        return JsonResponse({"generatedText": generated_text})

    except json.JSONDecodeError:
        return JsonResponse({"error": "Invalid JSON in request body"}, status=400)
    except Exception as e:
        print(f"Error calling Gemini API: {e}")
        return JsonResponse({"error": "Failed to generate content"}, status=500)
    
