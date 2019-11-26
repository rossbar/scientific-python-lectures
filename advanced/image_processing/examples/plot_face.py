"""
Displaying a Racoon Face
========================

Small example to plot a racoon face.
"""

from scipy import misc
from imageio import imwrite
f = misc.face()
imwrite('face.png', f) # uses the Image module (PIL)

import matplotlib.pyplot as plt
plt.imshow(f)
plt.show()
