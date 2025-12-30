class Comment:
    def __init__(self, text, author):
        self.text = text
        self.author = author
        self.replies = []
        self.is_deleted = False

    def add_reply(self, reply):
        self.replies.append(reply)

    def remove_reply(self):
        self.text = "This comment was deleted."
        self.is_deleted = True

    def display(self, indent=0):
        padding = "    " * indent
        
        if self.is_deleted:
            print(f"{padding}{self.text}")
        else:
            print(f"{padding}{self.author}: {self.text}")

        for reply in self.replies:
            reply.display(indent + 1)

if __name__ == '__main__':
    root_comment = Comment("What an amazing book!", "Bodya")
    
    reply1 = Comment("The book is a total disappointment :(", "Andriy")
    reply2 = Comment("What is so great about it?", "Maryna")

    root_comment.add_reply(reply1)
    root_comment.add_reply(reply2)

    reply1_1 = Comment("Not a book, just a waste of paper...", "Serhiy")
    reply1.add_reply(reply1_1)

    reply1.remove_reply()

    print("--- Comments Tree Structure ---")
    root_comment.display()
    