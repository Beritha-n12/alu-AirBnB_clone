# console.py
import cmd

class HBNBCommand(cmd.Cmd):
    prompt = "(hbnb) "

    def do_quit(self, arg):
        """Quit the console."""
        return True

    def do_EOF(self, arg):
        """Exit on Ctrl+D."""
        return True

    def emptyline(self):
        """Do nothing on an empty line."""
        pass

if __name__ == '__main__':
    HBNBCommand().cmdloop()

