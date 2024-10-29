Matrix is a class that implements a set of operations on matrices. The code is written in python3, and is an alternative to other libraries.
The reference book is F. Odetti, M. Raimondo, "Elementi di Algebra Lineare," ECIG - ISBN -88-7545-480-9.
The library implements the following functions:
  
  1) Zeros() 			# .. Create a matrix of zeros ..
  2) Scalar(Alpha)		# .. Create a matrix of scalar Alpha ..
  3) Random(minval,maxval)	# .. Create a matrix of random scalar between minval maxval..
  4) Identity() 		# .. Create an identity matrix  ..
  5) put(i,j) 			# .. Set the element Mij in the matrix .. 
  6) get(i,j)			# .. Retrieve element Mij in the matrix ..  
  7) MultForScalar(Alpha)	# .. Multiply a matrix for a scalar ..
  8) SwapRows(i,j) 		# .. Elementary operation 1) swap two rows .. 
  9) RowsForScalar(i,Alpha) 	# .. Elementary operation 2) multiply the row i for scalar Alpha ..
 10) SumRowsForScalar(i,j,Alpha)# .. Elementary operation 3) sum two rows i,j and the second multiplied for a scalar ..
 11) Trans()			# .. Transpose the matrix.
 12) ExtractColoumn(row,coloumn)# .. Extract coloumn ..
 13) Gauss() 			# .. Apply the Gauss Method to solve linear systems of equations [A]x=[B] ..
 14) GaussJordan() 		# .. Apply the Gauss-Jordan Method to solve linear systems of equations [A]x=[B] ..
 15) Det()  			# .. Estimate the Det of a square matrix ..
 16) SubExt(Ri,Rf,Ci,Cf)	# .. Estract a submatrix from a matrix ..
 17) Inv() 			# .. Estimates the inverse of the matrix ..
 18) MultScalar(Alpha)		# .. Multiply the matrix for a scalar Alpha ..
 19) Rank()			# .. Estimates the matrix rank with Gauss reduction ..
 20) Round()			# .. Round the matrix elements that are below the NULL_THRESHOLD ..
 21) LU()			# .. LU decomposition useful to solve linear system Ax=b with different b .. 
# .. Function outside the class Matrix ..
 22) InsSub(Ri,Ci,A,B)		# .. Insert a submatrix B into matrix A where Ri and Ci are the initial row and coloumn ..

----------------------------------------
The operators + and * are overloaded, which means that you can write expressions C=A+B  or C=A*B directly on the matrices.

    
Usage:
There is a main.py file example that shows how to use the class and all the different functions implemented. With practical examples and simple exercises. 

License:
See LICENSE.txt for more information.

Contact: Massimo Donelli - massimo.donelli@unitn.it 

Project link: https://github.com/MassimoDonelli/matrix.git
