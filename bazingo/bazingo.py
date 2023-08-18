"""
Success Criteria:

1. Must allow tabs to opened, closed, moved, be renamed, added, removed, etc.
2. Close button that doesn't use file (dynamic images using PIL with the json color and char ✕ (or maybe tksvg when it gets updated)) and can be binded to a function.
3. Can scroll through tabs (.misc.ScrollableFrame).
4. Can drag tabs around (https://stackoverflow.com/questions/59114409/moving-a-widget-on-a-canvas-in-python).
5. No flicker when switching tabs.
6. Must be efficient (no lag when switching tabs) (uses forgets to save memory) (Will require tests).
7. Must be able to add images to tabs and group tabs.
"""

# See https://github.com/thonny/thonny/blob/master/thonny/custom_notebook.py for inspiration.


class BazingoTab:
    def __init__(self) -> None:
        pass


class TabView:
    def __init__(self) -> None:
        pass
