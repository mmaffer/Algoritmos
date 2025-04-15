import re

class HTMLTagChecker:
    def __init__(self, html_content):
        self.html = html_content
        self.stack = []
        self.tag_pattern = re.compile(r'</?([a-zA-Z0-9]+)>')

    def get_tags(self):
        """Extract all tags from the HTML content."""
        return list(self.tag_pattern.finditer(self.html))

    def is_opening_tag(self, tag):
        """Check if a tag is an opening tag."""
        return not tag.startswith('</')

    def get_tag_name(self, tag_match):
        """Extract tag name from a match object."""
        return tag_match.group(1)

    def process_tag(self, tag_match):
        """Process a tag: push if opening, pop if closing."""
        tag = tag_match.group()
        tag_name = self.get_tag_name(tag_match)

        if self.is_opening_tag(tag):
            self.stack.append(tag_name)
        else:
            if not self.stack or self.stack[-1] != tag_name:
                return False
            self.stack.pop()
        return True

    def is_balanced(self):
        """Check if all HTML tags are balanced."""
        for tag_match in self.get_tags():
            if not self.process_tag(tag_match):
                return False
        return len(self.stack) == 0


# Test 1
html1 = "<html><body><h1>Hello</h1></body></html>"
checker1 = HTMLTagChecker(html1)
print(checker1.is_balanced())  # True

# Test 2
html2 = "<div><p>Oops</div></p>"
checker2 = HTMLTagChecker(html2)
print(checker2.is_balanced())  # False

# Test 3
html3 = "<a><b></b><c></c></a>"
checker3 = HTMLTagChecker(html3)
print(checker3.is_balanced())  # True