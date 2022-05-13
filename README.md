# Matrix-Flatten
Converting 3D Array into 1D Array by reshape function in python.<br>
Numpy stores arrays internally as continguous arrays. It allows us to reshape the dimenstions of a numpy array by only modifying it's strides.<br>
Taking advantage of the way Numpy stores its array we can reshape it without incurring any siginificant computational cost.
