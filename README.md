# answerCall()
A Python 3 If-Structure challenge with unit tests. Your job: program Python to automatically answer calls or not based on 

**Rules:**
----------
* if you don't know the caller and it's a different area code, don't answer
* if you don't know the caller and it's the same area code, answer
* if it's a relative or friend, answer
* if it's a telemarketer, don't answer
* if it's after 10pm or before 7am, don't answer (no matter who it is)
<!-- I'd answer a call from a friend or relative in the middle of the night -->

**Inputs:**
----------
* **answerCall()** receives three inputs (string boolean string): caller_code, sameAreaCode, and cur_time
  * **caller_codes**: are as follows:
    * "U" = unknown
    * "F" = friend
    * "R" = relative
    * "T" = telemarketer
  * **sameAreaCode** is a Boolean
    * True = same area code as yours
    * False = different area code as yours
  * **cur_time** stands for current time and is in the 24-hour (military time) format
    * "09:15" = 9:15AM
    * "12:00" = 12:00PM
    * "14:00" = 2:00PM
    * "22:45" = 10:45PM
    * "00:30" = 12:30AM
    
**Outputs:**
------------
* **answerCall()** returns 1 output (a boolean): 
    * True = answer the call
    * False = don't answer the call
    
**Examples:** 
inputs => output/s
--------------------------------
* "U" True "09:00" => True
* "U" False "14:00" => False
* "U" True "23:50" => False
* "T" True "10:40" => False
* "T" False "23:00" => False
* "F" False "10:00' => True
* "F" False "23:00" => False
* "R" True "9:00" => True
* "R" False "4:00" => False
