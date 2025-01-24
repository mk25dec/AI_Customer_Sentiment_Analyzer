import requests

# Hugging Face API details (replace with your actual API token)
API_URL = "https://api-inference.huggingface.co/models/distilbert-base-uncased-finetuned-sst-2-english"
YOUR_HUGGING_FACE_API_TOKEN = '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'  # Replace with your actual token (avoid hardcoding)
#hugginface - Read Write access
apikey='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'


# Function to query the Hugging Face API
def query(payload):
    response = requests.post(API_URL, headers=headers, json=payload)
    try:
        return response.json()  # Parse JSON response
    except ValueError:
        return {"error": "Invalid JSON response"}

# Secure API Token Handling (avoid hardcoding)
headers = {"Authorization": f"Bearer {YOUR_HUGGING_FACE_API_TOKEN}"}

# Get user input for sentiment analysis
text = input("Enter some text for sentiment analysis: ")

# Query the Hugging Face API
api_output = query({"inputs": text})




# Debug: Print the raw API response
print(f"Raw API Output: {api_output} \n\n")

# Extract and print the predicted label
if isinstance(api_output, list) and len(api_output) > 0 and isinstance(api_output[0], list):  # Check nested list structure
    first_prediction_list = api_output[0]  # Extract the first inner list
    if isinstance(first_prediction_list, list) and len(first_prediction_list) > 0:  # Ensure it's a list with content
        # Sort by score to get the highest confidence prediction
        best_prediction = sorted(first_prediction_list, key=lambda x: x["score"], reverse=True)[0]
        predicted_label = best_prediction["label"].lower()  # Extract the label
        print(f"Input Text: {text} \n\n")
        print(f"Predicted Sentiment: {predicted_label}")
    else:
        print("Unexpected structure inside the nested list:", first_prediction_list)
elif "error" in api_output:  # Handle errors from the API
    print(f"Error from API: {api_output['error']}")
else:
    print("Unexpected API response:", api_output)
