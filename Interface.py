import tkinter as tk
from Markov import *
import unittest
import TestMarkov


def manual_input():
    global input_string, rules, text_box
    global res

    root = tk.Toplevel()

    label2 = tk.Label(root, text="Please input entry:")
    label2.pack()
    prepare_input(root)

    res = tk.Label(root)
    res.pack(side=tk.BOTTOM, padx=5, pady=5)


def prepare_input(root):
    entry = tk.Entry(root)
    entry.pack()
    stop_button_entry = tk.Button(root, text="Submit line", command=lambda: get_input_string(entry, root))
    stop_button_entry.pack()


def get_input_string(e, root):
    global input_string, text_box
    input_string = e.get()

    label3 = tk.Label(root, text="Please input rules (at least one). Divide them using newline. Do not use characters: : , ^")
    label3.pack()
    text_box = tk.Text(root)
    text_box.pack()
    stop_button = tk.Button(root, text="Submit", command=run_markov)
    stop_button.pack()


def get_rules():
    global text_box
    rules = text_box.get("1.0", tk.END).split("\n")[:-1]
    return rules


def run_tests():
    root2 = tk.Toplevel()
    suite = unittest.TestLoader().loadTestsFromModule(TestMarkov)
    tests_successful = unittest.TextTestRunner(verbosity=2).run(suite)

    label6 = tk.Label(root2, text=("Tests successful" if tests_successful.wasSuccessful() else "Tests failed!"))
    label6.pack(padx=10, pady=10)


def run_markov():
    ruleset = create_ruleset(get_rules())
    res_temp = markov(input_string, ruleset)
    res.configure(text=res_temp)


def create_interface():
    global input_string, rules
    window = tk.Tk()
    button_manual = tk.Button(window, text="Manual input", command=manual_input)
    button_manual.pack()
    button_tests = tk.Button(window, text="Run tests", command=run_tests)
    button_tests.pack()

    window.mainloop()
