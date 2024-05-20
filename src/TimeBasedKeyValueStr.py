# 981. Time Based Key-Value Store
# https://leetcode.com/problems/time-based-key-value-store/
#  981. Time Based Key-Value Store
# Medium
# Topics
# Companies
# Design a time-based key-value data structure that can store multiple values for the same key at different time stamps 
# and retrieve the key's value at a certain timestamp.

# Implement the TimeMap class:

# TimeMap() Initializes the object of the data structure.
# void set(String key, String value, int timestamp) Stores the key key with the value value at the given time timestamp.
# String get(String key, int timestamp) Returns a value such that set was called previously, with timestamp_prev <= timestamp. If there are multiple such values, it returns the value associated with the largest timestamp_prev. If there are no values, it returns "".
 

# Example 1:
# Input
# ["TimeMap", "set", "get", "get", "set", "get", "get"]
# [[], ["foo", "bar", 1], ["foo", 1], ["foo", 3], ["foo", "bar2", 4], ["foo", 4], ["foo", 5]]
# Output
# [null, null, "bar", "bar", null, "bar2", "bar2"]

# Explanation
# TimeMap timeMap = new TimeMap();
# timeMap.set("foo", "bar", 1);  // store the key "foo" and value "bar" along with timestamp = 1.
# timeMap.get("foo", 1);         // return "bar"
# timeMap.get("foo", 3);         // return "bar", since there is no value corresponding to foo at timestamp 3 and timestamp 2, then the only value is at timestamp 1 is "bar".
# timeMap.set("foo", "bar2", 4); // store the key "foo" and value "bar2" along with timestamp = 4.
# timeMap.get("foo", 4);         // return "bar2"
# timeMap.get("foo", 5);         // return "bar2"
 

# Constraints:
# 1 <= key.length, value.length <= 100
# key and value consist of lowercase English letters and digits.
# 1 <= timestamp <= 107
# All the timestamps timestamp of set are strictly increasing.
# At most 2 * 105 calls will be made to set and get.

import collections


class TimeMap:
    def __init__(self):
        # Initialize two dictionaries to store values and timestamps
        self.value_dict = collections.defaultdict(list)
        self.time_dict = collections.defaultdict(list)
        

    def set(self, key: str, value: str, timestamp: int) -> None:
        # Append the value and its corresponding timestamp to the respective lists for the given key
        self.value_dict[key].append(value)
        self.time_dict[key].append(timestamp)
        

    def get(self, key: str, timestamp: int) -> str:
        # Binary search to find the value corresponding to the given timestamp for the key
        l = 0
        r = len(self.time_dict.get(key, [])) - 1

        while l <= r:
            mid = l + (r - l) // 2

            if self.time_dict[key][mid] == timestamp:
                # If exact timestamp is found, return the corresponding value
                return self.value_dict[key][mid]
            elif self.time_dict[key][mid] > timestamp:
                # If mid timestamp is greater, search in the left half
                r = mid - 1
            else:
                # If mid timestamp is less, search in the right half
                l = mid + 1

        # If no exact match, return the closest previous value or empty string if none exists
        return self.value_dict[key][r] if r >= 0 else ""

# Time Complexity:
# - set: O(1) for each set operation, as appending to a list is an O(1) operation.
# - get: O(log T) where T is the number of timestamps associated with a key.
#        This complexity arises because the function performs a binary search over the timestamps.
        


# Your TimeMap object will be instantiated and called as such:
# obj = TimeMap()
# obj.set(key,value,timestamp)
# param_2 = obj.get(key,timestamp)
    
# Testing:
instance = TimeMap()
input = ["TimeMap", "set", "get", "get", "set", "get", "get"]
params = [[], ["foo", "bar", 1], ["foo", 1], ["foo", 3], ["foo", "bar2", 4], ["foo", 4], ["foo", 5]]
for i in range(len(input)):
    if input[i] == "set":
        print("put:",instance.set(params[i][0], params[i][1], params[i][2]))
    if input[i] == "get":
        print("get: ", instance.get(params[i][0], params[i][1]))
# Output
# [null, null, "bar", "bar", null, "bar2", "bar2"]
