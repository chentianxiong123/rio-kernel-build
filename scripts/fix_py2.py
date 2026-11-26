#!/usr/bin/env python3
p = "scripts/gcc-wrapper.py"
lines = open(p).read().split("\n")
out = []
for ln in lines:
    stripped = ln.lstrip()
    indent = ln[:len(ln)-len(stripped)]
    if stripped.startswith("print ") and not stripped.startswith("print("):
        body = stripped[len("print "):]
        # py2 print with trailing comma => end=" "
        if body.rstrip().endswith(","):
            body = body.rstrip()[:-1].rstrip()
            out.append(indent + "print(" + body + ", end=\" \")")
        else:
            out.append(indent + "print(" + body + ")")
    else:
        out.append(ln)
open(p, "w").write("\n".join(out))
print("fixed py2 prints")
