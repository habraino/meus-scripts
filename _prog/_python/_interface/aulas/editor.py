import tkinter as tk

class Window(tk.Tk):

    def __init__(self):
        super().__init__()
        self.title('My Editor')

        self.curent = tk.StringVar()

        self.txt = tk.Text(self, fg='#000000', bg='#ffffff', font=('calibre 13'))
        self.txt.bind('<KeyRelease>', self.update_index)
        self.txt.bind('<Control-h>', self.highlight_line)
        self.txt.bind('<Control-w>', self.highlight_word)
        self.txt.bind('<Control-d>', self.down_three_lines)
        self.txt.bind('<Control-b>', self.back_four_chars)
        self.txt.bind('<Control-t>', self.tag_alternating)
        self.txt.bind('<Control-r>', self.raise_selected)
        self.txt.bind('<Control-u>', self.underline_selected)
        self.txt.bind('<Control-p>', self.tag_python)

        self.txt.pack(side=tk.TOP, expand=True, fill=tk.BOTH)

        self.lb = tk.Label(self, textvar=self.curent, fg='#ffffff', bg='#002020')
        self.lb.pack(side=tk.BOTTOM, expand=True, fill=tk.X)

    def update_index(self, event=None):
        cursor_position = self.txt.index(tk.INSERT)
        cursor_position_pieces = str(cursor_position).split('.')

        cursor_line = cursor_position_pieces[0]
        cursor_char = cursor_position_pieces[1]

        self.curent.set('line: {}  char: {}  index: {}'.format(cursor_line, cursor_char, str(cursor_position)))

    def down_three_lines(self, event=None):
        current_cursor_index = str(self.txt.index(tk.INSERT))
        new_position = current_cursor_index + '+3l'
        self.txt.mark_set(tk.INSERT, new_position)

        return 'break'

    def back_four_chars(self, event=None):
        current_cursor_index = str(self.txt.index(tk.INSERT))
        new_position = current_cursor_index + '-4c'
        self.txt.mark_set(tk.INSERT, new_position)

        return 'break'

    def highlight_line(self, event=None):
        self.start = str(self.txt.index(tk.INSERT)) + 'linestart'
        self.end = str(self.txt.index(tk.INSERT)) + 'lineend'
        self.txt.tag_add('sel', self.start, self.end)

        return 'break'

    def highlight_word(self, event=None):
        word_pos = str(self.txt.index(tk.INSERT))
        start = word_pos + "wordstart"
        end = word_pos + "wordend"
        self.txt.tag_add(tk.INSERT, start, end)

        return 'break'

    def tag_alternating(self, event=None):
        for i in range(0, 27, 2):
            self.index = '1.' + str(i)
            self.end = self.index + '+1c'
            self.txt.tag_add('even', self.index, self.end)
            self.txt.tag_configure('even', foreground='orange')

            return "break"

    def raise_selected(self, event=None):
        self.txt.tag_configure('raise', offset=5)
        selection = self.txt.tag_ranges("sel")
        self.txt.tag_add('raise', selection[0], selection[1])

        return "break"

    def underline_selected(self, event=None):
        self.txt.tag_configure('underline', underline=1)
        selection = self.txt.tag_ranges("sel")
        self.txt.tag_add('underline', selection[0], selection[1])

        return "break"

    def tag_python(self, event=None):
        self.txt.tag_configure('python', foreground="#00ff00")

        start = 1.0
        idx = self.txt.search('python', start, stopindex=tk.END)
        while idx:
            tag_begin = idx
            tag_end = f"{idx}+6c"
            self.txt.tag_add('python', tag_begin, tag_end)
            start = tag_end
            idx = self.txt.search('python', start, stopindex=tk.END)
        return "break"


if __name__ == '__main__':
    window = Window()
    window.mainloop()


