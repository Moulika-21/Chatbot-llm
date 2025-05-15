import google.generativeai as genai

genai.configure(api_key="AIzaSyBjiqIeWsYmW3DhNKrS7qv6jnwnEmYUw1U")

models = genai.list_models()
for m in models:
    print(m.name, m.supported_generation_methods)
