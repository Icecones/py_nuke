
# Stefan Thorsson
# sthorsson@gmail.com

import os, nuke

def st_writeNodeSuffix(custom):
    # make sure custom param doesnt connect with values ahead of it
    if custom:
        custom = "_" + custom

    # get selected nodes
    writeNodes = nuke.selectedNodes()
    for wnode in writeNodes:
        if wnode.Class() == "Write":
            # Get top node in chain
            topnode_name = nuke.tcl("full_name [topnode %s]" % wnode.name()) 
            topnode = nuke.toNode(topnode_name) 
        
            # Path to read node
            fullPath = nuke.filename(topnode)
            pathOnly = os.path.dirname(topnode['file'].value())
            writePath = pathOnly + '/'
            
            # Focal Length
            fLength = topnode.metadata()['input/focal_length']
            focalSplit = fLength.split('/',1)
            focal = focalSplit[0]
            focal = focal + "MM"
        
            # Split up "File.jpg" to "File" and ".jpg"    
            fullPathSplit   = fullPath.split("/")
            fileName       = fullPathSplit[len(fullPathSplit)-1]
            fileNameSplit = fileName.split('.')
            
            # Define write path and assign to Write Node
            writePath = (writePath + fileNameSplit[0] + "_" + focal + custom + "." + fileNameSplit[1])
            wnode['file'].setValue(writePath)
            # Print the result
            print (wnode.name() + " : " + (wnode['file'].getValue()))

