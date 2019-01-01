import tkinter as tk
from tkinter import ttk
from Resources.Values import strings, colors, fonts
from Code.ReturnTool import ReturnTool


class ReturnToolPage(tk.Frame):

    __bgColor = colors.bgColor
    __fgColor = colors.fgColor

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.__controller = controller
        self.config(bg=colors.bgColor)
        self.columnconfigure(0, weight=1)

        self.__initUI()

    def start(self, args):
        self.__returnTool = ReturnTool(self.__errorLabel, self.__tree, self.__controller.login)
        self.__returnTool.populateData()

    def __initUI(self):

        """
        ReturnToolPage UI.
        main functions which you can call:
            self.returnTool.cancelBooking()  --     will cancel booking based on your selection
            self.returnTool.returnItem()     --     will return an item based on your selection
            self.returnTool.populateData()   --     will populate all required data in your treeView
        """

        frame = tk.Frame(self, bg=self.__bgColor)
        frame.grid(row=0, column=0, sticky="", pady=40)

        self.__tree = ttk.Treeview(frame, columns=(strings.priceDay, strings.priceHalfDay))

        mScrollBar = ttk.Scrollbar(frame, orient='vertical', command=self.__tree.yview)
        self.__tree.configure(yscrollcommand=mScrollBar.set)

        self.__errorLabel = tk.Label(frame, bg=colors.bgColor, fg=colors.fgColor)
        self.__errorLabel.grid(row=0, column=0, sticky="WN")

        self.__tree.heading('#0', text=strings.tool)
        self.__tree.heading('#1', text=strings.hireDate)
        self.__tree.heading('#2', text=strings.returnDate)
        self.__tree.column('#1', stretch=tk.YES)
        self.__tree.column('#2', stretch=tk.YES)
        self.__tree.column('#0', stretch=tk.YES)
        self.__tree.grid(row=1, column=0, columnspan=2, pady=20, sticky="N")

        mScrollBar.grid(row=1, column=3, pady=20, sticky='WNS')

        returnButton = tk.Label(frame, text=strings.returnItem, bg=colors.bgColor, fg=colors.fgColor,
                                font=fonts.buttonFont)

        returnButton.grid(row=2, column=1)
        returnButton.bind("<Button-1>", lambda event: self.__returnTool.returnItem())

        cancelButton = tk.Label(frame, text=strings.cancelBooking, bg=colors.bgColor, fg=colors.fgColor,
                                font=fonts.buttonFont)

        cancelButton.grid(row=2, column=0)
        cancelButton.bind("<Button-1>", lambda event: self.__returnTool.cancelBooking())
