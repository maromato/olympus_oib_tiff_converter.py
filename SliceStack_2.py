import os
import re
import time
import pickle
from ij.gui import GenericDialog
from ij.io import DirectoryChooser, FileSaver,OpenDialog
from ij import IJ, ImagePlus
from java.lang import Runtime, Runnable 
from loci.plugins.util import BFVirtualStack
from loci.formats import ChannelSeparator
 
def run():
srcDir = DirectoryChooser("Choose directory").getDirectory()
  if not srcDir:
    return
  
  targetDir = DirectoryChooser("Choose target directory").getDirectory()
  if targetDir is None:
    # User canceled the dialog
    return
  
  sId = ".tiff"  	
  iStack = 0
  
  for root, directories, filenames in os.walk(srcDir):
    for filename in filenames:
      path = os.path.join(root,filename)
      if not (sId in filename):
         continue
 
      cs = ChannelSeparator()
      cs.setId(path)
      print "cs" ,cs
      bf = BFVirtualStack(path, cs, False, False, False)
      for sliceIndex in xrange(1, bf.getSize() +1):
        print "Processing slice", sliceIndex
        ip = bf.getProcessor(sliceIndex)
        sliceFileName = os.path.join(targetDir+filename+"_"+str(sliceIndex) + ".tif")
        print sliceFileName
        #FileSaver(ImagePlus(str(sliceIndex), ip)).saveAsTiff(sliceFileName)
 
run()
