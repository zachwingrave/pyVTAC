import tkinter as tk
import tkinter.filedialog as tkfd
import tkinter.scrolledtext as tkst
import ttkbootstrap as ttk
import ttkbootstrap.constants as ttkc
import pandas as pd
import phonenumbers
import logging
import os


VC_ELIGIBILITY = "VC Scholarship"
COURSE_TITLE = "COURSE_TITLE"
STUDENT_ID = "S1SSP_STU_SPK_STU_ID"
PATHWAY = "Pathway Package"
MOBILE_NO = "MOBILE_PHONE_NO"
HOME_NO = "HOME_PHONE_NO"
STREAM = "Stream"
CAMPUS = "Community Services campus"
PATHWAY = "Pathway Package"


class MainApplication(tk.Frame):
    def __init__(self, parent, *args, **kwargs):
        tk.Frame.__init__(self, parent, *args, **kwargs)
        self.parent = parent
        self.writer = None
        self.data = None

        self.btnOpenFile = ttk.Button(
            self,
            text="Open file",
            bootstyle=ttkc.PRIMARY,
            command=self.browseFiles,
            state="enabled",
        )
        self.btnOpenFile.pack(side=ttkc.LEFT, padx=5, pady=10)

        self.btnSortData = ttk.Button(
            self,
            text="Sort data",
            bootstyle=ttkc.SUCCESS,
            command=self.sortData,
            state="disabled",
        )
        self.btnSortData.pack(side=ttkc.LEFT, padx=5, pady=10)

        self.btnOpenResults = ttk.Button(
            self,
            text="Open results",
            bootstyle=ttkc.INFO,
            command=self.openResults,
            state="disabled",
        )
        self.btnOpenResults.pack(side=ttkc.LEFT, padx=5, pady=10)

        self.btnQuit = ttk.Button(
            self,
            text="Quit",
            bootstyle=ttkc.DANGER,
            command=self.quit,
            state="enabled",
        )
        self.btnQuit.pack(side=ttkc.LEFT, padx=5, pady=10)

        self.stLogger = tkst.ScrolledText(self, state="disabled")
        handler = TextHandler(self.stLogger)
        self.logger = logging.getLogger()
        self.logger.addHandler(handler)
        self.stLogger.pack(side=ttkc.BOTTOM, padx=5, pady=10)

        self.logger.info("Main application window initialised")

        # <create the rest of your GUI here>

    def browseFiles(self):
        self.logger.debug("File dialog window opened")

        filename = tkfd.askopenfilename(
            initialdir="~/Downloads",
            title="Select data source",
            filetypes=(
                ("Excel files", "*.xlsx *.xls"),
                ("Comma separated", "*.csv"),
                ("All files", "*.*"),
            ),
        )

        if filename != "":
            try:
                self.logger.info("File Opened: " + filename)
                self.btnSortData.configure(state="enabled")
                self.writer = pd.ExcelWriter(
                    path=filename, mode="a", if_sheet_exists="replace"
                )
                self.data = pd.read_excel(io=filename, engine="openpyxl")
            except (PermissionError) as e:
                # self.logger.exception(e)
                self.logger.error(
                    "Error: File open in another program. Close and try again."
                )
                self.btnSortData.configure(state="disabled")
                self.btnOpenResults.configure(state="disabled")
                self.writer = None
                self.data = None
        else:
            self.logger.info("No file selected")
            self.btnSortData.configure(state="disabled")
            self.btnOpenResults.configure(state="disabled")
            self.writer = None
            self.data = None

        self.logger.debug("File dialog window closed")

    def openResults(self):
        self.logger.info("Opening results file")
        os.system('start EXCEL.EXE "' + self.writer.__fspath__() + '"')

    def dataSummary(self, data, header=None):
        dataSummary = {
            "Total rows": len(data.index),
            "Total cols": len(data.columns),
        }
        if header:
            self.logger.debug("Data summary for " + header)
        else:
            header = ""
            self.logger.debug("Data summary")
        for key in dataSummary:
            self.logger.debug(header + " " + key + ": " + str(dataSummary[key]))

    def sortData(self):
        self.logger.debug("Sorting data")

        self.dataSummary(self.data, "ALL RECORDS")  # Summarise initial data state
        self.btnSortData.configure(text="Sorting in progress", bootstyle=ttkc.WARNING)

        DF_ALL_RECORDS = self.data.sort_values(
            by=[STUDENT_ID, COURSE_TITLE], ascending=[True, True]
        )  # ready for cleaning

        """Step 1: Format phone numbers to modified international format"""

        def parseNumber(
            number,
        ):  # use 'phonenumbers' module to format phone numbers to AU
            try:
                parsedNumber = (
                    phonenumbers.format_number(
                        phonenumbers.parse(number, "AU"),
                        phonenumbers.PhoneNumberFormat.INTERNATIONAL,  # leads with international calling code, +61
                    )
                    .replace("+", "")  # drop the leading +
                    .replace(" ", "")  # drop spaces in the middle of the number
                )
                return parsedNumber
            except (phonenumbers.phonenumberutil.NumberParseException):
                if number == "nan":  # replace NaN with empty string
                    return ""
                else:
                    return number

        DF_ALL_RECORDS[MOBILE_NO] = DF_ALL_RECORDS.apply(
            lambda x: parseNumber(
                str(x[MOBILE_NO])
            ),  # apply the 'parseNumber' callback function to all row values in the MOBILE_NO column
            axis="columns",
        )

        DF_ALL_RECORDS[HOME_NO] = DF_ALL_RECORDS.apply(
            lambda x: parseNumber(
                str(x[HOME_NO])
            ),  # apply the 'parseNumber' callback function to all row values in the HOME_NO column
            axis="columns",
        )

        """Step 2: Append 'Stream' to 'Course Title' in brackets"""

        DF_ALL_RECORDS[COURSE_TITLE] = (
            DF_ALL_RECORDS[COURSE_TITLE]
            + " ("
            + DF_ALL_RECORDS[STREAM].fillna(value="")
            + ")"
        ).replace(
            to_replace=" \(\)", value="", regex=True
        )  # replace empty brackets resulting from empty STREAM field using a regular expression. Tested with https://regex101.com/

        """Step 3: Append 'Campus' to 'Course Title' """

        if CAMPUS in DF_ALL_RECORDS.columns:
            DF_ALL_RECORDS[COURSE_TITLE] = (
                DF_ALL_RECORDS[COURSE_TITLE]
                + " - "
                + DF_ALL_RECORDS[CAMPUS].fillna("")  # replace NaN with empty string
            ).replace(
                to_replace=" - $", value="", regex=True
            )  # replace dangling ' - ' resulting from empty CAMPUS field using a regular expression. Tested with https://regex101.com/

        """Step 4: Dedupe entire list by 'Student ID' (S1SSP_STU_SPK_STU_ID)"""

        self.logger.info(
            "Deduping list based on STUDENT_ID and creating sheet FIRST_CONTACT"
        )
        DF_FIRST_CONTACT = DF_ALL_RECORDS.drop_duplicates(subset=STUDENT_ID)
        self.dataSummary(DF_FIRST_CONTACT, "DF_FIRST_CONTACT")

        """TODO Step 5: Sort duplicate offers (i.e. packaged degrees) according to 'Course Title' enum (e.g. 'Diploma'=0, 'Advanced Diploma'=1, 'Bachelor'=2) and append higher course offer to lower course offer (lower first) - append with /"""

        # code here

        """Step 6: Filter deduped list from Step 5 into individual sheets for 'VC_SCHOLARSHIPS', 'AVIATION', 'HARD_PACKAGE', 'SOFT_PACKAGE', 'HARD_SINGLE', 'SOFT_SINGLE' """

        DF_VC_SCHOLARSHIP = DF_ALL_RECORDS[DF_ALL_RECORDS[VC_ELIGIBILITY] == "Yes"]
        DF_PACKAGE_OFFERS = DF_ALL_RECORDS[DF_ALL_RECORDS[PATHWAY] == "Yes"]
        DF_SINGLE_OFFERS = DF_ALL_RECORDS[DF_ALL_RECORDS[PATHWAY] != "Yes"]
        # DF_AVIATION = DF_ALL_RECORDS  # TODO
        # DF_HARD_PACKAGE = DF_ALL_RECORDS  # TODO
        # DF_SOFT_PACKAGE = DF_ALL_RECORDS  # TODO
        # DF_HARD_SINGLE = DF_ALL_RECORDS  # TODO
        # DF_SOFT_SINGLE = DF_ALL_RECORDS  # TODO

        """Step 7: Save all new sheets to disk"""

        self.logger.info("Saving sorted data to spreadsheet")
        DF_ALL_RECORDS.to_excel(self.writer, sheet_name="ALL_RECORDS")
        DF_FIRST_CONTACT.to_excel(self.writer, sheet_name="FIRST_CONTACT")
        DF_VC_SCHOLARSHIP.to_excel(self.writer, sheet_name="VC_SCHOLARSHIP")
        DF_PACKAGE_OFFERS.to_excel(self.writer, sheet_name="PACKAGE_OFFERS")
        DF_SINGLE_OFFERS.to_excel(self.writer, sheet_name="SINGLE_OFFERS")
        # DF_AVIATION.to_excel(self.writer, sheet_name="AVIATION")
        # DF_HARD_PACKAGE.to_excel(self.writer, sheet_name="HARD_PACKAGE")
        # DF_SOFT_PACKAGE.to_excel(self.writer, sheet_name="SOFT_PACKAGE")
        # DF_HARD_SINGLE.to_excel(self.writer, sheet_name="HARD_SINGLE")
        # DF_SOFT_SINGLE.to_excel(self.writer, sheet_name="SOFT_SINGLE")

        self.logger.debug("Saving file to disk")
        self.writer.close()

        self.btnSortData.configure(state="disabled")
        self.logger.debug("Data sort complete")
        self.openResults()
        self.btnOpenResults.configure(state="enabled")


class TextHandler(logging.Handler):
    """This class allows you to log to a Tkinter Text or ScrolledText widget
    Adapted from /u/johan: https://stackoverflow.com/questions/13318742/python-logging-to-tkinter-text-widget"""

    def __init__(self, loggingWidget):
        logging.Handler.__init__(self)

        logging.basicConfig(
            # filename="log/app.log",
            format="%(asctime)s %(levelname)-4s %(message)s",
            datefmt="%Y-%m-%d %H:%M:%S",
            level=logging.DEBUG,
        )

        self.log = loggingWidget
        self.setLevel(logging.DEBUG)
        formatter = logging.Formatter(
            fmt="%(asctime)s %(levelname)-4s %(message)s", datefmt="%Y-%m-%d %H:%M:%S"
        )
        self.setFormatter(formatter)

    def emit(self, record):
        msg = self.format(record)
        self.log.configure(state="normal")
        self.log.insert(ttk.END, msg + "\n")
        self.log.configure(state="disabled")


if __name__ == "__main__":
    root = tk.Tk()
    root.wm_title("pyVTAC")
    MainApplication(root).pack(side="top", fill="both", expand=True)
    root.mainloop()
