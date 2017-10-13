'''
初始化函数
'''

import wx

def init():
    app = wx.App()

    frm = wx.Frame(None, title="Hello World")
    frm.Show()

    app.MainLoop()