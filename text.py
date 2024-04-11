def chuncker(text, font):
    chunks = text.split(" ")
    curr_line = ""
    lines = []
    i = 0

    space_w = font.getsize(" ")

    for i in range(len(chunks)):
        if (font.getsize(curr_line) + space_w + font.getsize(chunks[i])) < 122:
            curr_line = f"{curr_line} {chunks[i]}"
        else:
            curr_line = curr_line.strip()
            lines.append(curr_line)
            curr_line = chunks[i]

    lines.append(curr_line)
    return lines


class Font:
    def getsize(self, text):
        return len(text)

font = Font()
print(chuncker("Lorem ipsum dolor sit amet, consetetur sadipscing elitr, sed diam nonumy eirmod tempor invidunt ut labore et dolore magna aliquyam erat, sed diam voluptua. At vero eos et accusam et justo duo dolores et ea rebum. Stet clita kasd gubergren, no sea takimata sanctus est Lorem ipsum dolor sit amet. Lorem ipsum dolor sit amet, consetetur sadipscing elitr, sed diam nonumy eirmod tempor invidunt ut labore et dolore magna aliquyam erat, sed diam voluptua. At vero eos et accusam et justo duo dolores et ea rebum. Stet clita kasd gubergren, no sea takimata sanctus est Lorem ipsum dolor sit amet.", font))
