#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""Subclass of wx.Panel"""

#-----------------------------------------------------------------------------------------
#Import
try:
    #wxPython
    import wx
    #python std library
    import sys
    #Grass modules nad packages
    from gui_core.gselect import Select
    #our modules and packages

except ImportError as err:
    print(u"ImportError: {}".format(err))
    sys.exit("-1")
#-----------------------------------------------------------------------------------------

class InputOutputPanel(wx.Panel):
    """
    Subclass of wx.Panel.
    Represents top-left part of the window.
    Contains selection of input and output mapsets
    and selection of data field which should be reclassify.
    """
    #-----------------------------------------------------------------------------------------

    def __init__(self, parent, id):

        wx.Panel.__init__(self, parent, id)
        #INPUT
        self.__buildInputPanel()
        #FIELD
        self.__buildFieldPanel()
        #OUTPUT
        self.__buildOutputPanel()
        #LAYOUT
        self.__layout()
        self.SetMinSize((400, -1))

        self.fieldPanel.Hide() #may not be needed at all
    #-----------------------------------------------------------------------------------------


    def __buildInputPanel(self):
        """
        Creates input combo box with label.
        :return: void
        """
        self.inputPanel = wx.Panel(self, wx.NewId())
        self.input = Select(self.inputPanel, wx.NewId(), type='raster')
        self.inputLabel = wx.StaticText(self.inputPanel, wx.NewId(), "Input raster map", size=(120, -1))

        inputBox = wx.BoxSizer(wx.HORIZONTAL)
        inputBox.Add(self.inputLabel, 0, wx.ALIGN_CENTER)
        inputBox.Add(self.input, wx.EXPAND, wx.ALIGN_CENTER)

        self.inputPanel.SetSizer(inputBox)
    #-----------------------------------------------------------------------------------------


    def __buildFieldPanel(self):
        """
        Creates field combo box with label.
        :return: void
        """
        self.fieldPanel = wx.Panel(self, wx.NewId())
        self.field = wx.ComboBox(self.fieldPanel, wx.NewId())
        self.fieldLabel = wx.StaticText(self.fieldPanel, wx.NewId(), "Field", size=(120, -1))
        fieldBox = wx.BoxSizer(wx.HORIZONTAL)
        fieldBox.Add(self.fieldLabel, 0, wx.ALIGN_CENTER)
        fieldBox.Add(self.field, wx.EXPAND, wx.ALIGN_CENTER)
        self.fieldPanel.SetSizer(fieldBox)
    #-----------------------------------------------------------------------------------------


    def __buildOutputPanel(self):
        """
        Creates output text control with label.
        :return: void
        """
        self.outputPanel = wx.Panel(self, wx.NewId())
        #self.output = wx.TextCtrl(self.outputPanel, wx.NewId())
        self.output = Select(self.outputPanel, wx.NewId(), type='raster')
        self.outputLabel = wx.StaticText(self.outputPanel, wx.NewId(), "Output raster map", size=(120, -1))
        outputBox = wx.BoxSizer(wx.HORIZONTAL)
        outputBox.Add(self.outputLabel, 0, wx.ALIGN_CENTER)
        outputBox.Add(self.output, wx.EXPAND, wx.ALIGN_CENTER)
        self.outputPanel.SetSizer(outputBox)
    #-----------------------------------------------------------------------------------------


    def __layout(self):
        """
        Specifies final layout in InputOutputPanel.
        :return: void
        """
        margin = 5
        box = wx.StaticBox(self, wx.NewId(), "Input and Output")
        vBox = wx.StaticBoxSizer(box, wx.VERTICAL)
        vBox.Add(self.inputPanel, 0, wx.ALL | wx.EXPAND, margin)
        vBox.Add(self.fieldPanel, 0, wx.ALL | wx.EXPAND, margin)
        vBox.Add(self.outputPanel, 0, wx.ALL | wx.EXPAND, margin)
        self.SetSizer(vBox)
    #-----------------------------------------------------------------------------------------


if __name__ == "__main__":
    pass
