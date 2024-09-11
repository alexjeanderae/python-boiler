# To Remember

## 1. Use of f-strings for Prompts:
- In Python, f-strings allow you to embed expressions inside string literals using `{}`.
- This is useful for dynamic prompt creation, ensuring the inclusion of variables in queries and instructions.
- Pairs very well with triple backticks (```).
- **Example in python**:
    name = "Alice"
    prompt = f"Hello, {name}, what would you like to do today?"
- **Example in python with backticks for multiline**:
    Notice that "quote" of the prompt is removed, the f is at the beggining and the ``` will be typically syntax error. 
    Also the indentation is not what I usually expect.
    story = "Alice met a crazy cat"
    prompt = f"""
    complete the following story: {story}?
    """

## 2. User/System/Assistant Roles:
- **User**: The person interacting with the model, providing input or asking questions.
- **System**: Sets the behavior of the assistant (usually not visible to the user, contains background instructions).
- **Assistant**: In short the response you get from the API preformated to look like a conversation. It is typically used to give context when using the api. Like your previous answer was...

**Example of interaction flow**:

- **System**: "You are a helpful travel assistant that provides concise travel advice and information."

- **User**: "I'm planning a trip to Japan in December. What are some things I should know?"

- **Assistant**: "In December, Japan can be quite cold, especially in the northern regions. Be sure to pack warm clothing if you're visiting cities like Sapporo. You can also enjoy winter festivals, hot springs, and stunning holiday illuminations. Do you need help planning your itinerary?"

In this example:
- The **System** sets the assistant's behavior to focus on travel advice.
- The **User** asks a travel-related question.
- The **Assistant** provides an informative response based on the user's input and the system's instructions.

A normal response from the API would be in JSON format with meta data in it like id, model; followed by choices[0].text that should contain what you would get from assistant; then some billing/usage data.

## 3. List of Dictionaries Example:
- Often, prompts need data structured for better context or handling.
- **Example**:
    ```python
    [{"role": "system", "content": "You are an AI assistant."},
     {"role": "user", "content": "Tell me a joke."},
     {"role": "assistant", "content": "Why did the scarecrow win an award? Because he was outstanding in his field!"}]
    ```

## 4. Importance of Action Verbs in Prompts:
- Action verbs clarify what you want the model to do.
- Common verbs: **generate**, **explain**, **list**, **summarize**, **analyze**.
- **Example**: 
    - Instead of: "Can you describe?"
    - Use: "Describe in detail the characteristics of an ocean ecosystem."

## 5. Optional Additions:
- **Contextualization**: Use clear and specific context when asking questions to help the model provide accurate responses.
    - Example: "Given that I am a beginner in Rust, can you explain how loops work?"
- **Prompt Length**: Strike a balance between too short (vague) and too long (overloaded).
- **Multi-part Prompts**: Break down complex requests into smaller, digestible parts for clarity.

## 6. Structured Output:
- **List**: Use the verb list and you will get a list. You can specify numbered list.
- **Table**: Ask for a table and detail the column titles.
- **Paragraph**: Specify if you want outlines, bullet points or headings with sub-headings.
- **Conditions**: ChatGPT should understand if and else type conditions when generating response.
- **Custom format**:
        client = OpenAI(api_key="<OPENAI_API_TOKEN>")

        # Create the instructions
        instructions = "You will be provided with a text delimited by triple backticks. Infer its language, then generate a suitable title for it. "

        # Create the output format
        output_format = """Use the following format for the output:
                - Text: <the text>
                - Language: <the text language>
                - Title: <the generated title>"""

        # Create the final prompt
        prompt = instructions + output_format + f"```{text}```"
        response = get_response(prompt)
        print(response)
