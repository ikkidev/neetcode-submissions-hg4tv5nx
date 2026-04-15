class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        # Keep map of closing bracket characters
        close_map = { ")" : "(", "]" : "[", "}" : "{" }

        for c in s:
            # If c is a closing bracket. Check if we have a corresponding
            # open bracket in the map

            if c in close_map:
                if stack and stack[-1] == close_map[c]:
                    stack.pop()
                # if stack is empty or we don't find a corresponding open
                # the string is invalid
                else:
                    return False
            # Append closing bracket to the stack
            else:
                stack.append(c)

        #If stack is not empty we know there's a leftover bracket somewhere
        return False if stack else True