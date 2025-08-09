QuickSocket
-

A simple wrapper for socket to easily build servers and clients.

---

Key Features:
-
- Converts all data to bytes using [dill](https://github.com/uqfoundation/dill)
- Sends the length of the data as a header automatically
---
`pip install git+https://github.com/MineFartS/QuickSocket`

---

Example Usage:
-
```
import quicksocket

# ======================================
# |             Server                 |
# ======================================

h = quicksocket.host(443)

for conn in h.listen():
    data = conn.recv()
    # do something with data
    conn.send(data)

# ======================================
# |              Client                |
# ======================================

c = quicksocket.client('127.0.0.1', 443)

data = 123

c.send(data)
resp = c.recv()
```
