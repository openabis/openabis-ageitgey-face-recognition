class FaceNotRecognized(Exception):
    """Exception for not recognized face in the image."""

    def __init__(self, message, *args):
        self.status = 400
        self.message = message
        super(FaceNotRecognized, self).__init__(message, *args)


class MultipleFacesDetected(Exception):
    """Exception for multiple faces in the image."""

    def __init__(self, message, *args):
        self.status = 400
        self.message = message
        super(MultipleFacesDetected, self).__init__(message, *args)
