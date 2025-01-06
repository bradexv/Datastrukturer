class Node:
        
    def __init__(self, element):
        self._element = element;
        #self._parent = None; trenger ikke parent pga går bare nedvoer i treet
        self._right = None;
        self._left = None;

    def __str__(self):
        return str(self._element);


class Set:
   
    def __init__(self):
        self._root = None;
        self._length = 0;
    
    #hjelpemetode
    def getRoot(self):
        return self._root;
        
    def search(self, v, x):
        if (v is None):
            return None;

        if (v._element == x):
            return v;

        if (x < v._element):
            return self.search(v._left, x);

        if (x > v._element):
            return self.search(v._right, x);

    def contains(self, x):
        resultat = self.search(self._root, x);
        if resultat:
            return True;
        else:
            return False;



    def insertP(self, v, x):
        if (v is None):
            v = Node(x);

        elif (x < v._element):
            #print("gaar inn i venstre");
            v._left = self.insertP(v._left, x);

        elif (x > v._element):
            #print("gaar inn i hoyre");
            v._right = self.insertP(v._right, x);

        return v;

    def insert(self, x): #x er elementet som skal settes inn
        #edge case:
        if (self._root is None):
            self._root = Node(x);
            self._length = self._length + 1;
        
        #legger til en ekstra condition pga skal ikke gaa an aa sette inn et element som allerede er i treet
        elif (self.contains(x)):
            return None;
        
        else:
            result = self.insertP(self._root, x);
            if result:
                self._length = self._length + 1;
    


    def size(self):
        return self._length;


    #en metode brukt bare for aa sjekke at alle elementene har kommet med i treet
    def printAllHelper(self, v):
        if (v is None):
            return;
        print(v);
        self.printAllHelper(v._left);
        self.printAllHelper(v._right);

    def printAll(self):
        print("Kjorer printAll fra roten. Roten er: " + str(self._root));
        self.printAllHelper(self._root);
    
    
    
    def findMin(self):
        currentMin = self._root;
        currentNode = self._root;
    
        while (currentNode is not None):
            if (currentNode._element < currentMin._element):
                currentMin = currentNode;
            currentNode = currentNode._left;
    
        return currentMin;

    #ekstrametode bare brukt i testing
    def findMax(self): #ekstrametode
        currentMax = self._root;
        currentNode = self._root;
    
        while (currentNode is not None):
            if (currentNode._element > currentMax._element):
                currentMax = currentNode;
            currentNode = currentNode._right;
    
        return currentMax;

    def findMinFromV(self, v):
        currentMin = v;
        currentNode = v;
    
        while (currentNode is not None):
            if (currentNode._element < currentMin._element):
                currentMin = currentNode;
            currentNode = currentNode._left;
    
        return currentMin;
        
    #naar fjerner en node: erstatte node med minste i høyre subtre
    def remove(self, x):
        self._root = self.removeP(self._root, x); #pga denne oppdateres bare dersom roten faktisk endres

        self._length = self._length - 1;

    def removeP(self, v, x): 
        if (v is None):
            #print("v er tom.");
            return None;

        if (x < v._element):
            v._left = self.removeP(v._left, x);
            return v;

        if (x > v._element):
            v._right = self.removeP(v._right, x);
            return v;

        if (v._left is None):
            return v._right;

        if (v._right is None):
            return v._left;

        u = self.findMinFromV(v._right);
        v._element = u._element;
        v._right = self.removeP(v._right, u._element);

        return v;

        
        
    