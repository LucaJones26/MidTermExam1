def count_pattern_occurrences(text):
    count = 0
    start_index = 0

    while start_index < len(text):

        start_index = text.find('b', start_index)

        if start_index == -1:
            break


        for end_index in range(start_index + 3, len(text) + 1):
            if text[end_index - 3:end_index] == "Bob":  # Check if last 3 letters are 'Bob'
                count += 1  # Found a valid pattern
                break  # Move to the next 'b'

        start_index += 1

    return count


# Example usage
text = "bababababBob bxyzBob bHelloWorldBob"
print(count_pattern_occurrences(text))
