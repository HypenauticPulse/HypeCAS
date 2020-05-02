import sys
import traceback


class TracePrints(object):
    # Sourced from the selected answer at https://stackoverflow.com/questions/1617494/finding-a-print-statement-in
    # -python
    def __init__(self):
        self.stdout = sys.stdout

    def write(self, s):
        self.stdout.write("Writing %r\n" % s)
        traceback.print_stack(file=self.stdout)
