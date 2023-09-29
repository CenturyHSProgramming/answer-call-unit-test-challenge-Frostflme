# answerCall.py
# by _______

# For instructions on what to do, see README.md
# or visit (https://github.com/HundredVisionsGuy/answerCall)

# Write function defintion: answerCall()
def answerCall(caller_codes: str, sameAreaCode: bool, cur_time: str) -> bool:
    validTime = checkValidTime(cur_time)
    temp = checkCallerCode(caller_codes)
    isTelemarketer = temp[1]
    isFriendRelative = temp[0]

    # The nest of if statements
    if validTime:
        if isTelemarketer:
            return False
        elif isFriendRelative:
            return True
        else:
            if sameAreaCode:
                return True
            else:
                return False
    else: return False

# Make sure it returns a value

def checkValidTime(time: str) -> bool:
    """This function checks to see if the time is an acceptable time to respond to the call. If it's between 22:00 and 7:00 exclusive, then don't respond."""
    temp = time.split(":")
    hours, minutes = (int(temp[0]), int(temp[1]))
    if hours > 22 or hours < 7:
        return False
    elif hours == 22:
        if minutes != 0: return False
        else: return True
    else: return True

def checkCallerCode(caller: str) -> tuple:
    """This function checks the caller to see who's calling. It returns two booleans in a tuple, the first one representing if it's a friend or relative, and the second one representing if it's a telemarketer. Both shouln't be true at the same time."""
    if caller == "U":
        return (False, False)
    elif caller == "T":
        return (False, True)
    else:
        return (True, False)

if __name__ == '__main__':
    print(checkValidTime("11:27"))
    print(checkValidTime("20:23"))
    print(checkValidTime("00:00"))
    print(checkValidTime("22:00"))
    print(checkValidTime("22:01"))
    print(checkValidTime("7:00"))
    print(checkValidTime("6:59"))
    print()
    print(answerCall("U", True, "12:00"))
