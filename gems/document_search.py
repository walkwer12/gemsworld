#How Divide and Conquer can be applied in a search engine–like scenario

documents = ["RM", "Big Data", "AI", "ML", "Python", "Java", "C++", "JavaScript"]
#need to sort the list
documents.sort()

def binary_search(documents, keyword, low, high):
    if low > high:
        return -1

    mid = (low + high) // 2

    if documents[mid].lower() == keyword.lower():
        return mid
    elif documents[mid].lower() < keyword.lower():
        return binary_search(documents, keyword, mid + 1, high)
    else:
        return binary_search(documents, keyword, low, mid - 1)

result = binary_search(documents, "RM", 0, len(documents) - 1)
if result != -1:
    print(f"Document found at index: {result + 1}")
    print(f"Result: {documents[result]}")
else:
    print("Document not found")