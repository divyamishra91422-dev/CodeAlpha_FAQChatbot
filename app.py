
import tkinter as tk
from tkinter import scrolledtext
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
FAQS = [
    ("hello", "Hello! Welcome to my AI FAQ Chatbot. How can I help you?"),
    ("hi", "Hi! How can I help you today?"),
    ("hey", "Hey! Ask me anything about programming or technology."),
    ("how are you", "I am fine, thank you! What would you like to learn?"),
    ("what is your name", "I am an AI FAQ Chatbot built using Python and Machine Learning."),
    ("bye", "Goodbye! Thank you for chatting with me."),
    ("thank you", "You're welcome! Happy to help."),

    ("what is AI", "AI stands for Artificial Intelligence. It enables computers to perform tasks that normally require human intelligence."),
    ("what is machine learning", "Machine Learning is a branch of AI that helps computers learn patterns from data."),
    ("what is Python", "Python is a programming language used in AI, machine learning, automation, and web development."),
    ("what is NLP", "NLP stands for Natural Language Processing. It helps computers understand human language."),
    ("what is a chatbot", "A chatbot is a software application that communicates with users through text or voice."),

    ("what is MySQL", "MySQL is a relational database management system used to store and manage data using SQL."),
    ("what is SQL", "SQL stands for Structured Query Language. It is used to retrieve and manage data in relational databases."),
    ("what is a database", "A database is an organized collection of information that can be stored, searched, and updated."),
    ("what is HTML", "HTML structures the content of web pages."),
    ("what is CSS", "CSS is used to style web pages, including colors, layouts, and fonts."),
    ("what is JavaScript", "JavaScript makes web pages interactive."),
    ("what is an algorithm", "An algorithm is a step-by-step procedure for solving a problem."),
    ("what is deep learning", "Deep Learning is a type of machine learning that uses neural networks.")
]


class FAQChatbot:
    def __init__(self, root):
        self.root = root
        self.root.title("AI FAQ Chatbot")
        self.root.geometry("700x600")
        self.root.minsize(500, 450)
        self.root.configure(bg="#f2f5fb")

        self.questions = [item[0] for item in FAQS]
        self.answers = [item[1] for item in FAQS]

        self.vectorizer = TfidfVectorizer(
            lowercase=True,
            stop_words="english",
            ngram_range=(1, 2)
        )
        self.question_vectors = self.vectorizer.fit_transform(self.questions)

        header = tk.Frame(root, bg="#263b80", padx=16, pady=16)
        header.pack(fill="x")

        tk.Label(
            header,
            text="AI FAQ Chatbot",
            font=("Arial", 20, "bold"),
            bg="#263b80",
            fg="white"
        ).pack(anchor="w")

        tk.Label(
            header,
            text="Ask a question about AI, Python, machine learning, and technology.",
            font=("Arial", 10),
            bg="#263b80",
            fg="white",
            wraplength=620,
            justify="left"
        ).pack(anchor="w", pady=(6, 0))

        self.chat_area = scrolledtext.ScrolledText(
            root,
            wrap=tk.WORD,
            font=("Arial", 11),
            bg="white",
            fg="#202438",
            padx=12,
            pady=12,
            state="disabled"
        )
        self.chat_area.pack(fill="both", expand=True, padx=14, pady=14)

        bottom = tk.Frame(root, bg="#f2f5fb", padx=14)
        bottom.pack(fill="x", pady=(0, 14))

        self.entry = tk.Entry(bottom, font=("Arial", 12))
        self.entry.pack(side="left", fill="x", expand=True, ipady=9)
        self.entry.bind("<Return>", self.send_message)

        send_button = tk.Button(
            bottom,
            text="Send",
            command=self.send_message,
            font=("Arial", 11, "bold"),
            bg="#263b80",
            fg="white",
            activebackground="#354da0",
            activeforeground="white",
            padx=18,
            pady=8,
            relief="flat"
        )
        send_button.pack(side="left", padx=(8, 0))

        clear_button = tk.Button(
            bottom,
            text="Clear",
            command=self.clear_chat,
            font=("Arial", 10),
            padx=10,
            pady=8
        )
        clear_button.pack(side="left", padx=(6, 0))

        self.add_message(
            "Bot",
            "Hello! Welcome to the AI FAQ Chatbot. Ask me a question to get started."
        )
        self.entry.focus_set()

    def add_message(self, sender, message):
        self.chat_area.configure(state="normal")
        self.chat_area.insert(tk.END, f"{sender}: {message}\n\n")
        self.chat_area.see(tk.END)
        self.chat_area.configure(state="disabled")

    def send_message(self, event=None):
        question = self.entry.get().strip()

        if not question:
            return

        self.entry.delete(0, tk.END)
        self.add_message("You", question)

        query_vector = self.vectorizer.transform([question])
        scores = cosine_similarity(query_vector, self.question_vectors)[0]

        best_index = scores.argmax()
        best_score = scores[best_index]

        if best_score >= 0.18:
            answer = self.answers[best_index]
        else:
            answer = (
                "Sorry, I could not find a matching FAQ. "
                "Please try asking about AI, machine learning, Python, NLP, or databases."
            )

        self.add_message("Bot", answer)

    def clear_chat(self):
        self.chat_area.configure(state="normal")
        self.chat_area.delete("1.0", tk.END)
        self.chat_area.configure(state="disabled")
        self.add_message("Bot", "Chat cleared! Ask me a new question.")


if __name__ == "__main__":
    root = tk.Tk()
    app = FAQChatbot(root)
    root.mainloop()
