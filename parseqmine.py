#!/usr/bin/env python

import sys

def simple():
    qc = 0
    rc = 0
    cc = 0

    for line in sys.stdin:
        c = line[0]
        if c == 'P':
            qc += 1
        elif c == 'R':
            rc += 1
        elif c == 'C':
            cc += 1

    r = ""
    if qc > 0:
        r = r + "Q" + str(qc)
    if rc > 0:
        if r != "":
            r = r + " "
        r = r + "R" + str(rc)
    if cc > 0:
        if r != "":
            r = r + " "
        r = r + "C" + str(cc)
    if r:
        sys.stdout.write(r + "\n")
    else:
        sys.stdout.write("-\n")

def fancy():
    qc = 0
    rc = 0
    cc = 0
    tags = {}

    for line in sys.stdin:
        parts = line.strip().split(" ")
        c = parts[0][0]
        if c == 'P':
            qc += 1
        elif c == 'R':
            rc += 1
        elif c == 'C':
            cc += 1
        k = parts[1]
        if k == "(null)":
            k = "*"
        if k in tags:
            tags[k] += 1
        else:
            tags[k] = 1

    r = ""
    if qc > 0:
        r = r + "Q" + str(qc)
    if rc > 0:
        if r != "":
            r = r + " "
        r = r + "R" + str(rc)
    if cc > 0:
        if r != "":
            r = r + " "
        r = r + "C" + str(cc)
    
    if tags:
        r += " " + ",".join([ k + ":" + str(tags[k]) for k in tags.keys() ])

    if r:
        sys.stdout.write(r + "\n")
    else:
        sys.stdout.write("-\n")

if __name__ == "__main__":
    args = sys.argv[1:]
    sys.stdin.readline()
    if args:
        fancy()
    else:
        simple()

