
# .. Massimo Donelli, October 2024, V1.0 ..
from random import *
NULL_THRESHOLD = 1.0e-6
class matrix():
    def __init__(self,rows,columns) -> None:
        self.rows = rows
        self.columns = columns
        self.Elements= []
        self.Zeros()    
    def __str__(self) -> str:
        return ('Matrix(' + str(self.rows)+ "," + str(self.columns) + ")")
    # .. Print the matrix ..
    def Show(self):
        for I_X_FOR in range(self.rows):    
            print("|",end="\t")
            for J_X_FOR in range(self.columns):     
                print(self.Elements[I_X_FOR][J_X_FOR],end="\t")
            print("| \n")    
    # .. Create a matrix of zeros ..
    def Zeros(self):
        Dummy_Elements= []
        for I_X_FOR in range(self.rows):
            Dummy_Elements.append([])
        #  
        for J_X_FOR in range(self.rows):
            for I_X_FOR in range(self.columns):
                Dummy_Elements[J_X_FOR].append(0)
        self.Elements=Dummy_Elements
# .. Create a matrix of scalar ..
    def Scalar(self,alpha):
        Dummy_Elements= []
        for I_X_FOR in range(self.rows):
            Dummy_Elements.append([])
        #  
        for J_X_FOR in range(self.rows):
            for I_X_FOR in range(self.columns):
                Dummy_Elements[J_X_FOR].append(alpha)
        self.Elements=Dummy_Elements
    # .. Create a matrix of random scalar ..
    def Random(self,minvalue,maxvalue):
        #  
        for J_X_FOR in range(self.rows):
            for I_X_FOR in range(self.columns):
                self.Elements[I_X_FOR][J_X_FOR]=randint(minvalue,maxvalue)
        return(self)
    # .. Create an identity matrix  ..
    def Identity(self):
        if(self.rows == self.columns):
            Dummy_Elements= []
            for I_X_FOR in range(self.rows):
                Dummy_Elements.append([])
        #    
            for J_X_FOR in range(self.columns):
                for I_X_FOR in range(self.rows): 
                    if(J_X_FOR==I_X_FOR):
                        Dummy_Elements[J_X_FOR].append(1)
                    else:    
                        Dummy_Elements[J_X_FOR].append(0)
            self.Elements=Dummy_Elements
        else:
            print("Error: the matrix must be square")  
            return(-1) 
    # .. Set element Mij in the matrix ..   
    def put(self,row,coloumn,Aij):
        if((row > self.rows) or (coloumn > self.columns) or (row<0) or (coloumn<0)):
            print("Error: wrong index")  
            return(-1)
        else:
            self.Elements[row][coloumn]=Aij
    # .. Retrieve element Mij in the matrix ..   
    def get(self,row,coloumn):
        if((row > self.rows) or (coloumn > self.columns) or (row<0) or (coloumn<0)):
            print("Error: wrong index")  
            return(-1)
        else:
            return(self.Elements[row][coloumn])   
    # .. Multiply a matrix for a scalar ..
    def MultForScalar(self,Alpha):
        #
        for J_X_FOR in range(self.rows):      
            for I_X_FOR in range(self.columns):
                self.Elements[J_X_FOR-1][I_X_FOR-1]*=Alpha             
    # .. Elementary operation 1) swap two rows ..
    def SwapRows(self,i,j):
        if((i >self.rows) or (j >self.columns) or (i<0) or (j<0) or (i==j)):
            print("Error: wrong index")  
            return(-1)
        else:
            Dummy_Elements= []
            # .. Copy the row i ..
            for J_X_FOR in range(self.columns):
                Dummy_Elements.append(self.Elements[i][J_X_FOR])
            # .. Copy row j into row i ..    
            for J_X_FOR in range(self.columns):
                self.Elements[i][J_X_FOR]=self.Elements[j][J_X_FOR]
                self.Elements[j][J_X_FOR]= Dummy_Elements[J_X_FOR]
    # .. Elementary operation 2) multiply for a rows for scalar ..
    def RowsForScalar(self,i,Alpha):
        if((i >self.rows) or (i<0) or (Alpha == 0)):
            print("Error: wrong index")  
            return(-1)
        else:
            # .. Multiply row i for Alpha ..    
            for J_X_FOR in range(self.columns):
                self.Elements[i][J_X_FOR]=self.Elements[i][J_X_FOR]*Alpha   
    # .. Elementary operation 3) sum two rows i,j and the second multiplied for a scalar ..
    def SumRowsForScalar(self,i,j,Alpha):
        if((i >self.rows) or (j >self.columns) or (i<0) or (j<0)):
            print("Error: wrong index")  
            return(-1)
        elif(i==j):
            # .. do nothing ..  
            return(-1)
        else:
            for J_X_FOR in range(self.columns):
                self.Elements[i][J_X_FOR]=self.Elements[i][J_X_FOR] + Alpha*self.Elements[j][J_X_FOR]
                #self.Elements[j][J_X_FOR]=self.Elements[j][J_X_FOR] + Alpha*self.Elements[i][J_X_FOR]
     # .. Transpose the matrix ..
    def Trans(self):
        Dummy = matrix(self.columns,self.rows)
        Dummy.Zeros()
        #
        for J_X_FOR in range(self.rows):
            for I_X_FOR in range(self.columns): 
                Dummy.Elements[I_X_FOR-1][J_X_FOR-1] = self.Elements[J_X_FOR-1][I_X_FOR-1]
        # .. Save the transpose ..         
        self.rows = Dummy.rows
        self.columns = Dummy.columns
        self.Elements = Dummy.Elements    
 # .. Extract coloumn ..
    def ExtractColoumn(self,row,coloumn):
        DummyColoumns = []
        for I_X_FOR in range(row,self.rows): 
               DummyColoumns.append(self.Elements[I_X_FOR][coloumn]) 
        pivot = max(DummyColoumns)
        index_pivot = DummyColoumns.index(pivot)+row
        return pivot,index_pivot
 # .. Apply the Gauss Method to solve linear systems of equations [A]x=[B] ..
    def Gauss(self):
        Echelon = self
        SWAP_NUMBER = 0 # .. Useful for the Det estimation ..
        INDEX_ROW = 0
        INDEX_COL = 0
        if(self.rows==self.columns):
            # .. if the matrix is square ..
            SUB_COL = 1
        else:
            # .. if the matrix is rectangular ..
            SUB_COL = 2
        # .. Iteration .. 
        for J_X_FOR in range(INDEX_COL,Echelon.columns-SUB_COL):
            # .. Find the maximum pivot to reduce the approximation error ..
            pivot,index_pivot = Echelon.ExtractColoumn(INDEX_ROW,INDEX_COL)  
            # .. Swap the row ..
            if(INDEX_ROW!=index_pivot):
              Echelon.SwapRows(INDEX_ROW,index_pivot)
              SWAP_NUMBER += 1
            for I_X_FOR in range(INDEX_ROW+1,Echelon.rows):
                if(pivot !=0):
                    Echelon.SumRowsForScalar(I_X_FOR,INDEX_ROW,(-Echelon.Elements[I_X_FOR][J_X_FOR]/pivot))    
            INDEX_ROW += 1
            INDEX_COL += 1      
        if (SWAP_NUMBER % 2 == 0):
            DET_ALPHA = 1
        else:
            DET_ALPHA = -1              
        # .. Return the reduced matrix echelon ..         
        return(DET_ALPHA,Echelon)
 # .. Apply the Gauss-Jordan Method to solve linear systems of equations [A]x=[B] ..
    def GaussJordan(self):        
        DUMMY_MATRIX = self   
        # .. Perform the Gauss elimination in order to obtain a lower diagonal matrix ..    
        DUMMY_MATRIX.Gauss()
        INDEX_ROW = DUMMY_MATRIX.rows-1  
        if(self.rows==self.columns):
            # .. if the matrix is square ..
            SUB_COL = 1
        else:
            # .. if the matrix is rectangular ..
            SUB_COL = 2  
        # .. Iteration .. 
        for J_X_FOR in range(DUMMY_MATRIX.columns-SUB_COL,0,-1):
            pivot = DUMMY_MATRIX.Elements[J_X_FOR][J_X_FOR]
            for I_X_FOR in range(DUMMY_MATRIX.rows-1,-1,-1):
                if(pivot !=0):
                    DUMMY_MATRIX.SumRowsForScalar(I_X_FOR,INDEX_ROW,(-DUMMY_MATRIX.Elements[I_X_FOR][J_X_FOR]/pivot)) 
            INDEX_ROW -= 1
    # .. Estimate the Det of a square matrix ..
    def Det(self):
         det = 1
         if(self.rows!=self.columns):
            # .. if the matrix is not square ..
            print("Error the matrix is not square")
            return(-1)
         #
         if(self.rows==2):
             # .. It is a 2x2 matrix ..
             det = (self.Elements[0][0]*self.Elements[1][1])-(self.Elements[0][1]*self.Elements[1][0])
         elif(self.rows == 3):
             # .. It is a 3x3 matrix with Sarrus..
             det = (self.Elements[0][0]*self.Elements[1][1]*self.Elements[2][2])+(self.Elements[0][1]*self.Elements[1][2]*self.Elements[2][0]) + (self.Elements[0][2]*self.Elements[1][0]*self.Elements[2][1]) - (self.Elements[2][0]*self.Elements[1][1]*self.Elements[0][2]) - (self.Elements[2][1]*self.Elements[1][2]*self.Elements[0][0]) - (self.Elements[2][2]*self.Elements[1][0]*self.Elements[0][1])
         elif(self.rows > 3):   
             DET_ALPHA,Echelon = self.Gauss()
             # .. It is a 4x4 or greater square matrix ..
             for I_X_FOR in range(self.rows):
                det *= Echelon.Elements[I_X_FOR][I_X_FOR] 
             det *= DET_ALPHA      
         return(det)
