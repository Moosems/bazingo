<h1 align="center">Bazingo 0.0.2</h1>

> **Note**
> If Python was installed via Homebrew, installed on Mac by default, or installed on Linux, tkinter will likely not work properly and may need to be installed via `brew install python-tk` or with the distro package manager on Linux as documented [here](https://tecadmin.net/how-to-install-python-tkinter-on-linux/).

## Description
`Bazingo` aims to replace the conventional `Notebook` widget with a less buggy and more customizable alternative. See [this](https://github.com/thonny/thonny/issues/2737) for some of the reaons why the package was created.

<!-- Insert image here -->

## Features (WIP)
- [ ] Customizable tabs
- [ ] Close tab button
- [ ] Scrollable tabs
- [ ] Draggable tabs
- [ ] No flicker when switching tabs
- [ ] Efficient
- [ ] Add images to tabs
- [ ] Group tabs
- [ ] Tests

## Installation
```bash
pip install bazingo
```

## Documentation

### `bazingo.py`

#### `class Bazingo`
Nothing is implemented yet.

#### `class BazingoTab`
Nothing is implemented yet.

### `misc.py`

#### `scroll_fix(delta: int) -> int`
Corrects scrolling numbers handed by tk across multiple platforms (Windows, Linux, and Mac). The scroll events passed by macOS, Linux, and Windows are all different so they  must to be rectified to work properly when dealing with the events. This function is used by the `ScrollableFrame` class.

#### `ScrollableFrame(self, master: Misc, orient: str = "horizontal", scrollbar: bool = False, *args, **kwargs)`
|Options|Description|Type|
|---|---|---|
|`master`|The parent widget.|`Misc`|
|`orient`|The orientation of the scroll bar. Can be either `"horizontal"` or `"vertical"`.|`str`|
|`scrollbar`|Whether or not to display a scroll bar. Defaults to `False`.|`bool`|
|`*args`|Arguments to be passed to the `Frame` class.|`tuple`|
|`**kwargs`|Keyword arguments to be passed to the `Frame` class.|`dict`|

A frame that allows for both horizontal and vertical scrolling. This class is used by the `Bazingo` class for the tab bar.


##### `ScrollableFrame.destroy(self) -> None`
Because of the way the `ScrollableFrame` class works, it requires a special `destroy` method to be called when the widget is destroyed. 

##### `ScrollableFrame.create_binds(self, _: Event) -> None`
Creates the binds for the scroll bar. This method is called by the `ScrollableFrame` class and should not be called manually. This is what uses the `scroll_fix` function to correct the scrolling numbers.

##### `ScrollableFrame.remove_binds(self, _: Event) -> None`
Removes the binds for the scroll bar. This method is called by the `ScrollableFrame` class and should not be called manually.

##### `ScrollableFrame._on_mousewheel(self, event: Event) -> None`
Handles the mouse wheel event. This method is called by the `ScrollableFrame` class and should not be called manually. This is the most important method in the `ScrollableFrame` class as it handles the scrolling.

##### `ScrollableFrame.update_canvas_window_size(self) -> None`
This method updates the size of the parent frame, canvas range, and scroll bar range. This method should be called after adding widgets to the `ScrollableFrame` class.

#### Basic usage (ScrollableFrame)
```python
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
```