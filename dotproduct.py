{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 2,
   "id": "748e7828",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Dot Product  : \n",
      " [[22 12]\n",
      " [40 32]]\n",
      "\n",
      "Dot Product  : \n",
      " [[22 32]\n",
      " [15 32]]\n"
     ]
    }
   ],
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
  },
  {
   "cell_type": "code",
   "execution_count": 6,
   "id": "f8f497b0",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
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
    }
   ],
   "source": [
    "import numpy as np\n",
    "vector_a = np.array([[1,4,2],[5,6,4],[4,5,3]])\n",
    "vector_b = np.array([[2,4,6],[5,2,7],[5,6,1]])\n",
    "product = np.dot(vector_a,vector_b)\n",
    "print(\"Dot Product  : \\n\", product)\n",
    "product = np.dot(vector_b, vector_a)\n",
    "print(\"\\nDot Product  : \\n\", product)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "8afd0128",
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "7e01a67d",
   "metadata": {},
   "outputs": [],
   "source": []
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3 (ipykernel)",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.9.12"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
