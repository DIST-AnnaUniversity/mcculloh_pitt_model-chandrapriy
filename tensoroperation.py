{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 4,
   "id": "f829d7bd",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "tf.Tensor([[4 6]], shape=(1, 2), dtype=int32)\n"
     ]
    }
   ],
   "source": [
    "import tensorflow as tf\n",
    "tensor_a = tf.constant([[1,2]], dtype = tf.int32)\n",
    "tensor_b = tf.constant([[3, 4]], dtype = tf.int32)\n",
    "tensor_add = tf.add(tensor_a, tensor_b)\n",
    "print(tensor_add)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 10,
   "id": "d3eff9b3",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "tf.Tensor([[-2 -2]], shape=(1, 2), dtype=int32)\n"
     ]
    }
   ],
   "source": [
    "import tensorflow as tf\n",
    "tensor_a = tf.constant([[1,2]], dtype = tf.int32)\n",
    "tensor_b = tf.constant([[3, 4]], dtype = tf.int32)\n",
    "tensor_subtract = tf.subtract(tensor_a, tensor_b)\n",
    "print(tensor_subtract)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 11,
   "id": "c41ce969",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "tf.Tensor([[3 8]], shape=(1, 2), dtype=int32)\n"
     ]
    }
   ],
   "source": [
    "import tensorflow as tf\n",
    "tensor_a = tf.constant([[1,2]], dtype = tf.int32)\n",
    "tensor_b = tf.constant([[3, 4]], dtype = tf.int32)\n",
    "tensor_mul= tf.multiply(tensor_a, tensor_b)\n",
    "print(tensor_mul)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "d1b7689c",
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
