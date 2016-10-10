# (c) Copyright 2014-2016 Synapse Wireless, Inc.
"""
This wxPython application participates in the "McastCount" multi-snap-node
demonstration. Protoboards use LEDs and buttons to show/increment the
network-wide count. This application uses a wx.StaticText and a
wx.Button instead.
"""

import logging
import wx
from snapconnect import snap

# Configure the type and port of your bridge node
#BRIDGE_NODE = {'type':snap.SERIAL_TYPE_SNAPSTICK100, 'port':0} # Serial connections
#BRIDGE_NODE = {'type':'TCP', 'host':'10.82.5.4', 'port':None} # TCP connections
BRIDGE_NODE = {'type': snap.SERIAL_TYPE_RS232, 'port': 0}  # Serial connections

# Basic logging
logging.basicConfig(level=logging.DEBUG, format='%(asctime)-15s %(levelname)-8s %(name)-8s %(message)s')

def setButtonCount(value):
    """Set the value of the button count."""
    frame.buttonCount = value
    stCount.SetLabel("Count: " + str(frame.buttonCount))

def guiButtonPressed(event):
    """Update the GUI text and other nodes' values for button Count"""
    setButtonCount(frame.buttonCount + 1)  # locally
    comm.mcastRpc(1, 2, 'setButtonCount', frame.buttonCount)  # RPC to other nodes

# The wx application object
app = wx.App()

# Frame, panel, static-text, and button ... with sizers
frame = wx.Frame(None, title="Mcast Counter")
panel = wx.Panel(frame)
stCount = wx.StaticText(panel)
stCount.SetMinSize((150, -1))
btInc = wx.Button(panel, label="Increment")
box = wx.BoxSizer(wx.HORIZONTAL)
box.Add(btInc, border=10, flag=wx.ALL)
box.Add(stCount, border=10, flag=wx.ALL | wx.ALIGN_CENTER_VERTICAL)
panel.SetSizerAndFit(box)
boxo = wx.BoxSizer(wx.VERTICAL)
boxo.Add(panel)
frame.SetSizerAndFit(boxo)

setButtonCount(0)  # initialize the button count to 0
frame.Bind(wx.EVT_BUTTON, guiButtonPressed)  # register for button clicks

# Create the SNAPconnect instance and expose the 'setButtonCount' function
comm = snap.Snap(funcs={'setButtonCount': setButtonCount})
if BRIDGE_NODE['type'] == 'TCP':
    comm.connect_tcp(BRIDGE_NODE['host'], port=BRIDGE_NODE['port'])
else:
    comm.open_serial(BRIDGE_NODE['type'], BRIDGE_NODE['port'])

# Start a timer that fires every 20ms and gives the SNAPconnect
# instance some attention
poller = wx.Timer(frame)
frame.Bind(wx.EVT_TIMER, lambda event: comm.poll())
poller.Start(20, wx.TIMER_CONTINUOUS)

# Show the frame and start the wx event loop
frame.Show()
app.MainLoop()
