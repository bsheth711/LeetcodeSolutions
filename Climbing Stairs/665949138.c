int climbStairs(int n){
    /*
    x | f(x)
    1 1
    2 2
    3 3
    4 5
    5 8
    
   climbStairs(3) + climbStairs(4)
   2 2 1
   2 1 1 1
   2 1 2
    
    
           2
       1       2
     1   (2)   (1)   
    (1)
    
          1
       1       2
     1    2   1  (2)
    1 (2)  (1)   (1)
   (1) 
    
    */
    
    if (n == 1) {
        return 1;
    }
    if (n == 2) {
        return 2;
    }
    
    int arr[3];
    arr[0] = 1;
    arr[1] = 2;
    
    for (int i = 2; i < n; ++i) {
        arr[2] = arr[1] + arr[0];
        arr[0] = arr[1];
        arr[1] = arr[2];
    }
    
    return arr[2];
}