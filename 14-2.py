class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None


class DoublyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        self.delete_stack = []  # (prev_node, deleted_node, next_node) 저장

    def append(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            self.tail = new_node
        else:
            new_node.prev = self.tail
            self.tail.next = new_node
            self.tail = new_node
        return new_node  # 노드 참조 반환

    def delete(self, node):
        """노드 객체를 직접 받아서 삭제 (O(1))"""
        prev_node = node.prev
        next_node = node.next

        self.delete_stack.append((prev_node, node, next_node))

        if prev_node:
            prev_node.next = next_node
        else:
            self.head = next_node  # head 삭제

        if next_node:
            next_node.prev = prev_node
        else:
            self.tail = prev_node  # tail 삭제

        # 삭제 후 커서 이동: 다음 노드 우선, 없으면 이전 노드
        return next_node if next_node else prev_node

    def undo_delete(self):
        """가장 최근 삭제를 복원 (O(1))"""
        if not self.delete_stack:
            return

        prev_node, node, next_node = self.delete_stack.pop()

        node.prev = prev_node
        node.next = next_node

        if prev_node:
            prev_node.next = node
        else:
            self.head = node  # head 복원

        if next_node:
            next_node.prev = node
        else:
            self.tail = node  # tail 복원


def solution(n, k, cmd):
    dll = DoublyLinkedList()

    # 노드 생성 및 리스트 구성, 인덱스로 바로 접근하기 위해 배열에도 저장
    nodes = [dll.append(i) for i in range(n)]

    cursor = nodes[k]  # 현재 커서 노드

    for command in cmd:
        if command[0] == 'U':
            count = int(command.split()[1])
            for _ in range(count):
                cursor = cursor.prev

        elif command[0] == 'D':
            count = int(command.split()[1])
            for _ in range(count):
                cursor = cursor.next

        elif command[0] == 'C':
            cursor = dll.delete(cursor)  # 삭제 후 커서 자동 이동

        elif command[0] == 'Z':
            dll.undo_delete()  # 복원 (커서는 이동 안 함)

    # 결과 조합: delete_stack에 남은 노드들은 'X', 나머지는 'O'
    deleted = {node.data for _, node, _ in dll.delete_stack}
    return "".join('X' if i in deleted else 'O' for i in range(n))