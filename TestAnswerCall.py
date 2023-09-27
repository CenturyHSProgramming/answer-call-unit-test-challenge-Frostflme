# TestAnswerCall.py

# Import Statements
import unittest
import answerCall

class KnownValues(unittest.TestCase):
    def test_answerCallForUnknownSameAreaCodeGoodTime(self):
        # Capture the results of the function
        result = answerCall.answerCall("U", True, "09:00")
        # Check for expected output
        self.assertEqual(True, result)

    def test_answerCallForUnknownDifferentAreaCodeGoodTime(self):
        # Capture the results of the function
        result = answerCall.answerCall("U", False, "14:00")
        # Check for expected output
        self.assertEqual(False, result)

    def test_answerCallForUnknownSameAreaCodeBadTime(self):
        # Capture the results of the function
        result = answerCall.answerCall("U", True, "23:50" )
        # Check for expected output
        self.assertEqual(False, result)

    def test_answerCallForTelemarketerSameAreaCodeGoodTime(self):
        # Capture the results of the function
        result = answerCall.answerCall("T", True, "10:40" )
        # Check for expected output
        self.assertEqual(False, result)

    def test_answerCallForTelemarketerDifferentAreaCodeBadTime(self):
        # Capture the results of the function
        result = answerCall.answerCall("T", False, "23:00" )
        # Check for expected output
        self.assertEqual(False, result)

    def test_answerCallForFriendDifferentAreaCodeGoodTime(self):
        # Capture the results of the function
        result = answerCall.answerCall("F", False, "10:00")
        # Check for expected output
        self.assertEqual(True, result)

    def test_answerCallForFriendDifferentAreaCodeBadTime(self):
        # Capture the results of the function
        result = answerCall.answerCall("F", False, "23:00")
        # Check for expected output
        self.assertEqual(False, result)

    def test_answerCallForFriendDifferentAreaCodeGoodTime_2(self):
        # Capture the results of the function
        result = answerCall.answerCall("F", False, "13:00")
        # Check for expected output
        self.assertEqual(True, result)

    def test_answerCallForRelativeDifferentAreaCodeGoodTime(self):
        # Capture the results of the function
        result = answerCall.answerCall("R", False, "9:00")
        # Check for expected output
        self.assertEqual(True, result)

    def test_answerCallForRelativeDifferentAreaCodeBadTime(self):
        # Capture the results of the function
        result = answerCall.answerCall("R", False, "04:00")
        # Check for expected output
        self.assertEqual(False, result)

    def test_answerCallForRelativeDifferentAreaCodeGoodTime_2(self):
        # Capture the results of the function
        result = answerCall.answerCall("R", False, "16:00")
        # Check for expected output
        self.assertEqual(True, result)

# Run the tests
if __name__ == '__main__':
    unittest.main()
