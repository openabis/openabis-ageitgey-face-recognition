class FaceNotRecognized(Exception):
    """Exception for not recognized face in the image."""

    def __init__(self, *args):
        self.status = 400
        super(FaceNotRecognized, self).__init__(*args)


class MultipleFacesDetected(Exception):
    """Exception for multiple faces in the image."""

    def __init__(self, *args):
        self.status = 400
        super(MultipleFacesDetected, self).__init__(*args)
