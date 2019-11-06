import io

import numpy as np
from face_recognition import face_encodings, load_image_file, api

from .exceptions import FaceNotRecognized, MultipleFacesDetected

# Default encoding from ageitgey/face-recognition
IMAGE_ENCODING = "128-dimension"


class FaceRecognition:
    """
    Plugin for ageitgey/face-recognition library to be use for computing and matching facial biometrics.
    """

    def __init__(self, config):
        """
        :param config: Environment configurations.
        """
        self.config = config

    def encode_image(self, face):
        """
        Encode image to 128-dimensional face encodings
        :param face: Face object
        :return: Face object
        """
        image = load_image_file(io.BytesIO(face.image))

        # The method returns a list of encodings because an image can have multiple faces.
        encodings = face_encodings(image)

        if len(encodings) < 1:
            raise FaceNotRecognized("No face detected in the image. A single face in the image is required.")
        elif len(encodings) > 1:
            raise MultipleFacesDetected(
                "Multiple faces are detected in the image. Please ensure a single face in the image."
            )
        face_encoding = encodings[0]
        face_template = face.template.add()
        face_template.format = IMAGE_ENCODING
        face_template.template = face_encoding.dumps()

        return face

    def get_encoding(self, face):
        for item in face.encodings:
            if item.format == IMAGE_ENCODING:
                return np.loads(item.template)

        return None

    def match_face_encodings(self, known_face, face_to_compare):
        known_face_encoding = self.get_encoding(known_face)
        face_encoding_to_compare = self.get_encoding(face_to_compare)
        face_distance = api.face_distance(
            face_encodings=[known_face_encoding], face_to_compare=face_encoding_to_compare
        )

        return face_distance
