# coding: koi8-r
# ====================================================
#	Cycle - calendar for women
#	Distributed under GNU Public License
# Author: Oleg S. Gints (altgo@users.sourceforge.net)
# Home page: http://cycle.sourceforge.net
# ===================================================
import hashlib
import pickle
import os.path
import os
import cal_year
import wx
import warnings
# deprecated since release 2.3
warnings.filterwarnings("ignore",
                        category=DeprecationWarning,
                        message='.*rotor module', module=__name__)

try:
    import rotor
except:
    import p_rotor as rotor


def Save_Cycle(name='cycle', passwd='123', file='cycle'):
    """ Save the contents of our document to disk.
    """
    objSave = []
    m = hashlib.md5()
    m.update(passwd.encode('utf-8'))
    rt = rotor.newrotor(m.digest())
    objSave.append(['period', cal_year.cycle.period])
    objSave.append(['by_average', cal_year.cycle.by_average])
    objSave.append(['disp', cal_year.cycle.disp])
    objSave.append(['first_week_day', cal_year.cycle.first_week_day])
    objSave.append(['note', cal_year.cycle.note])
    for d in cal_year.cycle.begin:
        objSave.append(['begin', [d.GetDay(), d.GetMonth(), d.GetYear()]])

    for d in cal_year.cycle.last:
        objSave.append(['last', [d.GetDay(), d.GetMonth(), d.GetYear()]])

    for d in cal_year.cycle.tablet:
        objSave.append(['tablet', [d.GetDay(), d.GetMonth(), d.GetYear()]])

    for d in list(cal_year.cycle.colour_set.keys()):
        objSave.append(['colour', [d, cal_year.cycle.colour_set[d].Get()]])

    tmp = rt.encrypt(b'Cycle'+pickle.dumps(objSave))
    tmp = b"UserName="+pickle.dumps(name)+b"==="+tmp
    p, f_name = get_f_name(file)

    if not os.path.exists(p):
        os.mkdir(p, 0o700)
    f = open(f_name, "wb")
    f.write(tmp)
    f.close()
#    print "All data saved to disk"


def Load_Cycle(name='cycle', passwd='123', file='cycle'):

    p, f_name = get_f_name(file)
    if os.path.isfile(f_name):
        m = hashlib.md5()
        m.update(passwd.encode('utf-8'))
        rt = rotor.newrotor(m.digest())
        f = open(f_name, "rb")
        tmp = f.read()
        if tmp[:len(b"UserName=")] == b"UserName=":
            # new format
            n = tmp.find(b"===")+len(b"===")
            tmp = tmp[n:]  # remove username
        tmp = rt.decrypt(tmp)
        f.close()
        if tmp[0:5] != b'Cycle':
            #	    print 'Password is invalid'
            return False
        else:
            tmp = tmp[5:]  # remove control word 'Cycle'
            objLoad = pickle.loads(tmp)
            set_color_default()
            for type, d in objLoad:
                #		print "Load: ", type, d
                if type == 'period':
                    cal_year.cycle.period = int(d)
                elif type == 'by_average':
                    cal_year.cycle.by_average = int(d)
                elif type == 'disp':
                    cal_year.cycle.disp = int(d)
                elif type == 'first_week_day':
                    cal_year.cycle.first_week_day = int(d)
                elif type == 'begin':
                    dt = wx.DateTime.FromDMY(d[0], d[1], d[2])
                    cal_year.cycle.begin.append(dt)
                elif type == 'last':
                    dt = wx.DateTime.FromDMY(d[0], d[1], d[2])
                    cal_year.cycle.last.append(dt)
                elif type == 'tablet':
                    dt = wx.DateTime.FromDMY(d[0], d[1], d[2])
                    cal_year.cycle.tablet.append(dt)
                elif type == 'note':
                    cal_year.cycle.note = d.copy()
                elif type == 'colour':  # d=['item', (r,g,b)]
                    c = wx.Colour(d[1][0], d[1][1], d[1][2])
                    if d[0] in cal_year.cycle.colour_set:
                        cal_year.cycle.colour_set[d[0]] = c
                    else:
                        cal_yaar.cycle.colour_set.update({d[0]: c})
#	    print "Load OK"
            return True

# -------------------------------------------------------


def get_f_name(name=""):
    if '__WXMSW__' in wx.PlatformInfo:
        p = os.path.join(os.getcwd(), "data")
    else:
        p = os.path.expanduser("~/.cycle")
    f_name = os.path.join(p, name)

    return p, f_name

# -------------------------------------------------------


def set_color_default():
    cal_year.cycle.colour_set = {'begin': wx.TheColourDatabase.Find('RED'),
                                 'prog begin': wx.TheColourDatabase.Find('PINK'),
                                 'conception': wx.TheColourDatabase.Find('MAGENTA'),
                                 'safe sex': wx.TheColourDatabase.Find('WHEAT'),
                                 'fertile': wx.TheColourDatabase.Find('GREEN YELLOW'),
                                 'ovule': wx.TheColourDatabase.Find('SPRING GREEN'),
                                 '1-st tablet': wx.TheColourDatabase.Find('GOLD'),
                                 'pause': wx.TheColourDatabase.Find('LIGHT BLUE'),
                                 'next 1-st tablet': wx.TheColourDatabase.Find('PINK')}
