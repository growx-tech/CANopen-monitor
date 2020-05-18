import curses
from .frame_table import FrameTable


class Pane(FrameTable):
    def __init__(self,
                 name,
                 fields=[],
                 capacity=None,
                 stale_time=60,
                 dead_time=600):
        super().__init__(name=name,
                         capacity=capacity,
                         stale_time=stale_time,
                         dead_time=dead_time)
        self.window = curses.newwin(0, 0, 0, 0)
        self.name = name
        self.fields = fields
        self.selected = False

        self.scroll_pos = 0
        self.window.scrollok(True)

    def resize(self, width, height, x_off, y_off):
        self.window = curses.newwin(height, width, y_off, x_off)

    def scroll(self, rate = 1):
        max = len(self.table)
        self.scroll_pos += rate
        if(self.scroll_pos < 0): self.scroll_pos = 0
        elif(self.scroll_pos >= max): self.scroll_pos = max - 1

    def draw(self, width, height, x_off, y_off):
        self.resize(width, height, x_off, y_off)
        self.window.addstr(1, 1, self.name + "(" + str(len(self.table)) + ")")

        if(self.selected): banner_color = 5
        else: banner_color = 2
        self.window.chgat(1, 1, -1, curses.color_pair(banner_color))

        self.window.addstr(2, 1, "")
        for field in self.fields:
            self.window.addstr(str(field + ": "))
        self.window.chgat(2, 1, -1, curses.color_pair(6))

        for i, frame in enumerate(list(map(lambda x: self.table[x], self.ids()))):
            if(self.selected and i == self.scroll_pos): color = 7
            else: color = 0
            self.window.addstr(3 + i, 1, str(hex(frame.node_id)).ljust(6, ' ') + "\t" + frame.name.ljust(20, ' ') + frame.ndev.ljust(6, ' ') + "\t" + str(frame), curses.color_pair(color))

            self.window.chgat(3 + i, 1, -1, curses.color_pair(color))

        self.window.box()
        self.window.refresh()
