# Bench fixture: inert text. The host never resolves.
import urllib.request
urllib.request.urlopen(urllib.request.Request("http://sim.invalid/beacon", data=b"hello"))
