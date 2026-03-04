#!/usr/bin/env python3
"""Splash screen displayed during arcade cabinet startup."""

import tkinter as tk
import sys
import os


def main():
    root = tk.Tk()
    root.title("IUT Arcade")
    root.configure(bg="white")
    root.attributes("-fullscreen", True)
    root.attributes("-topmost", True)

    frame = tk.Frame(root, bg="white")
    frame.place(relx=0.5, rely=0.5, anchor="center")

    tk.Label(frame, text="IUT Arcade", font=("Helvetica", 48, "bold"), bg="white", fg="black").pack(pady=20)

    status_var = tk.StringVar(value="Chargement...")
    tk.Label(frame, textvariable=status_var, font=("Helvetica", 20), bg="white", fg="#555555").pack(pady=10)

    # Read status updates from a temp file written by lancerBorne.sh
    status_file = "/tmp/arcade_status"

    def poll_status():
        if os.path.exists(status_file):
            try:
                with open(status_file) as f:
                    msg = f.read().strip()
                if msg == "READY":
                    root.destroy()
                    return
                if msg:
                    status_var.set(msg)
            except OSError:
                pass
        root.after(500, poll_status)

    root.after(500, poll_status)
    root.mainloop()


if __name__ == "__main__":
    main()
