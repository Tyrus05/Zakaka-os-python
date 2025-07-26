import tkinter as tk
import os

// un terminal mon bb mon petit will
class TerminalOS:
    def __init__(self, root):
        self.root = root
        self.root.title("PyOS Terminal")
        self.root.configure(bg="black")

        # Zone de texte
        self.text = tk.Text(root, bg="black", fg="green", insertbackground="green",
                            font=("Courier", 12), wrap="word")
        self.text.pack(fill="both", expand=True)
        self.text.insert("end", "PyOS Terminal\nTape 'help' pour la liste des commandes.\n\npyos> ")
        self.text.bind("<Return>", self.execute_command)
        self.text.focus_set()

        self.prompt = "pyos> "
        self.command_start = self.text.index("insert")

    def execute_command(self, event):
        line = self.text.get("insert linestart", "insert lineend")
        command = line.replace(self.prompt, "").strip()

        output = self.handle_command(command)

        self.text.insert("end", "\n" + output + "\n" + self.prompt)
        self.text.see("end")
        return "break"

    def handle_command(self, command):
        if command == "help":
            return "Commandes disponibles: help, ls, pwd, echo [texte], exit"
        elif command == "ls":
            return "\n".join(os.listdir("."))
        elif command == "pwd":
            return os.getcwd()
        elif command.startswith("echo "):
            return command[5:]
        elif command == "exit":
            self.root.quit()
        else:
            return f"Commande inconnue: {command}"

if __name__ == "__main__":
    root = tk.Tk()
    app = TerminalOS(root)
    root.mainloop()
