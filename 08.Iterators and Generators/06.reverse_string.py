def reverse_text(text):
    index = -1

    while index >= -len(text):
        yield text[index]
        index -= 1
#     ili:
#     index = len(text) - 1
#     while index > -1:
#         yield text[index]
#         index -= 1


for char in reverse_text("step"):
    print(char, end='')
