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
- **Allow for maybe**: If the model can only reply yes or no, some more strange output will appear. Propose a maybe/unknown option as output.
- **Allow for multiple classes**: when doing classification, the classifications might not be MECE and it could have both like Belgian (nationality) and French (as the language not the nationality).

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
## 7. Few shots prompting:
    Provide the model with a few examples of Questions/Answers. Typically used for classifications / switch type with a user/content followed by assistant/content messages a few times. Always add a unknown class.
    # Few shots prompt via API
            response = client.chat.completions.create (
                model= ""gpt-4o-mini",
                messages = [
                    # Provide the examples as previous conversations
                    {"role": "user", "content": "For pizza you need dough, passata and basil"},
                    {"role": "assistant", "content": "italian food"},
                    {"role": "user", "content": "For pizza you need dough, tomato sauce and pinneaples"},
                    {"role": "assistant", "content": "american food"},
                    {"role": "user", "content": "For pizza you need dough, ketchup and mustard"},
                    {"role": "assistant", "content": "unknown"},
                    # Provide the text for the model to classify
                    {"role": "user", "content":"For pizza you need dough, tomato sauce and cheese"}
                ]

            )
     # Few shots prompt via GUI
        prompt = """
            Receiving a promotion at work made me feel on top of the world -> Happiness
            The movie's ending left me with a heavy feeling in my chest -> Sadness
            Walking alone in the dark alley sent shivers down my spine -> Fear
            They sat and ate their meal -> no explicit emotion

           Classify:  The scene felt mundane and uneventful ->
            """
## 8. Multi-steps prompting:
    Provide the model with a few steps to follow. Step 1 do this, Step 2 do that. This can lead you to console.log type checking blocks of prompt output or even enable something TDDish.
    Example of such a prompt:

        code_to_validate = "______"
        prompt =   f"""Determine the correctness of the code delimited by triple backticks as follows:
                Step 1: Check code correctness in each function.
                Step 2: Verify if the divide function handles the case when dividing by 0.
                Step 3: Verify that 12 divided by 4 returns 3.
                Code: '''{code_to_validate}'''"""

        print(get_response(prompt))

## 9. Chain-of-thought:
    Use few-shots to break the process. Models are not good at deduction. Generate intermediate steps to get insights and make sure that it is not a black box. Check for self consistency - make a new chat and ask again. See if you get the same answer.

    Identifying the Root Cause of a Data Discrepancy
        Problem: The employee notices that the daily report shows a significant difference between expected and actual values for a particular trading position. The actual value is lower than expected, but the sources of the discrepancy aren't immediately obvious. How should the employee proceed?

        Prompt: "Let's analyze this discrepancy step by step:

        First, check the input data sources used to generate the report. Were all positions and trades properly imported and processed?
        Then, review any adjustments or manual entries that might have been applied after the original data was input. Were any outliers or corrections introduced?
        Next, compare the formulas and calculations used in the report. Could there be an error in how certain values are being aggregated or weighted?
        Lastly, consider external factors such as exchange rate fluctuations or market conditions that may have impacted the position’s value overnight.
        By systematically evaluating each of these factors, we can pinpoint where the discrepancy originated."

## 10. Mocking data, tone adjustment and mash-ups:
    Usually you cannot get llms to generate formats like xls. But you can ask for a table you can copy. You can get it create by asking to mash-up two domains together. You can also provide existing text and ask to improve the tone.

    # Mocking data prompt example using GUI
            Create a mock dataset for training purposes that focuses on eCommerce sales data for a small business specializing in online smartphone case sales. The dataset should comprise the following columns:
                - Transaction ID
                - Transaction date
                - Product SKU
                - Product name
                - Quantity
                - Unit price
                - Total amount
             Please ensure that the mock dataset is realistic and representative of typical eCommerce sales data for the specified small business. 

    # Tone adjustment example using GUI
        Need to make the audience clear for this to work
        "Take the australian consumer law main piece of legislation and put the main 5 points in street tiktok youth parlance of the 21st century"

     # Text expansion prompt example using API
        service_description = """Service: Social XYZ
        - Social media strategy
        - Content creation
        - Social media engagement and community building
        - Influencer contracting"""

        prompt = f"""Expand the description for the company. The service is delimited by triple backticks. Provide an overview of its feature and benefits, without bypassing the limit of two sentences. Use a professional tone. 
        ```{service_description}```"""
## 11. Visualize data:
    TBC but it seems you can get graphs out of dirty data.


## 12. Model and domain knowledge:
        "Large language models like GPT-4 have domain knowledge, but their depth and specificity vary based on the data they've been trained on. Here’s how it works:

        General Knowledge: Language models are trained on a vast amount of data from the internet, which gives them general knowledge across many domains (science, history, programming, literature, etc.). This allows them to provide relevant information on a wide variety of topics.

        Expert-Level Knowledge: While they can simulate expert-level responses in some areas, they are not specialists in the way a trained professional is. They don't "understand" topics in the same way humans do; instead, they generate text based on patterns found in their training data.

        Narrow Domains: In highly specialized fields (e.g., advanced medicine, niche engineering), they may lack the depth and specificity of a true expert. The models provide useful insights but might not always have the latest or most specific information.

        Limitations: Models also don’t have access to real-time updates unless connected to external databases or updated regularly, so their knowledge is capped at the last time they were trained (for GPT-4, this is September 2021)."

## 13. Documenting:
    Provide the llm with jargonistic or difficult to read text and ask it to add comments with explanations.