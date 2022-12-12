import tkinter as tk
import tkinter.filedialog as fd
import ttkbootstrap as ttk
import ttkbootstrap.constants as ttkc


class MainApplication(tk.Frame):
    def __init__(self, parent, *args, **kwargs):
        tk.Frame.__init__(self, parent, *args, **kwargs)
        self.parent = parent

        self.btnOpenFile = ttk.Button(
            self, text="Open file", bootstyle=ttkc.SUCCESS, command=self.browseFiles
        )
        self.btnOpenFile.pack(side=ttkc.LEFT, padx=5, pady=10)

        self.btnQuit = ttk.Button(
            self, text="Quit", bootstyle=(ttkc.INFO, ttkc.OUTLINE), command=self.quit
        )
        self.btnQuit.pack(side=ttkc.LEFT, padx=5, pady=10)

        self.lblFileName = ttk.Label(self, bootstyle=(ttkc.DEFAULT))

        # <create the rest of your GUI here>

    def browseFiles(self):
        filename = fd.askopenfilename(
            initialdir="~/Downloads",
            title="Select data source",
            filetypes=(
                ("Excel files", "*.xlsx *.xls"),
                ("Comma separated", "*.csv"),
                ("All files", "*.*"),
            ),
        )

        if filename != "":
            self.lblFileName.pack(side=ttkc.BOTTOM, padx=5, pady=10)
            self.lblFileName.configure(text="File Opened: " + filename)
        else:
            self.lblFileName.pack_forget()


if __name__ == "__main__":
    root = tk.Tk()
    root.wm_title("pyVTAC")
    MainApplication(root).pack(side="top", fill="both", expand=True)
    root.mainloop()
