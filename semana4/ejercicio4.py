class TextEditor:
    """A simple text editor using stack to support typing, deleting, and undo operations."""

    def __init__(self):
        self.text = ""  # Current state of the text
        self.history_stack = []  # Stack to store previous states

    def type(self, new_text):
        """Append text and save current state to history."""
        self.history_stack.append(self.text)
        self.text += new_text
        return self.text

    def delete(self, count):
        """Delete the last 'count' characters and save current state."""
        self.history_stack.append(self.text)
        self.text = self.text[:-count] if count <= len(self.text) else ""
        return self.text

    def undo(self):
        """Undo the last operation by restoring the previous state."""
        if self.history_stack:
            self.text = self.history_stack.pop()
        return self.text

    def get_text(self):
        """Return the current content of the editor."""
        return self.text


# Example usage and test cases
if __name__ == "__main__":
    editor = TextEditor()

    print("Typing 'hello' →", editor.type("hello"))      # "hello"
    print("Typing ' world' →", editor.type(" world"))    # "hello world"
    print("Deleting 6 characters →", editor.delete(6))   # "hello"
    print("Undo →", editor.undo())                       # "hello world"
    print("Undo →", editor.undo())                       # "hello"
    print("Undo →", editor.undo())                       # ""
