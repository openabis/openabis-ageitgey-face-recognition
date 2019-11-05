import io

import numpy as np
from face_recognition import face_encodings, load_image_file, api

from .exceptions import FaceNotRecognized

DEFAULT_ENCODING = "128-dimension"
MATCHING_TOLERANCE = 0.5


class FaceRecognition:
    """
    Plugin for ageitgey/face-recognition library to be use for computing and matching facial biometrics.
    """

    def __init__(self, config):
        """
        :param config: Dictionary of environment variables. Required by OpenAbis.
        """
        pass

    def encode_image(self, face):
        image = load_image_file(io.BytesIO(face.image))

        try:
            # The method returns a list of encodings because an image can have multiple faces, since we are sure to
            # have a single face per image, we only get the first item from list
            face_encoding = face_encodings(image)[0]

        except IndexError:
            raise FaceNotRecognized

        image_encoding = face.encodings.add()
        image_encoding.name = DEFAULT_ENCODING
        image_encoding.encoding = face_encoding.dumps()

        return face

    def get_encoding(self, face):
        """
        Get the 128-dimensional encoding from face object
        :param face: Face object
        :return:
         If face object has the encoding, return ther 128-dimensional numpy array encoding of the image.
         If not, return an empty numpy array
        """
        for item in face.encodings:
            if item.name == DEFAULT_ENCODING:
                return np.loads(item.encoding)

        return np.empty(0)

    def match_face_encodings(self, known_face, face_to_compare):
        """
        Match face encodings
        :param known_face: Face object as the basis for verification
        :param face_to_compare: Face object to verify
        :return: Value of face distance as computed
        """
        known_face_encoding = self.get_encoding(known_face)
        face_encoding_to_compare = self.get_encoding(face_to_compare)

        if known_face_encoding.size < 1:
            known_face_encoding = self.encode_image(known_face)

        if face_encoding_to_compare.size < 1:
            known_face_encoding = self.encode_image(face_to_compare)

        face_distance = api.face_distance(
            face_encodings=[known_face_encoding], face_to_compare=face_encoding_to_compare
        )

        return face_distance[0]
