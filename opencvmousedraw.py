# -*- coding: utf-8 -*-
"""
Basic example of using the mouse to draw a rectangle in a openCV window 

@author: Roger Woodman
"""


import cv2
import numpy

class DrawTest():

    def __init__(self):    
        """Initialise drawing variables"""
        # Flag for wether the user has clicked and now dragging
        self.drawing = False
        # Points for the rectangle
        self.point1 = (-1, -1)
        self.point2 = (-1, -1)
        # Initial image
        self.imageMain = numpy.zeros((512, 512, 3), numpy.uint8)
        # Image to draw on
        self.imageDraw = self.imageMain.copy()    

    def draw(self, event, x, y, params, flags):
        """Handles mouse callback events"""
        if(event == cv2.EVENT_LBUTTONDOWN and not self.drawing):
            self.drawing = True
            self.point1 = x,y
        elif (event == cv2.EVENT_MOUSEMOVE and self.drawing):
            self.imageDraw = self.imageMain.copy()
            cv2.rectangle(self.imageDraw, self.point1, (x,y), (0,255,0), 1)
        elif event == cv2.EVENT_LBUTTONUP:
            if(self.drawing):
                self.point2 = x, y
            self.drawing = False

if __name__ == '__main__':
    
    # Create drawing object
    drawTest = DrawTest()
    # Create an openCV window
    cv2.namedWindow('Draw test')
    # Attach an even handler to the window
    cv2.setMouseCallback('Draw test', drawTest.draw)
    print("Press Escape to exit the program")
    
    # Loop until user presses escape
    while(True):
        cv2.imshow('Draw test', drawTest.imageDraw)
        # Press escape to exit the program
        k = cv2.waitKey(1) & 0xFF
        if k == 27:
            break
        
    # close CV window
    cv2.destroyAllWindows()