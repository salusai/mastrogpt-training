import sys
sys.path.append("packages/rag/rag")
import rag, vdb

def test_parse_query():
    query = "Hello"
    rag.parse_query(query)

    query = "Hello@"
    rag.parse_query(query)

    query = "@M"
    rag.parse_query(query)

    query = "@M Hello"
    rag.parse_query(query)

    query = "@D20 Hello"
    rag.parse_query(query)

    query = "@D20bit Hello"
    rag.parse_query(query)

    query = "@Pbit Hello"
    rag.parse_query(query)

    query = "@test"
    rag.parse_query(query)


def test_vdb():
    args = {}
    db = vdb.VectorDB(args, "hello")
    db.insert("this is a test")
    db.insert("another test")

    db = vdb.VectorDB(args, "h", shorten=True)
    db.collection
    db.vector_search("test")


def test_rag():
    args = {}
    rag.rag(args)
    
    args = {"input": "@M"}
    rag.rag(args)

    inp = "@P20h"
    rag.parse_query(inp)
    args = {"input": inp}
    rag.rag(args)


    inp = "@Ltest test@"
    rag.parse_query(inp)
    args = {"input": inp}
    rag.rag(args)
    
    inp = "@Ltest what is a test?"
    opt = rag.parse_query(inp)
    rag.parse_query(inp)
    args = {"input": inp}
    rag.rag(args)

    inp = "who are you?@"
    opt = rag.parse_query(inp)
    args = {"input": inp}
    rag.rag(args)


