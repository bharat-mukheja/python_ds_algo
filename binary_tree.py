from tree import Tree

class BinaryTree(Tree):
    """Abstract base class representing a binary tree structure."""

    # Abstract methods additional
    def left(self,p):
        """Return a Position representing p's left child.
        Return None if p doesn't have a left child."""
        raise NotImplementedError('must be implemented by subclass')

    def right(self, p):
        """Return a Position representing p's right child.
        Return None if p doesn't have a right child."""
        raise NotImplementedError('must be implemented by subclass')

    # Concrete methods of this class
    def sibling(self,p):
        """Returns a Position representing p's sibling (or None if no sibling)."""
        parent = self.parent(p)
        if parent is None:                  # p is root
            return None
        elif p == self.left(parent):
            return self.right(parent)       # possibly None
        else:
            return self.left(parent)        # possibly None

    def children(self, p):
        """Generate an iteration of Positions representing p's children."""
        if self.left(p) is not None:
            yield self.left(p)
        if self.right(p) is not None:
            yield self.right(p)

