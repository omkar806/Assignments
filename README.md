# Invoice to JSON Converter

This project provides a tool to convert invoices and receipts into structured JSON format using the Gemini-1.5 Flash API. It includes a Streamlit web application for easy interaction and testing.

## Contents

1. **Colab Notebook**: Contains the core logic for converting invoices to JSON using the Gemini-1.5 Flash API.
2. **app.py**: Implements a Streamlit user interface for the invoice conversion tool.

## Live Demo

You can test the application with your own receipts using our Hugging Face Spaces deployment:

[![Streamlit App](https://static.streamlit.io/badges/streamlit_badge_black_white.svg)](https://huggingface.co/spaces/Omkar008/Invoice_To_Json)

## Features

- Upload invoice or receipt images
- Extract key information such as customer details, products, and total amount
- Convert extracted data into a structured JSON format
- User-friendly web interface for easy testing and interaction

## How to Use

1. Visit the [Hugging Face Spaces link](https://huggingface.co/spaces/Omkar008/Invoice_To_Json)
2. Upload your invoice or receipt image
3. The application will process the image and return a JSON object with extracted information

## Technology Stack

- Gemini-1.5 Flash API for image analysis and data extraction
- Streamlit for the web application interface
- Hugging Face Spaces for deployment and hosting

## Deployment

The Streamlit app is deployed on Hugging Face Spaces, which offers free resources to showcase AI projects. This allows for easy sharing and testing of the application.
