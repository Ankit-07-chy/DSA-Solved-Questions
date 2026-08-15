import sys

def finalText(q, operations):
    class TextEditor:
        def __init__(self):
            self.text = [] 
            self.history = [] 

        def insert(self, text):
            self.text.extend(list(text))
            self.history.append(['INSERT', text])

        def backspace(self):
            if self.text:
                removed_char = self.text.pop()
                self.history.append(['BACKSPACE', removed_char])

        def undo(self):
            if not self.history:
                return
            
            op_type, value = self.history.pop()

            if op_type == 'INSERT':
                for _ in range(len(value)):
                    self.text.pop()
                    
            elif op_type == 'BACKSPACE':
                self.text.append(value)

    editor = TextEditor()
    
    for op in operations:
        if op == 'UNDO':
            editor.undo()
        else:
            # FIXED: Safely handle splitting!
            parts = op.split(' ') 
            command = parts[0]
            
            if command == 'INSERT':
                # We know INSERT lines always have a 2nd part (the text)
                text_to_insert = parts[1]
                editor.insert(text_to_insert)
            elif command == 'BACKSPACE':
                editor.backspace()

    return ''.join(editor.text)

def main():
    data = sys.stdin.buffer.read().decode().strip().split('\n')
    if not data or not data[0].strip():
        return
    
    q = int(data[0])
    # Safely get only the operations, ignoring any extra blank lines at the end
    operations = []
    for i in range(1, q + 1):
        if i < len(data):
            operations.append(data[i].strip())
            
    sys.stdout.write(finalText(q, operations) + "\n")

if __name__ == "__main__":
    main()