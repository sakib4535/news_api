import streamlit as st
from text_preprocessing import tokenize_text, remove_stopwords, stem_tokens
import requests

# Set the page configuration
st.set_page_config(
    page_title="InfoDaily: News Recommendation App",
    page_icon="📰",
    layout="wide",
)

# Define custom CSS styles to improve the visual appearance
custom_style = """
<style>
body {
    background-color: #e3e4c2; /* Background color */
    font-family: Cambria, Cochin, Georgia, Times, 'Times New Roman', serif;
    padding: 20px; /* Add padding to the body */
}

.stApp {
    max-width: 1200px; /* Set the maximum width of the app */
}

.stTextInput {
    background-color: #eed33c; /* Input field background color */
    font-family: Cambria, Cochin, Georgia, Times, 'Times New Roman', serif;
    border: 2px solid #292828; /* Input field border color */
    border-radius: 5px; /* Rounded corners for input field */
    padding: 10px; /* Add padding to the input field */
    font-size: 16px; /* Font size */
}

.stButton {
    background-color: #007acc; /* Button background color */
    color: #ee2424; /* Text color for the button */
    border: 1px solid #232425; /* Button border */
    border-radius: 5px; /* Rounded corners for button */
    padding: 10px 20px; /* Add padding to the button */
    font-size: 16px; /* Font size */
    cursor: pointer; /* Add pointer cursor on hover */
    font-weight: bold; /* Make the button text bold */
    font-family: 'Helvetica', sans-serif; /* Specify a custom font */
}

.stButton:hover {
    background-color: #0055a3; /* Change button color on hover */
}

.stMarkdown a {
    color: #007acc; /* Link color */
    text-decoration: none; /* Remove underline from links */
    
}
</style>

"""
st.markdown(custom_style, unsafe_allow_html=True)

# Streamlit app title and description
st.title("InfoNews: News Recommendation API")
st.write("Provide Your Desired keyword or topic, and We'll Recommend Relevant News Articles from All Around the World")

# Create a search box
search_query = st.text_input("Enter the Keyword in Which You Are Interested:", key="search_query")

# Button to trigger the search
if st.button("Get Recommendations", key="search_button", help="Click to get news recommendations"):
    if search_query:
        # Process the input text using the text preprocessing functions
        tokens = tokenize_text(search_query)
        filtered_tokens = remove_stopwords(tokens)
        stemmed_tokens = stem_tokens(filtered_tokens)
        processed_text = " ".join(stemmed_tokens)

        api_key = 'fc9d7523a40c49f4b065e623bcf940e5'
        news_api_url = 'https://newsapi.org/v2/everything'

        # Set the parameters for the API request
        params = {
            'q': processed_text,
            'apiKey': api_key,
            'language': 'en'
        }

        # Make the API request
        response = requests.get(news_api_url, params=params)
        data = response.json()
        articles = data.get('articles', [])

        # Display the recommendations
        st.subheader("Recommended News Articles:")
        for article in articles:
            title = article.get('title', '')
            description = article.get('description', '')
            url = article.get('url', '')
            image_url = article.get('urlToImage', '')

            # Display a smaller image, title, description, and URL
            if image_url:
                st.image(image_url, caption=title, use_column_width=True, width=150)
            st.markdown(f"**Title:** [{title}]({url})")
            st.write(description)
            st.write("---")  # Add a separator

    else:
        st.warning("Please enter a keyword or topic.")
