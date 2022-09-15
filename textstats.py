import sys
import textstat

if len (sys.argv) > 1:
    ls, ws, cs, ss = textstat.stats_from_filename(sys.argv[1])
    print(f"{ls} lines, {ws} words, {cs} characters, {ss} sentences")