# -*- coding: utf-8 -*-

###########################################################################
## Python code generated with wxFormBuilder (version Oct 26 2018)
## http://www.wxformbuilder.org/
##
## PLEASE DO *NOT* EDIT THIS FILE!
###########################################################################

import wx
import wx.xrc


###########################################################################
## Class NewMatchDialog
###########################################################################

class NewMatchDialog(wx.Dialog):

    def __init__(self, parent):
        wx.Dialog.__init__(self, parent, id=wx.ID_ANY, title=u"New Match", pos=wx.DefaultPosition,
                           size=wx.Size(207, 243), style=wx.DEFAULT_DIALOG_STYLE)

        self.SetSizeHints(wx.DefaultSize, wx.DefaultSize)

        bSizer2 = wx.BoxSizer(wx.VERTICAL)

        self.m_lblMatchType = wx.StaticText(self, wx.ID_ANY, u"Match Type", wx.DefaultPosition, wx.DefaultSize, 0)
        self.m_lblMatchType.Wrap(-1)

        bSizer2.Add(self.m_lblMatchType, 0, wx.ALL, 5)

        m_matchTypeChoices = []
        self.m_matchType = wx.ComboBox(self, wx.ID_ANY, u"501", wx.DefaultPosition, wx.DefaultSize, m_matchTypeChoices,
                                       0)
        bSizer2.Add(self.m_matchType, 0, wx.ALL, 5)

        self.m_lblNumPlayers = wx.StaticText(self, wx.ID_ANY, u"No. of Players", wx.DefaultPosition, wx.DefaultSize, 0)
        self.m_lblNumPlayers.Wrap(-1)

        bSizer2.Add(self.m_lblNumPlayers, 0, wx.ALL, 5)

        m_numPlayersChoices = []
        self.m_numPlayers = wx.ComboBox(self, wx.ID_ANY, u"2", wx.DefaultPosition, wx.DefaultSize, m_numPlayersChoices,
                                        0)
        bSizer2.Add(self.m_numPlayers, 0, wx.ALL, 5)

        self.m_button2 = wx.Button(self, wx.ID_ANY, u"Go!", wx.DefaultPosition, wx.DefaultSize, 0)
        bSizer2.Add(self.m_button2, 0, wx.ALL, 5)

        self.m_button3 = wx.Button(self, wx.ID_ANY, u"Cancel", wx.DefaultPosition, wx.DefaultSize, 0)
        bSizer2.Add(self.m_button3, 0, wx.ALL, 5)

        self.SetSizer(bSizer2)
        self.Layout()

        self.Centre(wx.BOTH)

    def __del__(self):
        pass
