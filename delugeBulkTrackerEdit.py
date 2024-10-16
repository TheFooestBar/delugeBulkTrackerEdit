#!/usr/bin/env python3

import os,sys,re,pickle,argparse
import deluge.core

def printTrackers(state):
    for torrent in state.torrents:
        print(f'[] {torrent.filename}')
        for tracker in torrent.trackers:
            print(f'   - {tracker["url"]}')

def replaceTracker(state, trackerOld, trackerNew):
    for torrent in state.torrents:
        updatedTrackers = []
        
        for tracker in torrent.trackers:
            if trackerOld in tracker["url"]:
                updatedTrackers.append(tracker['url'])
                tracker['url'] = trackerNew
                
        if len(updatedTrackers) != 0:
            print(f'[] {torrent.filename}')
            for tracker in updatedTrackers:
                print(f'   Updated: [{tracker}] => [{trackerNew}]')

    return state

def main(argv):
    parser = argparse.ArgumentParser(description="Update Deluge torrent trackers in bulk because Deluge cannot")

    subparser = parser.add_subparsers(dest='command')

    parser_replace = subparser.add_parser('replace')
    parser_replace.add_argument(
        '-f', '--state-file',
        help        = 'Path to torrents.state file',
        dest        = 'stateFile',
        type        = str,
        required    = True
    )
    parser_replace.add_argument(
        '-o', '--old-tracker',
        help        = 'Tracker to filter on for replacement',
        dest        = 'trackerOld',
        type        = str,
        required    = True
    )
    parser_replace.add_argument(
        '-n', '--new-tracker',
        help        = 'Tracker to use for the replacement',
        dest        = 'trackerNew',
        type        = str,
        required    = True
    )

    parser_print = subparser.add_parser('print')
    parser_print.add_argument(
        '-f', '--state-file',
        help        = 'Path to torrents.state file',
        dest        = 'stateFile',
        type        = str,
        required    = True
    )

    args = parser.parse_args()

    if not args.command:
        parser.print_help()
        return False
    
    with open(args.stateFile, 'rb') as _file:
        state = pickle.load(_file, encoding='utf8')

    if   args.command == 'print':
        printTrackers(state)
    elif args.command == 'replace':
        stateNew = replaceTracker(state, args.trackerOld, args.trackerNew)

        with open(args.stateFile + '.new', 'wb') as _file:
            pickle.dump(stateNew, _file)

exit(main(sys.argv))
