#!/usr/bin/env python3
p = "scripts/gcc-wrapper.py"
lines = open(p).read().split("\n")
out = []
for ln in lines:
    stripped = ln.lstrip()
    indent = ln[:len(ln)-len(stripped)]
    if stripped.startswith("print ") and not stripped.startswith("print("):
        body = stripped[len("print "):]
        if body.rstrip().endswith(","):
            body = body.rstrip()[:-1].rstrip()
            out.append(indent + "print(" + body + ", end=\" \")")
        else:
            out.append(indent + "print(" + body + ")")
    else:
        out.append(ln)
t = "\n".join(out)
# py3: bytes line rstrip with str arg fails -> use no-arg rstrip
t = t.replace("line.rstrip(chr(10))", "line.rstrip()")
t = t.replace("line.rstrip(" + repr(chr(10)) + ")", "line.rstrip()")
open(p, "w").write(t)
print("fixed py2 prints + bytes")
