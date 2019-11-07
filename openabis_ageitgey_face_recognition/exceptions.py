class FaceNotRecognized(Exception):
    """Exception for not recognized face in the image."""

    def __init__(self):
        self.status = 406


class MultipleFacesDetected(Exception):
    """Exception for multiple faces in the image."""

    def __init__(self):
        self.status = 406
