# To Remember

## 1. Use of f-strings for Prompts:
- In Python, f-strings allow you to embed expressions inside string literals using `{}`.
- This is useful for dynamic prompt creation, ensuring the inclusion of variables in queries and instructions.
- **Example**:
    ```python
    name = "Alice"
    prompt = f"Hello, {name}, what would you like to do today?"
    ```

## 2. User/System/Assistant Roles:
- **User**: The person interacting with the model, providing input or asking questions.
- **System**: Sets the behavior of the assistant (usually not visible to the user, contains background instructions).
- **Assistant**: The AI that responds to user prompts, guided by both system instructions and user inputs.
- **Example of interaction flow**:
    - **User**: "What is the capital of France?"
    - **Assistant**: "The capital of France is Paris."

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

## 5. Proposed Additions:
- **Contextualization**: Use clear and specific context when asking questions to help the model provide accurate responses.
    - Example: "Given that I am a beginner in Rust, can you explain how loops work?"
- **Prompt Length**: Strike a balance between too short (vague) and too long (overloaded).
- **Multi-part Prompts**: Break down complex requests into smaller, digestible parts for clarity.
