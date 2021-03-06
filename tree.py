class BSTree:

        
        #
        # Constructor
        #

        def __init__(self, content=None):
                """
                Initialize the tree with a valid value(can't be None).
                """
                if not content:
                        self.content = 0
                else:
                        self.content = content
                
                self.lnode = None
                self.rnode = None

        #
        # Operators Overloading
        #

        def __str__(self):
                return str(self.content)
        
        
        def __add__(self, x):
                if type(x) is not type(self):
                        return (self.content + x)
                else: 
                        return (self.content + x.content)                                       

                        
        def __sub__(self, x):
                if type(x) is not type(self):
                        return (self.content - x)
                else:
                        return (self.content - x.content)                                       

                        
        def __mul__(self, x):
                if type(x) is not type(self):
                        return (self.content * x)
                else:
                        return (self.content * x.content)                                       

                        
        def __div__(self, x):
                if type(x) is not type(self):
                        return (self.content / x)
                else:
                        return (self.content / x.content)                               

        #
        # Methods
        #

        def add(self, content=None):
                """
                Add an element to the tree. In the right if the value if is bigger than the
                actual, and in the left if its less than the actual.
                """
                if not content:
                        return -1

                if content > self.content:
                        if self.rnode:
                                self.rnode.add(content)
                        else:
                                self.rnode = BSTree(content)

                if content <= self.content:
                        if self.lnode:
                                self.lnode.add(content)
                        else: 
                                self.lnode = BSTree(content)

                                
        def view(self, level=1):
                """
                Print the tree on the screen.
                """
                arrow = "---" * level
                print ("|%s>%s" % (arrow, self.content))

                if self.rnode:
                        self.rnode.view(level+1)
                if self.lnode:
                        self.lnode.view(level+1)

                return

                
        def size(self):
                """
                Returns the size of the tree.
                """
                tsize = 1

                if self.rnode:
                        tsize += self.rnode.size()
                if self.lnode:
                        tsize += self.lnode.size()

                return tsize

                
        def min(self):
                """
                Returns the minimum value of the tree.
                """
                while (self.lnode):
                        self = self.lnode
                
                return self.content

                
        def max(self):
                """
                Returns the maximum value of the tree.
                """
                while (self.rnode):
                        self = self.rnode
                
                return self.content

                
        def search(self, element=None):
                """
                Returns the level of the element on the tree.
                """
                if not element: return -1

                while (1):
                        if not self:
                                return -1
                        if (not self.lnode) and (not self.rnode):
                                return -1

                        if self.content == element:
                                return self
                        
                        self = (self.lnode, self.rnode)[self.content <= element]

                        
        def delete(self, element=None):
                """
                Delete an element of the tree.
                """
                if not element: return -1

                if self.search(element):
                        while (1):
                                if not self:
                                        return None
                                if (not self.lnode) and (not self.rnode):
                                        return None
        
                                if self.lnode and self.lnode.content == element:
                                        break
                                if self.rnode and self.rnode.content == element:
                                        break
                                
                                self = (self.lnode, self.rnode)[self.content <= element]

                        if self.rnode and self.rnode.content == element: 
                                del self.rnode
                                self.rnode = 0
                        
                        if self.lnode and self.lnode.content == element:
                                del self.lnode
                                self.lnode = 0
                        
                        return element

                        
        def height(self):
                """
                Returns the height of the tree.
                """
                ltmp, rtmp = 0, 0
                if not self:
                        return 0
                if self.lnode:
                        ltmp = self.lnode.height()
                if self.rnode:
                        rtmp = self.rnode.height()
                return ( 1 + max(ltmp, rtmp))