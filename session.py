import pickle


def load_user_session(session_bytes):
    return pickle.loads(session_bytes)
