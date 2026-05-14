import io
import numpy as np
import librosa
import streamlit as st

from resemblyzer import (
    VoiceEncoder,
    preprocess_wav
)


@st.cache_resource
def load_voice_encoder():

    return VoiceEncoder()


def cosine_similarity(a, b):

    a = np.array(a)
    b = np.array(b)

    return np.dot(a, b) / (
        np.linalg.norm(a)
        * np.linalg.norm(b)
    )


def get_voice_embedding(audio_bytes):

    try:

        if not audio_bytes:
            return None

        encoder = load_voice_encoder()

        audio, sr = librosa.load(
            io.BytesIO(audio_bytes),
            sr=16000
        )

        # Empty audio check
        if len(audio) == 0:

            st.warning("Empty audio detected")

            return None

        wav = preprocess_wav(audio)

        embedding = encoder.embed_utterance(wav)

        return embedding.tolist()

    except Exception as e:

        st.error(f"Voice Recognition Error: {e}")

        return None


def identify_speaker(
    new_embedding,
    candidates_dict,
    threshold=0.70
):

    best_sid = None

    best_score = -1.0

    if new_embedding is None:
        return None, 0

    for sid, stored_embedding in candidates_dict.items():

        if stored_embedding:

            similarity = cosine_similarity(
                new_embedding,
                stored_embedding
            )

            if similarity > best_score:

                best_score = similarity
                best_sid = sid

    if best_score >= threshold:

        return best_sid, best_score

    return None, best_score


def process_bulk_audio(
    audio_bytes,
    candidates_dict,
    threshold=0.70
):

    try:

        if not audio_bytes:
            return {}

        encoder = load_voice_encoder()

        audio, sr = librosa.load(
            io.BytesIO(audio_bytes),
            sr=16000
        )

        if len(audio) == 0:
            return {}

        segments = librosa.effects.split(
            audio,
            top_db=30
        )

        identified_results = {}

        for start, end in segments:

            # Ignore very short segments
            if (end - start) < sr * 1.0:
                continue

            segment_audio = audio[start:end]

            wav = preprocess_wav(segment_audio)

            embedding = encoder.embed_utterance(wav)

            sid, score = identify_speaker(
                embedding,
                candidates_dict,
                threshold
            )

            if sid:

                if (
                    sid not in identified_results
                    or score > identified_results[sid]
                ):

                    identified_results[sid] = score

        return identified_results

    except Exception as e:

        st.error(f"Bulk Audio Error: {e}")

        return {}