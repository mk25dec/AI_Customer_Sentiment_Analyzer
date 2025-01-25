import streamlit as st
import requests
import transformers  # For Hugging Face model loading (if needed)

api_token = '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'

def main():
    """Main function of the Streamlit app"""

    # Title and text input
    st.title("Sentiment Analysis App")
    text = st.text_input("Enter some text for sentiment analysis:")

    # Sentiment analysis button
    if st.button("Analyze Sentiment"):
        if text:
            # Call sentiment analysis function (defined below)
            sentiment = analyze_sentiment(text)
            st.write(f"Predicted Sentiment: {sentiment}")
        else:
            st.warning("Please enter some text to analyze.")

def analyze_sentiment(text):
    """Function to perform sentiment analysis using Hugging Face API"""

    # Access API token securely (replace with your environment variable access)
    #api_token = os.environ.get("HUGGING_FACE_API_TOKEN")
    headers = {"Authorization": f"Bearer {api_token}"}

    # Hugging Face API details
    API_URL = "https://api-inference.huggingface.co/models/distilbert-base-uncased-finetuned-sst-2-english"

    # Prepare payload
    payload = {"inputs": text}

    # Send request and handle response
    try:
        response = requests.post(API_URL, headers=headers, json=payload)
        response.raise_for_status()  # Raise an exception for non-200 status codes
        api_output = response.json()

        # Extract and process the predicted label (modify based on API response structure)
        if isinstance(api_output, list) and len(api_output) > 0 and isinstance(api_output[0], list):
            first_prediction_list = api_output[0]
            if isinstance(first_prediction_list, list) and len(first_prediction_list) > 0:
                best_prediction = sorted(first_prediction_list, key=lambda x: x["score"], reverse=True)[0]
                predicted_label = best_prediction["label"].lower()
                return predicted_label
            else:
                return "Unexpected structure inside the nested list"
        else:
            return "Unexpected API response"
    except requests.exceptions.RequestException as e:
        return f"Error: {e}"

if __name__ == "__main__":
    main()