import answerCall as screener


def test_answerCallForUnknownSameAreaCodeGoodTime():
    result = screener.answerCall("U", True, "09:00")
    expected = True
    assert result == expected


def test_answerCallForUnknownDifferentAreaCodeGoodTime():
    result = screener.answerCall("U", False, "14:00")
    expected = False
    assert result == expected


def test_answerCallForUnknownSameAreaCodeBadTime():
    result = screener.answerCall("U", True, "23:50")
    expected = False
    assert result == expected


def test_answerCallForTelemarketerSameAreaCodeGoodTime():
    result = screener.answerCall("T", True, "10:40")
    expected = False
    assert result == expected


def test_answerCallForTelemarketerDifferentAreaCodeBadTime():
    result = screener.answerCall("T", False, "23:00")
    expected = False
    assert result == expected


def test_answerCallForFriendDifferentAreaCodeGoodTime():
    result = screener.answerCall("F", False, "10:00")
    expected = True
    assert result == expected


def test_answerCallForFriendDifferentAreaCodeBadTime():
    result = screener.answerCall("F", False, "23:00")
    expected = False
    assert result == expected


def test_answerCallForFriendDifferentAreaCodeGoodTime_2():
    result = screener.answerCall("F", False, "13:00")
    expected = True
    assert result == expected


def test_answerCallForRelativeDifferentAreaCodeGoodTime():
    result = screener.answerCall("R", False, "9:00")
    expected = True
    assert result == expected


def test_answerCallForRelativeDifferentAreaCodeBadTime():
    result = screener.answerCall("R", False, "04:00")
    expected = False
    assert result == expected


def test_answerCallForRelativeDifferentAreaCodeGoodTime_2():
    result = screener.answerCall("R", False, "16:00")
    expected = True
    assert result == expected
