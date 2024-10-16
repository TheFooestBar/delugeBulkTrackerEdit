# delugeBulkTrackerEdit

## Overview
Deluge stores tracker info under `config/state/torrents.state`, however, it is not stored in a format that you can easily search and replace. This script allows you to load this file and replace any trackers matching a keyword.

## Requirements

**NOTE:** This script is intended to run on the machine that has Deluge installed. It has all the dependencies installed.

But if want to run it elsewhere, install the requirements:
```
pip3 install --user -r requirements.txt
```

## Usage

Print all torrents and their trackers:
```
./delugeBulkTrackerEdit.py print --state-file torrents.state
```

Replace any trackers that contain "oldtracker" with a new URL:
```
./delugeBulkTrackerEdit.py replace --state-file torrents.state --old-tracker "oldtracker" --new-tracker "https://tracker.example.org/announce"
```