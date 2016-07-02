from app.functions import ext_allowed


def test_ext_allowed():
    ext_checks = ['check.jpg', 'check.png', 'check.txt', 'check.doc', 'check.pdf', 'check.docx']
    trues = 0

    for ext in ext_checks:
        check = ext_allowed(ext)
        if check:
            trues += 1

    assert trues == 2


def test_ext_allowed_no_split():
    fail = 'failing'

    assert ext_allowed(fail) is None
