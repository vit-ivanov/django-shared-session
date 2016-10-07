def is_empty(session):
    try:
        if not bool(session._session_key) and not session._session_cache:
            return True
    except AttributeError:
        return True