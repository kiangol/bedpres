# bedpres
Python program that checks ifinavet.no for available space in an event. Sends push notification when there is an available slot. 

## Usage

`bedpres.py` takes event id and refresh rate as input.

```bash
python bedpres.py
> Enter event id (3 digits): 325
> Refresh rate in seconds: 30

```

To run headless mode, for example on Raspberry Pi, 
use the `bedpresheadless.py`. Modify event url and refresh rate. Runs without asking for input. 

```bash
python bedpresheadless.py
 ---- BEGIN ----
```
