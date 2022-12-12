import tkinter as tk
import ttkbootstrap as ttk
import ttkbootstrap.constants as ttkc


class MainApplication(tk.Frame):
    def __init__(self, parent, *args, **kwargs):
        tk.Frame.__init__(self, parent, *args, **kwargs)
        self.parent = parent

        b1 = ttk.Button(self, text="Button 1", bootstyle=ttkc.SUCCESS)
        b1.pack(side=ttkc.LEFT, padx=5, pady=10)

        b2 = ttk.Button(self, text="Button 2", bootstyle=(ttkc.INFO, ttkc.OUTLINE))
        b2.pack(side=ttkc.LEFT, padx=5, pady=10)

        # <create the rest of your GUI here>


if __name__ == "__main__":
    root = tk.Tk()
    MainApplication(root).pack(side="top", fill="both", expand=True)
    root.mainloop()
