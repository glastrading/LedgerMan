import wx, webbrowser

SOURCE_URL = "https://github.com/finnmglas/LedgerMan"
DOCS_URL = "https://ledgerman.readthedocs.io"
DONATE_URL = "https://sponsor.finnmglas.com"


class MainView(wx.Frame):
    def __init__(self, *args, **kwargs):
        super(MainView, self).__init__(*args, **kwargs)

        self.build_ui()

    def build_ui(self):

        menubar = wx.MenuBar()

        # File Menu

        menu_file = wx.Menu()
        menu_file.Append(wx.ID_NEW, "&New")
        menu_file.Append(wx.ID_OPEN, "&Open")
        menu_file.Append(wx.ID_SAVE, "&Save")
        menu_file.AppendSeparator()

        menu_file_quit = wx.MenuItem(menu_file, wx.ID_EXIT, "&Quit")
        menu_file.Append(menu_file_quit)
        self.Bind(wx.EVT_MENU, self.quit, menu_file_quit)

        menubar.Append(menu_file, "&File")

        # Resource Menu

        menu_resources = wx.Menu()

        menu_resources_source = wx.MenuItem(
            menu_resources, wx.ID_ANY, "Source (&GitHub)"
        )
        menu_resources.Append(menu_resources_source)
        self.Bind(
            wx.EVT_MENU,
            lambda e: webbrowser.open(SOURCE_URL),
            menu_resources_source,
        )

        menu_resources_docs = wx.MenuItem(menu_resources, wx.ID_ANY, "&Documentation")
        menu_resources.Append(menu_resources_docs)
        self.Bind(
            wx.EVT_MENU,
            lambda e: webbrowser.open(DOCS_URL),
            menu_resources_docs,
        )
        menu_resources.AppendSeparator()

        menu_resources_sponsor = wx.MenuItem(
            menu_resources, wx.ID_ANY, "&Sponsor LedgerMan"
        )
        menu_resources.Append(menu_resources_sponsor)
        self.Bind(
            wx.EVT_MENU,
            lambda e: webbrowser.open(DONATE_URL),
            menu_resources_sponsor,
        )

        menubar.Append(menu_resources, "&Resources")

        # Finish setup

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
