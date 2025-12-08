from pynput.keyboard import Key, KeyCode

class InputProcessor:
    def __init__(self, initial_text=""):
        self.text_buffer = list(initial_text)
        self.cursor_position = len(self.text_buffer)

    def process_key(self, key):
        """
        Process a key event and update the text buffer.
        Returns a tuple: (string_representation_of_key, current_reconstructed_text)
        """
        key_char = ""
        
        if isinstance(key, KeyCode):
            # Regular character
            if key.char:
                key_char = key.char
                self.text_buffer.append(key_char)
            else:
                # Sometimes KeyCode doesn't have char (e.g. numpad)
                key_char = f"[{key.vk}]"
                self.text_buffer.append(key_char)
        
        elif isinstance(key, Key):
            # Special keys
            if key == Key.space:
                key_char = " "
                self.text_buffer.append(" ")
            elif key == Key.enter:
                key_char = "\n"
                self.text_buffer.append("\n")
            elif key == Key.backspace:
                key_char = "[BACKSPACE]"
                self.text_buffer.append("[BACKSPACE]")
            elif key == Key.delete:
                key_char = "[DEL]"
                self.text_buffer.append("[DEL]")
            elif key == Key.left:
                key_char = "[<]"
                self.text_buffer.append("[<]")
            elif key == Key.right:
                key_char = "[>]"
                self.text_buffer.append("[>]")
            # Add other keys as needed for visualization, but they don't affect text content usually
            # e.g. Shift, Ctrl, etc.
            else:
                key_char = f"[{key.name}]"
                # Optional: decide if we want to log Shift/Ctrl etc. to the text buffer
                # For now, let's not append modifiers to the text buffer to keep it readable-ish,
                # or append them if the user wants "all text typed".
                # The user said "all text typed", so let's append everything that produces a char or is a significant action.
                # Modifiers usually don't produce text on their own, so we might skip appending them to text_buffer
                # unless we want a full key log.
                # Let's stick to the previous logic for "other keys" which didn't append to text_buffer,
                # but wait, the user wants "all text typed it should not removed".
                # So I will append the string representation of the key.
                pass

        return key_char, "".join(self.text_buffer)

    def get_text(self):
        return "".join(self.text_buffer)

    def get_stats(self):
        text = self.get_text()
        return {
            "char_count": len(text),
            "word_count": len(text.split()) if text else 0
        }