# .. Estract a submatrix from A ..
    def SubExt(self,Ri,Rf,Ci,Cf):
        SubMatrix=matrix((Rf-Ri)+1,(Cf-Ci)+1)
        Rsub=0
        for I_X_FOR in range(Ri,Rf+1,1):
            Csub=0
            for J_X_FOR in range(Ci,Cf+1,1):
                SubMatrix.Elements[Rsub][Csub] = self.Elements[I_X_FOR][J_X_FOR]
                Csub+=1
            Rsub+=1    
        return(SubMatrix)
    # .. Estimates the inverse of the matrix ..
    def Inv(self):
        if(self.Det() == 0):
            print("Null Matrix Determinant the matrix cannot be inverted")
            return(-1)
        elif(self.rows!=self.columns):
            print("The Matrix is not square cannot calculate the determinant")
            return(-1)
        DUMMY = matrix(self.rows,self.columns)
        for I_X_FOR in range(self.rows):
           for J_X_FOR in range(self.columns):
                 DUMMY.Elements[I_X_FOR][J_X_FOR]=self.Elements[I_X_FOR][J_X_FOR]
        INVERSE = matrix(self.rows,self.columns)
        INVERSE.Identity()
        # .. Start with upper diagonal ..
        INDEX_ROW = 0
        INDEX_COL = 0
        SUB_COL = 1
        for J_X_FOR in range(INDEX_COL,self.columns-SUB_COL):
            # .. Find the maximum pivot to reduce the approximation error ..
            pivot,index_pivot = DUMMY.ExtractColoumn(INDEX_ROW,INDEX_COL)  
            # .. Swap the row ..
            if(INDEX_ROW!=index_pivot):
                DUMMY.SwapRows(INDEX_ROW,index_pivot)
                INVERSE.SwapRows(INDEX_ROW,index_pivot)
            for I_X_FOR in range(INDEX_ROW+1,self.rows):
                if(pivot !=0):
                    if(pivot < 0):
                      ALPHA = DUMMY.Elements[I_X_FOR][J_X_FOR]/pivot
                    else:
                      ALPHA = -DUMMY.Elements[I_X_FOR][J_X_FOR]/pivot
                    DUMMY.SumRowsForScalar(I_X_FOR,INDEX_ROW,ALPHA)
                    INVERSE.SumRowsForScalar(I_X_FOR,INDEX_ROW,ALPHA)  
            INDEX_ROW += 1
            INDEX_COL += 1
        # .. Now move to the upper terms ..
        for J_X_FOR in range(DUMMY.columns-SUB_COL,0,-1):
            for I_X_FOR in range(self.rows-1,-1,-1):
                pivot = DUMMY.Elements[J_X_FOR][J_X_FOR]
                if(pivot !=0):
                    if(pivot < 0):
                      ALPHA = DUMMY.Elements[I_X_FOR][J_X_FOR]/pivot
                    else:
                      ALPHA = -DUMMY.Elements[I_X_FOR][J_X_FOR]/pivot
                    DUMMY.SumRowsForScalar(I_X_FOR,INDEX_ROW,ALPHA)
                    INVERSE.SumRowsForScalar(I_X_FOR,INDEX_ROW,ALPHA) 
            INDEX_ROW -= 1 
        # .. Now operates on the diagonal terms .. 
        for J_X_FOR in range(DUMMY.columns): 
             if(DUMMY.Elements[J_X_FOR][J_X_FOR]!=0):
                ALPHA = 1/DUMMY.Elements[J_X_FOR][J_X_FOR]
             DUMMY.RowsForScalar(J_X_FOR,ALPHA)
             INVERSE.RowsForScalar(J_X_FOR,ALPHA)
        return(INVERSE)
    # .. Multiply the matrix for a scalar ..
    def MultScalar(self,alpha):
        for I_X_FOR in range(self.rows):
            for J_X_FOR in range(self.columns):
                self.Elements[I_X_FOR][J_X_FOR]*=alpha
        return(self)
    # .. Estimates the matrix rank with gauss reduction ..
    def Rank(self):
        rank = 0
        DET_ALPHA,Echelon = self.Gauss()
        Echelon.Round()
        DIAG_TERMS=min(self.rows,self.columns)
        for I_X_FOR in range(DIAG_TERMS):
                if(Echelon.Elements[I_X_FOR][I_X_FOR] > 0):
                    rank+=1
        if(rank > DIAG_TERMS):
            rank = DIAG_TERMS
        return(rank)  
    # .. Round the matrix elements that are below the NULL_THRESHOLD ..
    def Round(self):
        for I_X_FOR in range(self.rows):
            for J_X_FOR in range(self.columns):
                if(abs(self.Elements[I_X_FOR][J_X_FOR])<NULL_THRESHOLD):
                    self.Elements[I_X_FOR][J_X_FOR]=0
        return self
    # .. LU decomposition useful to solve linear system Ax=b with different b .. 
    def LU(self):
        U = self
        # .. Defines the L matrix .. 
        L = matrix(self.rows,self.columns)
        DUMMY = matrix(self.rows,self.columns)
        DUMMY.Identity()
        L.Identity()
        #
        SWAP_NUMBER = 0 # .. Used to identify if LU Decomposition is possible ..
        INDEX_ROW = 0
        INDEX_COL = 0
        if(self.rows==self.columns):
            # .. if the matrix is square ..
            SUB_COL = 1
        else:
            # .. if the matrix is rectangular ..
            SUB_COL = 2
        # .. Iteration .. 
        for J_X_FOR in range(INDEX_COL,U.columns-SUB_COL):
            # .. Find the maximum pivot to reduce the approximation error ..
            pivot,index_pivot = U.ExtractColoumn(INDEX_ROW,INDEX_COL)  
            # .. Swap the row ..
            if(INDEX_ROW!=index_pivot):
              U.SwapRows(INDEX_ROW,index_pivot)
              SWAP_NUMBER += 1
            for I_X_FOR in range(INDEX_ROW+1,U.rows):
                if(pivot !=0):
                    if(pivot < 0):
                      ALPHA = U.Elements[I_X_FOR][J_X_FOR]/pivot
                    else:
                      ALPHA = -U.Elements[I_X_FOR][J_X_FOR]/pivot
                    U.SumRowsForScalar(I_X_FOR,INDEX_ROW,ALPHA)   
                    DUMMY.Identity() 
                    DUMMY.SumRowsForScalar(I_X_FOR,INDEX_ROW,-ALPHA)       
                    L = L*DUMMY   
            INDEX_COL += 1    
            INDEX_ROW += 1            
        if (SWAP_NUMBER > 0):
            print("The decomposition is not suitable because of ",SWAP_NUMBER," swap lines operations")
            return(-1)
        # .. Round the U matrix ..
        U.Round() 
        L.Round() 
        # .. Return the reduced matrix echelon ..         
        return(L,U)        # .. Generates the L and U matrices ..
        
    # .. Overloading of the sum and multiplication operators ..
    def __add__(self,other):
        if((other.rows != self.rows) or (other.columns != self.columns)):
            print("Error the two matrix must have the same dimensions")
            return(-1)
        for I_X_FOR in range(other.rows):
            for J_X_FOR in range(other.columns):
                self.Elements[I_X_FOR][J_X_FOR]=self.Elements[I_X_FOR][J_X_FOR]+other.Elements[I_X_FOR][J_X_FOR]
        return self
    # .. Overloading of the * multiplication operators ..
    def __mul__(self,other):
        if(self.columns != other.rows):
            print("Error the number of coloumns of A must be equal to the rows of B")
            return -1
        RESULT = matrix(self.rows,other.columns)
        ROW_RESUL=0
        for I_X_FOR in range(self.rows):
            COL_RESUL=0
            for H_X_FOR in range(self.rows):
                DUMMY = 0
                for J_X_FOR in range(other.rows):
                    DUMMY+=self.Elements[I_X_FOR][J_X_FOR]*other.Elements[J_X_FOR][H_X_FOR]  
                RESULT.Elements[ROW_RESUL][COL_RESUL]=DUMMY
                COL_RESUL+=1
            ROW_RESUL+=1   
        return RESULT
# .. Function outside the class Matrix ..
# .. Insert a submatrix B into matrix A where Ri and Ci are the initial row and coloumn ..
def InsSub(Ri,Ci,A,B):
    if((B.rows > A.rows) or (B.columns > A.columns) or ((Ri + B.rows) > A.rows) or ((Ci + B.columns) > A.columns)):
        print("Error the submatrix is too big or placed into a wrong position")
        return(-1)
       # .. Fill the submatrix .. 
    Rsub=Ri
    for I_X_FOR in range(B.rows):
        Csub=Ci
        DUMMY=A
        for J_X_FOR in range(B.columns):
            DUMMY.Elements[Rsub][Csub]=B.Elements[I_X_FOR][J_X_FOR] 
            Csub+=1
        Rsub+=1    
    return(DUMMY)


