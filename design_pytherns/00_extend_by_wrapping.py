# Wrap the Function
# A pythonic and straightforward way to extend a function is by wrapping it. Here’s how you can do it:


from some_library import special_sum

def enhanced_sum(*args):
    # Add pre-processing (if any)
    result = special_sum(*args)
    # Add post-processing (if any)
    return result + 5  # Example post-process
# This approach is both simple and clean, and it will not break if the external library updates the function unless the signature or behavior of special_sum changes drastically. To mitigate that risk, you should carefully check the external library's documentation or changelogs during updates.

# Wrap the Class
#A wrapper class is a class designed to wrap around another class (or object) to provide additional functionality or interface. It’s part of a design pattern called composition, where the wrapper class "has a" relationship with the class it's wrapping (instead of "is a" which is inheritance).

# Let's assume the external class we want to wrap looks like this:
class SpecialDocument:
    def __init__(self, text):
        self.text = text

    def word_count(self):
        # Returns the number of words in the text
        return len(self.text.split())

    def get_summary(self):
        # Returns the first 10 words as a summary
        return ' '.join(self.text.split()[:10])

# Our wrapper class will "wrap" around SpecialDocument and extend its functionality.
class DocumentWrapper:
    def __init__(self, document: SpecialDocument):
        """
        Initializes the wrapper class with an instance of SpecialDocument.
        """
        self.document = document

    def print_summary(self):
        """
        Prints a summary of the document by invoking the wrapped `get_summary` method.
        """
        summary = self.document.get_summary()
        print(f"Summary: {summary}")

    def detailed_word_count(self):
        """
        Extends the functionality of `word_count` by adding additional info.
        This is a new feature that builds on the wrapped class method.
        """
        count = self.document.word_count()
        return f"Document contains {count} words."

    def add_footer(self, footer_text: str):
        """
        Adds a footer to the document.
        This modifies the wrapped class's internal state by appending to the text.
        """
        self.document.text += f"\n\n---\n{footer_text}"
    
    def search_word(self, word: str) -> bool:
        """
        Searches for a word in the document.
        Adds completely new functionality, not present in SpecialDocument.
        """
        return word in self.document.text

# Example usage:

# Creating a SpecialDocument instance
doc = SpecialDocument("This is a test document. It contains many words for demonstration purposes.")

# Wrapping the document with DocumentWrapper
wrapped_doc = DocumentWrapper(doc)

# Using the new functions added by DocumentWrapper
wrapped_doc.print_summary()  # Prints the first 10 words as a summary
print(wrapped_doc.detailed_word_count())  # "Document contains X words."
wrapped_doc.add_footer("End of Document.")  # Modifies the document by adding a footer
print(wrapped_doc.search_word("test"))  # Searches for the word "test" in the document