# -*- coding: utf-8 -*-

###########################################################################
## Python code generated with wxFormBuilder (version Oct 26 2018)
## http://www.wxformbuilder.org/
##
## PLEASE DO *NOT* EDIT THIS FILE!
###########################################################################

import wx
import wx.xrc
import wx.grid


###########################################################################
## Class MainFrame
###########################################################################
from app.client.gui.new_match_dlg import NewMatchDialog


class MainFrame(wx.Frame):

    def __init__(self, parent):
        wx.Frame.__init__(self, parent, id=wx.ID_ANY, title=u"Darts!", pos=wx.DefaultPosition, size=wx.Size(766, 436),
                          style=wx.DEFAULT_FRAME_STYLE | wx.TAB_TRAVERSAL)

        self.SetSizeHints(wx.DefaultSize, wx.DefaultSize)

        fgSizer1 = wx.FlexGridSizer(2, 1, 0, 0)
        fgSizer1.SetFlexibleDirection(wx.BOTH)
        fgSizer1.SetNonFlexibleGrowMode(wx.FLEX_GROWMODE_SPECIFIED)

        fgSizer1.SetMinSize(wx.Size(300, 400))
        self.m_staticText3 = wx.StaticText(self, wx.ID_ANY, u"Your Username:", wx.DefaultPosition, wx.DefaultSize, 0)
        self.m_staticText3.Wrap(-1)

        fgSizer1.Add(self.m_staticText3, 0, wx.ALL, 5)

        self.m_userName = wx.TextCtrl(self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0)
        fgSizer1.Add(self.m_userName, 0, wx.ALL, 5)

        self.m_matchGrid = wx.grid.Grid(self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, 0)

        # Grid
        self.m_matchGrid.CreateGrid(5, 4)
        self.m_matchGrid.EnableEditing(False)
        self.m_matchGrid.EnableGridLines(True)
        self.m_matchGrid.SetGridLineColour(wx.SystemSettings.GetColour(wx.SYS_COLOUR_BTNHIGHLIGHT))
        self.m_matchGrid.EnableDragGridSize(False)
        self.m_matchGrid.SetMargins(0, 0)

        # Columns
        self.m_matchGrid.EnableDragColMove(False)
        self.m_matchGrid.EnableDragColSize(True)
        self.m_matchGrid.SetColLabelSize(30)
        self.m_matchGrid.SetColLabelAlignment(wx.ALIGN_CENTER, wx.ALIGN_CENTER)

        # Rows
        self.m_matchGrid.EnableDragRowSize(True)
        self.m_matchGrid.SetRowLabelSize(80)
        self.m_matchGrid.SetRowLabelAlignment(wx.ALIGN_CENTER, wx.ALIGN_CENTER)

        # Label Appearance

        # Cell Defaults
        self.m_matchGrid.SetDefaultCellAlignment(wx.ALIGN_LEFT, wx.ALIGN_TOP)
        fgSizer1.Add(self.m_matchGrid, 0, wx.ALL, 5)

        self.m_newMatch = wx.Button(self, wx.ID_ANY, u"New Match", wx.DefaultPosition, wx.DefaultSize, 0)
        fgSizer1.Add(self.m_newMatch, 0, wx.ALL, 5)

        self.m_newMatch.Bind(wx.EVT_BUTTON, self.onclick)

        self.SetSizer(fgSizer1)
        self.Layout()

        self.Centre(wx.BOTH)

    def __del__(self):
        pass


if __name__ == '__main__':
    # When this module is run (not imported) then create the app, the
    # frame, show it, and start the event loop.
    app = wx.App()
    frm = MainFrame(None)
    frm.Show()
    app.MainLoop()
