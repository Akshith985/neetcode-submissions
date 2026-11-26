class Solution:
    def decodeString(self, s: str) -> str:
        stack: list[tuple[str, int]] = []
        curr_str = ""
        curr_num = 0

        for ch in s:
            if ch.isdigit():
                curr_num = curr_num * 10 + int(ch)
            elif ch == "[":
                stack.append((curr_str, curr_num))
                curr_str = ""
                curr_num = 0
            elif ch == "]":
                prev_str, repeat_count = stack.pop()
                curr_str = prev_str + curr_str * repeat_count
            else:
                curr_str += ch

        return curr_str