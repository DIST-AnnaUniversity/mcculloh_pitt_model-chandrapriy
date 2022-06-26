{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 2,
   "id": "1b7e7574",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "[0 1] value 1\n",
      "[1 1] value 0\n"
     ]
    }
   ],
   "source": [
    "import numpy as np\n",
    "def McNot(x,w,t):\n",
    "    net = np.dot(x,w)\n",
    "    if net>t:\n",
    "        output = 1\n",
    "    else:\n",
    "        output = 0\n",
    "    return output\n",
    "x0 = np.array([0,1])\n",
    "x3 = np.array([1,1])\n",
    "w = np.array([-1,1])\n",
    "t = 0\n",
    "ans1 = McNot(x0,w,t)\n",
    "print (x0, \"value\", ans1)\n",
    "ans2 = McNot(x3,w,t)\n",
    "print (x3, \"value\", ans2)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "a01fc56a",
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
