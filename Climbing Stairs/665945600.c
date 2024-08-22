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
    int arr[n + 1];
    arr[0] = 1;
    arr[1] = 2;
    
    for (int i = 2; i < n; ++i) {
        arr[i] = arr[i-1] + arr[i-2];
    }
    
    return arr[n-1];
}