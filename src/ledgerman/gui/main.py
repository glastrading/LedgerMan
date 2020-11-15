import wx


class MainView(wx.Frame):
    def __init__(self, *args, **kwargs):
        super(MainView, self).__init__(*args, **kwargs)

        self.build_ui()

    def build_ui(self):

        menubar = wx.MenuBar()

        fileMenu = wx.Menu()
        fileMenu.Append(wx.ID_NEW, "&New")
        fileMenu.Append(wx.ID_OPEN, "&Open")
        fileMenu.Append(wx.ID_SAVE, "&Save")
        fileMenu.AppendSeparator()

        imp = wx.Menu()
        imp.Append(wx.ID_ANY, "Import newsfeed list...")
        imp.Append(wx.ID_ANY, "Import bookmarks...")
        imp.Append(wx.ID_ANY, "Import mail...")

        fileMenu.Append(wx.ID_ANY, "I&mport", imp)

        qmi = wx.MenuItem(fileMenu, wx.ID_EXIT, "&Quit\tCtrl+W")
        fileMenu.Append(qmi)

        self.Bind(wx.EVT_MENU, self.quit, qmi)

        menubar.Append(fileMenu, "&File")
        self.SetMenuBar(menubar)

        self.SetSize((600, 400))
        self.SetTitle("LedgerMan")
        self.Centre()

    def quit(self, e):
        self.Close()


def main():

    app = wx.App()
    ex = MainView(None)
    ex.Show()
    app.MainLoop()
