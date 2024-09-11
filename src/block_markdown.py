def markdown_to_blocks(markdown: str) -> list:
    list_of_blocks = markdown.split("\n\n")
    list_of_blocks = filter(lambda x: x != "", list_of_blocks)
    list_of_blocks = list(map(lambda x: x.strip(), list_of_blocks))
    return list_of_blocks