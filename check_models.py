import google.generativeai as genai

genai.configure(api_key="Google_api_key")

models = genai.list_models()
for m in models:
    print(m.name, m.supported_generation_methods)
