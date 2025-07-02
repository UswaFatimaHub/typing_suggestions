from app.core.config import collection

def get_all_docs():
    cursor = collection.find({}, {
        "title": 1,
        "summary": 1,
        "answer": 1,
        "tags": 1,
        "_id": 0
    }).limit(1000)

    return list(cursor)
    # return list(collection.find())
