#!/usr/bin/env python3
# coding: koi8-r
# ====================================================
#	Cycle - calendar for women
#	Distributed under GNU Public License
# Author: Oleg S. Gints (altgo@users.sourceforge.net)
# Home page: http://cycle.sourceforge.net
# ===================================================
import builtins
import gettext
from set_dir import *
from dialogs import *
from save_load import *
from cal_year import *
import wx.lib.colourdb
import wx.html
import wx
import os
import sys
import gettext
import locale

#from prn import *

lang_find = False
if not '__WXMSW__' in wx.PlatformInfo:
    for lang_env_var in ('LANGUAGE', 'LC_ALL', 'LC_CTYPE', 'LANG'):
        if lang_find:
            break
        if lang_env_var in os.environ:
            env_language = os.environ[lang_env_var]
            for s_lang in env_language.split(':'):  # if set more languages
                os.environ[lang_env_var] = s_lang
                try:
                    dl = locale.getdefaultlocale()
                    lang = [dl[0][0:2]]
                    l = gettext.translation('cycle', msg_dir, lang)
                    if wx.USE_UNICODE:
                        builtins.__dict__['_'] = lambda s: l.ugettext(s)
                    else:
                        builtins.__dict__['_'] = lambda s: l.ugettext(
                            s).encode(dl[1])
                    _('try decode this string')
                    lang_find = True
                    break  # language was found
                except:
                    pass
else:  # for MS Windows
    try:
        dl = locale.getdefaultlocale()
        lang = [dl[0][0:2]]
        l = gettext.translation('cycle', msg_dir, lang)
        if wx.USE_UNICODE:
            builtins.__dict__['_'] = lambda s: l.ugettext(s)
        else:
            builtins.__dict__['_'] = lambda s: l.ugettext(s).encode(dl[1])
        _('try decode this string')
        lang_find = True
    except:
        pass

if not lang_find:
    builtins.__dict__['_'] = lambda s: s
    lang = [""]


class MyFrame(wx.Frame):
    def __init__(self, parent, ID, title):
        wx.Frame.__init__(self, parent, ID, title,
                          wx.DefaultPosition, wx.Size(800, 600))

#	self.printer = wx.HtmlEasyPrinting()
        icon = wx.Icon(os.path.join(
            icons_dir, 'mini/cycle.xpm'), wx.BITMAP_TYPE_XPM)
        self.SetIcon(icon)

        Val.frame = self
        self.CreateStatusBar()
        self.MakeToolMenu()  # toolbar

        self.cal = Cal_Year(self)
        self.OnCurrent(self)
        self.Bind(wx.EVT_CLOSE, self.OnCloseWindow)

    def OnCloseWindow(self, event):
        Save_Cycle(cycle.name, cycle.passwd, cycle.file)
        self.Destroy()

    def TimeToQuit(self, event):
        self.Close(True)

    def MakeToolMenu(self):
        tb = self.CreateToolBar(wx.TB_HORIZONTAL | wx.NO_BORDER)
        tb.SetToolBitmapSize(wx.Size(24, 24))

        qDec=SetToolPath(self, tb, 10, os.path.join(
                bitmaps_dir, 'dec.png'), _('Dec Year'))
        self.Bind(wx.EVT_TOOL, self.OnDecYear, qDec)

        qCurr=SetToolPath(self, tb, 20, os.path.join(
                bitmaps_dir, 'curr.png'), _('Current Year'))
        self.Bind(wx.EVT_TOOL, self.OnCurrent, qCurr)

        qInc=SetToolPath(self, tb, 30, os.path.join(
                bitmaps_dir, 'inc.png'), _('Inc Year'))
        self.Bind(wx.EVT_TOOL, self.OnIncYear, qInc)

        tb.SetToolSeparation(50)
        tb.AddSeparator()

        qLeg=SetToolPath(self, tb, 40, os.path.join(
                bitmaps_dir, 'legend.png'), _('Legend'))
        self.Bind(wx.EVT_TOOL, self.Legend, qLeg)

        qExp=SetToolPath(self, tb, 45, os.path.join(
                bitmaps_dir, 'export.png'), _('Export to iCal'))
        self.Bind(wx.EVT_TOOL, self.Export, qExp)

        qSett=SetToolPath(self, tb, 50, os.path.join(
                bitmaps_dir, 'set.png'), _('Settings'))
        self.Bind(wx.EVT_TOOL, self.Settings, qSett)

        qHelp=SetToolPath(self, tb, 55, os.path.join(
                bitmaps_dir, 'help.png'), _('Help'))
        self.Bind(wx.EVT_TOOL, self.Info, qHelp)

