import pygtk
import gtk
import subprocess

class InputArea(object):
    def destroy(self, widget, data=None):
        gtk.main_quit()

    def search(self, widget, event):
        if event.keyval == gtk.keysyms.Return:
            print "search this shit: " + self.text.get_text()
            subprocess.Popen(['arandr'])
            gtk.main_quit()

    def __init__(self):
        self.window = gtk.Window(gtk.WINDOW_TOPLEVEL)
        self.window.connect("destroy", self.destroy)
        self.window.connect("key-press-event", self.search)
        self.text = gtk.Entry()
        self.window.add(self.text)
        self.text.show()
        self.window.show()

    def show(self):
        gtk.main()


if __name__ == "__main__":
    pass
