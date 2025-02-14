import sys
sys.path.append("packages/form/puzzle")
import puzzle

def test_chess():
    fen = "rnbqkbnr/pppppppp/8/8/8/8/PPPPPPPP/RNBQKBNR"
    assert puzzle.extract_fen(fen) == fen

    out = f"hello {fen} world"
    assert puzzle.extract_fen(out) == fen
