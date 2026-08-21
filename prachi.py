class Node:
    def __init__(self, name, node_type):
        self.name = name
        self.node_type = node_type
        self.parent = None
        self.children = []

    def add_child(self, child):
        child.parent = self
        self.children.append(child)


class DirectoryTree:
    def __init__(self):
        self.root = Node("Root", "folder")

    def create_folder(self, parent, name):
        folder = Node(name, "folder")
        parent.add_child(folder)
        return folder

