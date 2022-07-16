"""

Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.

An input string is valid if:

Open brackets must be closed by the same type of brackets.
Open brackets must be closed in the correct order.



Example 1:

Input: s = "()"
Output: true
Example 2:

Input: s = "()[]{}"
Output: true
Example 3:

Input: s = "(]"
Output: false

Constraints:

1 <= s.length <= 104
s consists of parentheses only '()[]{}'.
"""

class ValidParenthesis:


    def is_valid_parenthesis(self, string):

        parenthesis_lookup = {
            ")":"(",
            "}":"{",
            "]":"[",
        }

        stack_store = []

        for i in string:
            if i in parenthesis_lookup:
                if stack_store and parenthesis_lookup[i] == stack_store[-1]:
                    stack_store.pop()
                else:
                    return False
            else:
                stack_store.append(i)
        return False if stack_store else True


list_of_test_strings = [ "()){}{{}", "(){}[]", "[", "]", "[()]", "()", "()[]{}", "(]" ]

valid_parenthesis = ValidParenthesis()

for i in list_of_test_strings:
    print(valid_parenthesis.is_valid_parenthesis(i))