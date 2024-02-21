def decode(message_file):
    codes = {}

    with open(message_file) as encoded_message:
        for code in encoded_message:
            number, word = code.split()
            number = int(number)
            codes[number] = word

    step = 1
    subsets = []
    decoded_message = ""

    nums = list(range(len(codes)))  # Create a list of numbers from 0 to len(codes) - 1

    while len(nums) != 0:
        if len(nums) >= step:
            subsets.append(nums[0:step])
            nums = nums[step:]
            step += 1
        else:
            return decoded_message

    for subset in subsets:
        end_value = subset[-1] + 1  # Take the end value of each range
        if end_value in codes:
            decoded_message += f"{codes[end_value]} "

    return decoded_message


decoded_message = decode("coding_qual_input.txt")
print(decoded_message)
