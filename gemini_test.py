from google import genai

client = genai.Client(api_key="AIzaSyC1NMaBZpP_rdS3AWnMsSx7CBO6vR6RHZs")

while(True):
        response = client.models.generate_content(
        model="gemini-3-flash-preview", 
        contents=(input)("Enter your question")
        )
        print(response.text)