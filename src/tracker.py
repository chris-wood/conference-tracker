import json
import sys
import pprint

ansiRed = "\x1b[31m";
ansiGreen = "\x1b[32m";
ansiYellow = "\x1b[33m";
ansiBlue = "\x1b[34m";
ansiMagenta = "\x1b[35m";
ansiCyan = "\x1b[36m";
ansiReset = "\x1b[0m";

def colorize(color, chars):

    result = chars
    if color == "red":
        result = ansiRed + chars + ansiReset
    elif color == "green":
        result = ansiGreen + chars + ansiReset
    elif color == "yellow":
        result = ansiYellow + chars + ansiReset
    elif color == "blue":
        result = ansiBlue + chars + ansiReset
    elif color == "magenta":
        result = ansiMagenta + chars + ansiReset
    elif color == "cyan":
        result = ansiCyan + chars + ansiReset
    else:
        raise Exception("Bad color: %s" % (color))

    return result

def printColorized(color, string):
    print colorize(color, string)
    return

def findConferencesByQuery(query, database):
    conferences = []
    for conference in database:
        for topic in conference["topics"]:
            # print topic, query
            if query in topic:
                conferences.append(conference)
                break
    return conferences

def findJournalsByQuery(query, database):
    return []

def main(args):
    print "Conference Tracker"
    print "Enter a series of keywords and return some possible conferences"
    print ""

    conferenceDatabase = json.loads(open("./db/conferences.json").read())
    journalDatabase = json.loads(open("./db/journals.json").read())

    # prompt...
    # TODO: loop
    print "Sample text or keywords: ",
    queryString = sys.stdin.readline().strip()
    conferences = findConferencesByQuery(queryString, conferenceDatabase)
    journals = findJournalsByQuery(queryString, journalDatabase)

    printColorized("green", str(conferences))
    print journals

if __name__ == "__main__":
    main(sys.argv[1:])