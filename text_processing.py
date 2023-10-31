def process_long_text(long_text, max_tokens=500):
    tokenized_text = long_text.split()  # Split text into tokens
    processed_text = []
    current_token_count = 0
    current_chunk = []

    for token in tokenized_text:
        token_length = len(token.split())  # Consider multi-word tokens
        if current_token_count + token_length <= max_tokens:
            current_token_count += token_length
            current_chunk.append(token)
        else:
            # If adding the token exceeds the limit, process the current chunk
            processed_chunk = " ".join(current_chunk)
            processed_text.append(processed_chunk)

            # Start a new chunk with the current token
            current_chunk = [token]
            current_token_count = token_length

    # Process the remaining chunk
    if current_chunk:
        processed_chunk = " ".join(current_chunk)
        processed_text.append(processed_chunk)

    return processed_text

# Example usage:
input_text = "Your long input text here..."
processed_chunks = process_long_text(input_text)
for i, chunk in enumerate(processed_chunks):
    print(f"Chunk {i + 1}: {chunk}")
