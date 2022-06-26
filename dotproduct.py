
   "outputs": [
    {
     
      "Dot Product  : \n",
      " [[22 12]\n",
      " [40 32]]\n",
      "\n",
      "Dot Product  : \n",
      " [[22 32]\n",
      " [15 32]]\n"
     ]
   
   "source": [
    "import numpy as np\n",
    "vector_a = np.array([[1, 4], [5, 6]])\n",
    "vector_b = np.array([[2, 4], [5, 2]])\n",
    "product = np.dot(vector_a, vector_b)\n",
    "print(\"Dot Product  : \\n\", product)\n",
    "product = np.dot(vector_b, vector_a)\n",
    "print(\"\\nDot Product  : \\n\", product)\n",
    " "
   ]
  
  
   "outputs": [
    {
     
      "Dot Product  : \n",
      " [[32 24 36]\n",
      " [60 56 76]\n",
      " [48 44 62]]\n",
      "\n",
      "Dot Product  : \n",
      " [[46 62 38]\n",
      " [43 67 39]\n",
      " [39 61 37]]\n"
     ]
    
   "source": [
    "import numpy as np\n",
    "vector_a = np.array([[1,4,2],[5,6,4],[4,5,3]])\n",
    "vector_b = np.array([[2,4,6],[5,2,7],[5,6,1]])\n",
    "product = np.dot(vector_a,vector_b)\n",
    "print(\"Dot Product  : \\n\", product)\n",
    "product = np.dot(vector_b, vector_a)\n",
    "print(\"\\nDot Product  : \\n\", product)"
   ]
 
