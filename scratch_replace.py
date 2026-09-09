import re
with open("script.js", "r", encoding="utf-8") as f:
    code = f.read()
code = re.sub(r'<div class="navbrand">.*?</div>', '<div class="navbrand"><span>Categories</span></div>', code)
with open("script.js", "w", encoding="utf-8") as f:
    f.write(code)
