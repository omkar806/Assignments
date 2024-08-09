import streamlit as st
from pdf2image import convert_from_path
import google.generativeai as genai
import os
import imghdr
import PIL.Image
import json
import tempfile
from dotenv import load_dotenv
load_dotenv()

# Configure Gemini API
GOOGLE_API_KEY = os.getenv("GOOGLE_API_KEY")
genai.configure(api_key=GOOGLE_API_KEY)
model = genai.GenerativeModel('gemini-1.5-flash')

def system_prompt() -> str:
    return """You are a Invoice/Receipt Analysing tool. Analyse the image of the invoice provided and extract information from the following receipt image and return a JSON object with these exact keys:Customer_Details,Products,Total Amount.

    Rules:
    1. For total_cost, use the highest monetary value in the text.
    2. Customer_Details will consist of another json object consisting the keys Customer_Name,Customer_Address,Email Address,Phone Number,Customer ID,Billing Address,Shipping Address,Account Number,Tax ID/VAT Number,Company Name,Payment Method.
    3.Products will consist of another json object consisting of keys Product_name_1,quantity,unit_price.
    6. If any value is not found, return null.
    7. If all values are null, return null.
    Ensure the strictly that output is a valid JSON object containing strictly the above keys, without any explanations.
    Generate a JSON response in the following format without using the ```json block. Ensure the output is properly formatted as plain text JSON.

    """

def get_invoice_details(image):
    response = model.generate_content([system_prompt(), image], stream=True)
    response.resolve()
    return response.text

def process_file(file):
    images = []
    if file.type == "application/pdf":
        with tempfile.NamedTemporaryFile(delete=False, suffix=".pdf") as tmp_file:
            tmp_file.write(file.getvalue())
            tmp_file_path = tmp_file.name
        
        pdf_images = convert_from_path(tmp_file_path)
        for img in pdf_images:
            images.append(img)
        
        os.unlink(tmp_file_path)
    elif file.type.startswith('image'):
        image = PIL.Image.open(file)
        images.append(image)
    else:
        st.error(f"Unsupported file type: {file.type}")
        return None

    return images

def main():
    st.title("Invoice Analyzer")

    uploaded_file = st.file_uploader("Choose an image or PDF file", type=["jpg", "jpeg", "png", "pdf"])

    if uploaded_file is not None:
        images = process_file(uploaded_file)

        if images:
            for i, img in enumerate(images):
                st.image(img, caption=f"Page {i+1}", use_column_width=True)
                
                with st.spinner(f"Analyzing page {i+1}..."):
                    json_output = get_invoice_details(img)
                
                try:
                    parsed_json = json.loads(json_output)
                    st.json(parsed_json)
                except json.JSONDecodeError:
                    st.error(f"Failed to parse JSON for page {i+1}. Raw output:")
                    st.text(json_output)

if __name__ == "__main__":
    main()