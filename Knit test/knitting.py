from pyknit import *
sweaterSwatch = pyknit.GaugeSwatch(row_count=18, row_measure=3.25, stitch_count=24, stitch_measure=4, units="in")
print(sweaterSwatch.measurement_to_rows(11))
