import openai

api_key = "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"
openai.api_key = api_key

def get_news_recommendations(user_input):
    response = openai.Completion.create(
        engine = "text-davinci-003",
        prompt=user_input,
        max_tokens=200,
    )

    return response.choices[0].text


