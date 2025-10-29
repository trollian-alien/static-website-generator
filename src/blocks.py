from enum import Enum

class BlockType(Enum):
    PARAGRAPH = "paragraph"
    HEADING = "heading"
    CODE = "code"
    QUOTE = "quote"
    UNORDERED_LIST = "unordered list"
    ORDERED_LIST = "ordered list"

def markdown_to_blocks(markdown):
    blocks = markdown.split("\n\n")
    return [block.strip() for block in blocks if block != ""]

def is_heading(block):
    i = 0
    while i < len(block) and block[i] == '#':
        i += 1
    return 1 <= i <= 6 and i < len(block) and block[i] == ' '

def block_to_block_type(block):
    if is_heading(block):
        return BlockType.HEADING
    elif block.startswith("```") and block.endswith("```"):
        return BlockType.CODE
    lines = block.split("\n")
    if False not in [line.startswith(">") for line in lines]:
        return BlockType.QUOTE
    elif False not in [line.startswith("-") for line in block.split("\n")]:
        return BlockType.UNORDERED_LIST
    elif False not in [lines[i].startswith(f"{i+1}.") for i in range(0,len(lines))]:
        return BlockType.ORDERED_LIST
    else:
        return BlockType.PARAGRAPH