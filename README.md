"""
(c) Copyright 2014-2015 Synapse Wireless, Inc.

McastCounter.py - A simple example of SNAP Connect and wxPython

=== Background ===

The McastCounter application is installed on the engines delivered with the EK2500,
EK2100, and DK-200 evaluation kits. The application provides a distributed button-click
counter across multiple nodes.

This GUI application provides a wxPython GUI that participates in the McastCounter
multi-node demonstration via SNAP Connect.

=== Running McastCounter.py ===

This example uses the wxPython GUI library from www.wxpython.org.
Install this library if you don't already have it, for example:

        pip install wxpython

This example was most recently tested against wxPython version 3.0.1.1.
Other wxPython versions (both older and newer) may also work.

Edit the "BRIDGE_NODE" tuple near the top of the code to provide the serial
interface "type" and "port" of your bridge node.
    
Once you have edited McastCounter.py for your available hardware, simply do:

python McastCounter.py

A small wxPython dialog box should appear, containing a button labeled "Increment"
as well as a "Count:" field. "setButtonCount()" calls from other SNAP nodes should
update the "Count:" field, and you can also trigger setButtonCount() calls from the
SNAP Connect application by clicking on the "Increment" button.

For more details, refer to source file McastCounter.py.

Refer to the 'McastCounter.py' SNAPpy script for more information about the
McastCounter demo. 
"""
