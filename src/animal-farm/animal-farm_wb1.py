# Animal Farm workbook data for the shared builder (book_build.py).
# The novel is not public domain in the US, so there is no reader: each chapter starts with an original summary instead.
import os, sys, io, contextlib
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
with contextlib.redirect_stdout(io.StringIO()):
    import build_all as _B
WB, CHMETA = {}, {}
for ch in _B.CHAPTERS:
    n = ch["num"]
    WB[n] = dict(vocab=[(w, w, pos, st, ipa, ko, col, ex1, ex2) for (w, pos, st, ipa, ko, col, ctx, ex1, ex2) in ch["vocab"]],
                 quiz=list(ch["quiz"]), discussion=list(ch["discussion"]))
    CHMETA[n] = dict(name=ch["title"], summary=ch["summary"], characters=ch["characters"])
