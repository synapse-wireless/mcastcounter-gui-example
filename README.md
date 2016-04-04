[![](https://cloud.githubusercontent.com/assets/1317406/12406044/32cd9916-be0f-11e5-9b18-1547f284f878.png)](http://www.synapse-wireless.com/)

# SNAPconnect Example - McastCounter GUI in wxPython

![wxPython McastCounter Demo](https://cloud.githubusercontent.com/assets/1317406/14266506/61511b30-fa8e-11e5-9fe0-7d905a0f81ea.gif)

This example application provides a wxPython GUI that participates in the McastCounter
multi-node demonstration via SNAPconnect.

## Background

The McastCounter SNAPpy script is pre-installed on SNAP modules delivered with the EK2500, EK2100, and DK-200 evaluation kits.
It provides a distributed button-click counter across multiple nodes.

## Running This Example

This example uses the wxPython GUI library from www.wxpython.org.
Install this library if you don't already have it, for example:

```bash
pip install wxpython
```

This example was most recently tested against wxPython version 3.0.1.1.
Other wxPython versions (both older and newer) may also work.

Edit the `BRIDGE_NODE` tuple near the top of [McastCounter.py](McastCounter.py) to provide the serial
interface "type" and "port" of your bridge node.

Once you have edited McastCounter.py for your available hardware, simply run:

```bash
python McastCounter.py
```

A small wxPython dialog box should appear, containing a button labeled "Increment"
as well as a "Count:" field. "setButtonCount()" calls from other SNAP nodes should
update the "Count:" field, and you can also trigger setButtonCount() calls from the
SNAPconnect application by clicking on the "Increment" button.

For more details, refer to source file [McastCounter.py](McastCounter.py).

Refer to the 'McastCounter.py' SNAPpy script for more information about the McastCounter demo.

## License

Copyright © 2016 [Synapse Wireless](http://www.synapse-wireless.com/), licensed under the [Apache License v2.0](LICENSE.md).

<!-- meta-tags: vvv-snapconnect, vvv-wx, vvv-gui,vvv-python, vvv-example -->
