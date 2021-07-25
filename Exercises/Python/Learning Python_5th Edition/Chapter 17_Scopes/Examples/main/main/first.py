X = 99      # This code doesn7t know about second.py
        
def setX(new):      # Accessor make external changes explicit
    global X        # And can manage access in a single place
    X = new