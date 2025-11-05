import sys


def run_length_encoding(input_str: str) -> str:
    result = []
    # store the current character
    cur_char = input_str[0]
    # store the count of the current character
    count = 1

    # loop starts from second character until the end of input string
    for i in range(1, len(input_str)):
        # until the characters found are same as the current character increase count
        if input_str[i] == cur_char:
            count += 1
        # if a new character is found which is not the current character
        # append the character and it's count and change the current character as the new character
        else:
            result.append(f"{cur_char},{count};")
            cur_char = input_str[i]
            count = 1
    # appending the last character and it's count after the loop ends
    result.append(f"{cur_char},{count}")
    return "".join(result)


if __name__ == "__main__":
    # read from STDIN
    input_string = sys.stdin.read().strip()

    # perform run length encoding
    output = run_length_encoding(input_string)
    # print output
    print(output)


# runnable with the command
# echo "AAAAABBBBCCCCAA" | python run_length_encoding.py
