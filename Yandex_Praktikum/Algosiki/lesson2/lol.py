def solution(node):
    while node.next is not None:
        node.prev, node.next = node.next, node.prev
        node = node.prev
    node.prev, node.next = node.next, node.prev
    return node
