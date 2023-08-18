from platform import system
from tkinter import Canvas, Event, Misc
from tkinter.ttk import Frame, Scrollbar

SYSTEM = system()


def scroll_fix(delta: int) -> int:
    """Corrects scrolling numbers across platforms"""

    # The scroll events passed by macOS, Linux, and Windows are different,
    # so they must to be rectified to work properly when dealing with the events.
    # Originally found here: https://stackoverflow.com/a/17457843/17053202
    if delta in (4, 5):
        # Linux device
        return 1 if delta == 4 else -1
    return -delta if SYSTEM == "Darwin" else delta // 120

class ScrollableFrame(Frame):
    """A frame that allows for both horizontal and vertical scrolling."""

    # Example usage:
    """
    from tkinter import Label, Tk

    from bazingo.misc import ScrollableFrame

    # Create the root
    root = Tk()

    # Create the frame
    frame = ScrollableFrame(root, orient="horizontal")  # Or use "vertical"
    frame.parent_frame.pack(fill="both", expand=True)

    # Add some labels
    counter = 1
    for i in range(100):
        lbl = Label(frame, text=f"Label {counter}")
        lbl.grid(row=0, column=i)
        counter += 1

    # Run the app
    root.mainloop()

    """

    def __init__(
        self,
        master: Misc,
        orient: str = "horizontal",
        scrollbar: bool = False,
        *args,
        **kwargs,
    ):
        # Set the orient attribute
        self.orient = orient

        # Create the parent items
        self.parent_frame = Frame(master, *args, **kwargs)
        self.parent_canvas = Canvas(self.parent_frame, highlightthickness=0)

        # Call the parent constructor directly
        Frame.__init__(self, self.parent_canvas, *args, **kwargs)

        # Create the canvas and the scrollbar
        if "height" in kwargs:
            self.parent_canvas.configure(height=kwargs["height"])
        if "width" in kwargs:
            self.parent_canvas.configure(width=kwargs["width"])
        if scrollbar:
            self.scrollbar = Scrollbar(self.parent_frame, orient=orient)

        # Grid the canvas and set the column and row weights
        self.parent_canvas.grid(row=0, column=0, sticky="nsew")
        self.parent_frame.rowconfigure(0, weight=1)
        self.parent_frame.columnconfigure(0, weight=1)

        # Grid the scrollbar and configure the canvas/scrollbar
        if scrollbar:
            if self.orient == "horizontal":
                self.scrollbar.grid(row=1, column=0, sticky="ew")
                self.parent_canvas.configure(xscrollcommand=self.scrollbar.set)
                self.scrollbar.configure(command=self.parent_canvas.xview)
            else:
                self.scrollbar.grid(row=0, column=1, sticky="ns")
                self.parent_canvas.configure(yscrollcommand=self.scrollbar.set)
                self.scrollbar.configure(command=self.parent_canvas.yview)

        # Bind the mousewheel to the canvas
        self.parent_canvas.bind("<Enter>", self.create_binds)
        self.parent_canvas.bind("<Leave>", self.remove_binds)

        # Create the window in the canvas
        self.window_id = self.parent_canvas.create_window(
            0,
            0,
            window=self,
            anchor="nw",
            tags="self.frame",
            width=self.winfo_reqwidth(),
            height=self.winfo_reqheight(),
        )

        # Bind the config handler
        self.parent_canvas.bind(
            "<Configure>",
            lambda _: self.parent_canvas.configure(
                scrollregion=self.parent_canvas.bbox("all")
            ),
        )

        self.bind("<Map>", lambda _: self.update_canvas_window_size())

    def destroy(self) -> None:
        """Destroys the widget"""
        Frame.destroy(self)

    def create_binds(self, _: Event) -> None:
        """Binds the mousewheel to the canvas"""
        self.parent_canvas.bind_all("<Button-4>", self._on_mousewheel, add=True)
        self.parent_canvas.bind_all("<Button-5>", self._on_mousewheel, add=True)
        self.parent_canvas.bind_all("<MouseWheel>", self._on_mousewheel, add=True)

    def remove_binds(self, _: Event) -> None:
        """Unbinds the mousewheel from the canvas"""
        self.parent_canvas.unbind_all("<Button-4>")
        self.parent_canvas.unbind_all("<Button-5>")
        self.parent_canvas.unbind_all("<MouseWheel>")

    def _on_mousewheel(self, event: Event) -> None:
        """Handles mousewheel scrolling"""
        if event.delta == 0:
            event.delta = event.num
        if self.orient == "horizontal":
            self.parent_canvas.xview_scroll(scroll_fix(event.delta), "units")
        else:
            self.parent_canvas.yview_scroll(scroll_fix(event.delta), "units")

    def update_canvas_window_size(self) -> None:
        """Update the window size of the frame in the canvas"""

        # Update the window size of the frame in the canvas
        self.update_idletasks()
        self.parent_canvas.itemconfig(
            self.window_id, width=self.winfo_reqwidth(), height=self.winfo_reqheight()
        )
        self.parent_canvas.configure(scrollregion=self.parent_canvas.bbox("all"))

        # Update the scrollbar
        if hasattr(self, "scrollbar"):
            if self.orient == "horizontal":
                self.scrollbar.configure(command=self.parent_canvas.xview)
            else:
                self.scrollbar.configure(command=self.parent_canvas.yview)

        # Update the canvas size
        self.parent_canvas.configure(
            width=self.winfo_reqwidth()
            if self.orient == "vertical"
            else self.parent_frame.winfo_reqwidth(),
            height=self.winfo_reqheight()
            if self.orient == "horizontal"
            else self.parent_frame.winfo_reqheight(),
        )

        # Update the parent frame to the canvas size
        self.parent_frame.configure(
            width=self.winfo_reqwidth(), height=self.winfo_reqheight()
        )
