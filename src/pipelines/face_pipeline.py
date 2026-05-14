import dlib
import numpy as np
import face_recognition_models
from sklearn.svm import SVC
import streamlit as st
from src.database.db import get_all_students


@st.cache_resource
def load_dlib_models():

    detector = dlib.get_frontal_face_detector()

    sp = dlib.shape_predictor(
        face_recognition_models.pose_predictor_model_location()
    )

    facerec = dlib.face_recognition_model_v1(
        face_recognition_models.face_recognition_model_location()
    )

    return detector, sp, facerec


def preprocess_image(image_np):

    # RGBA -> RGB
    if len(image_np.shape) == 3 and image_np.shape[2] == 4:
        image_np = image_np[:, :, :3]

    # Ensure uint8
    image_np = image_np.astype(np.uint8)

    # Ensure contiguous array
    image_np = np.ascontiguousarray(image_np)

    return image_np


def get_face_embeddings(image_np):

    image_np = preprocess_image(image_np)

    detector, sp, facerec = load_dlib_models()

    faces = detector(image_np, 1)

    encodings = []

    for face in faces:

        shape = sp(image_np, face)

        face_descriptor = facerec.compute_face_descriptor(
            image_np,
            shape
        )

        encodings.append(np.array(face_descriptor))

    return encodings


@st.cache_resource
def get_trained_model():

    X = []
    y = []

    student_db = get_all_students()

    if not student_db:
        return None

    for student in student_db:

        embedding = student.get("face_embedding")

        if embedding:

            X.append(np.array(embedding))
            y.append(student.get("student_id"))

    if len(X) == 0:
        return None

    # ONLY ONE STUDENT
    if len(set(y)) < 2:

        return {
            "clf": None,
            "X": X,
            "y": y
        }

    clf = SVC(
        kernel='linear',
        probability=True,
        class_weight='balanced'
    )

    try:

        clf.fit(X, y)

    except Exception as e:

        st.error(f"Training Error: {e}")

        return None

    return {
        "clf": clf,
        "X": X,
        "y": y
    }


def train_classifier():

    st.cache_resource.clear()

    model_data = get_trained_model()

    return bool(model_data)


def predict_attendance(class_image_np):

    class_image_np = preprocess_image(class_image_np)

    encodings = get_face_embeddings(class_image_np)

    detected_student = {}

    model_data = get_trained_model()

    if not model_data:
        return detected_student, [], len(encodings)

    clf = model_data["clf"]

    X_train = model_data["X"]

    y_train = model_data["y"]

    all_students = sorted(list(set(y_train)))

    for encoding in encodings:

        # MULTIPLE STUDENTS
        if clf is not None and len(all_students) >= 2:

            predicted_id = int(
                clf.predict([encoding])[0]
            )

        # SINGLE STUDENT
        else:

            predicted_id = int(all_students[0])

        student_embedding = X_train[
            y_train.index(predicted_id)
        ]

        best_match_score = np.linalg.norm(
            student_embedding - encoding
        )

        resemblance_threshold = 0.6

        if best_match_score <= resemblance_threshold:

            detected_student[predicted_id] = True

    return detected_student, all_students, len(encodings)