#	SetToolPath(self, tb, 57, os.path.join(bitmaps_dir,'help.png'), _('Print'))
#	wx.EVT_TOOL(self, 57, self.test)

        tb.AddSeparator()

        qExit=SetToolPath(self, tb, 60, os.path.join(
                bitmaps_dir, 'exit.png'), _('Exit'))
        self.Bind(wx.EVT_TOOL, self.TimeToQuit, qExit)

        tb.Realize()

    def test(self, event):
        #rpt = report_year(self.cal.year)
        # self.printer.PreviewText(rpt)
        # self.printer.PreviewFile('2.html')
        dlg = Colour_Dlg(self)
        dlg.ShowModal()
        dlg.Destroy()

    def Legend(self, event):
        dlg = Legend_Dlg(self)
        dlg.ShowModal()
        dlg.Destroy()

    def Export(self, event):
        dlg = wx.FileDialog(self, _("Export to iCal"),
                            style=wx.FD_SAVE)

        if dlg.ShowModal() == wx.ID_OK:
            try:
                fileobj = file(dlg.GetPath(), "w")
                report_year_ical(self.cal.year, fileobj)
            except (IOError, OSError) as err:
                wx.MessageDialog(
                    self, str(err), _("Unable to export"), style=wx.OK).ShowModal()

    def Settings(self, event):
        dlg = Settings_Dlg(self)
        if dlg.ShowModal() == wx.ID_OK:
            self.cal.Set_Year(wx.DateTime.Today().GetYear())
        dlg.Destroy()

    def Info(self, event):
        global lang
        f_name = os.path.join(doc_dir, "README_"+lang[0]+".html")
        if not os.path.isfile(f_name):
            f_name = os.path.join(doc_dir, "README.html")
        f = open(f_name, "r")
        msg = f.read()
        dlg = Help_Dlg(self, _('Help'), msg)
        dlg.ShowModal()

    # increment and decrement toolbar controls

    def OnIncYear(self, event):
        self.cal.Inc_Year()

    def OnDecYear(self, event):
        self.cal.Dec_Year()

    def OnCurrent(self, event):
        self.cal.Set_Year(wx.DateTime.Today().GetYear())


# ----------------------------------------------
def SetToolPath(self, tb, id, bmp, title):
    global dir_path
#    tb.AddSimpleTool(id, wx.Bitmap(os.path.join(dir_path, bmp), wx.BITMAP_TYPE_PNG),
#                     title, title)
    return tb.AddTool(id, "", wx.Bitmap(os.path.join(dir_path, bmp), wx.BITMAP_TYPE_PNG),
                     wx.NullBitmap, wx.ITEM_NORMAL, title, title)


class MyApp(wx.App):
    def OnInit(self):
        wx.lib.colourdb.updateColourDB()
        ret = first_login()
        if ret == 'bad_login':
            return True
        elif ret == 'not_first':
            dlg = Login_Dlg(None)
            if dlg.ShowModal() == wx.ID_CANCEL:
                dlg.Destroy()
                return True
            dlg.Destroy()
        self.frame_init()
        return True

    def frame_init(self):
        frame = MyFrame(None, -1, "")
        frame.Show(True)
        self.SetTopWindow(frame)


if __name__ == '__main__':
    locale.setlocale(locale.LC_ALL, "")
    dir_path = os.getcwd()
    app = MyApp(0)
    app.MainLoop()
