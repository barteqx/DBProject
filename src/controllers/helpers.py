global session

def logged():
    return session.login == 1


def is_policeman():
    return session.role == 1


def is_admin():
    return session.role == 2
