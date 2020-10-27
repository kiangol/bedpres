# bedpres
Python program that checks ifinavet.no for available space at an event. Sends push notification when there is an available slot. 

## Usage

`bedpres.py` takes event id and refresh rate as input. This can be found in the URL of the event, e.g. https://ifinavet.no/event/325
The event id is **325**

```bash
python bedpres.py
> Enter event id (3 digits): 325
> Refresh rate in seconds: 30

```

To run headless mode, for example on Raspberry Pi, 
use the `bedpresheadless.py`. Modify `event_url` and `refresh_rate`. Runs without asking for input. 

```bash
python bedpresheadless.py
 ---- BEGIN ----
```

To run in background:
```bash
nohup python bedpresheadless.py & 
```
