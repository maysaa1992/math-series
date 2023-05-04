def fibonacci(n):
    '''
    this function calculate the fibinacci of n number 
    param : n as integer
    return : integer
    
    but if the (n) not equal intger if return message in string tell the user enter an integer number
    '''
    if type (n) != int:
        return "please enter a number"
    if n==1 or n==0:
        return n
    else:
        return fibonacci(n-1)+fibonacci(n-2)
    
    
def lucus (n):
    '''
    this function calculate the lucus of n number 
    param : n as integer
    return : integer
    
    but if the (n) not equal intger if return message in string tell the user enter an integer number
    '''
   
    if type (n) != int:
      return "please enter a number"
    if n==0:  
        return 2
    if n==1:
        return 1
    else:
        return lucus(n-2)+lucus(n-1)
    
def sum (n,x=0,y=1):
    '''
    this function calculate the sunition of n number 
    params : n,x,y as integer
    return : integer
    
    but if the (n) not equal intger if return message in string tell the user enter an integer number
    '''
    if type (n)==int and type (x)==int and type(y) == int:
      if x==0 and y==1:
       return fibonacci(n)
      else:
        if x==2 and y==1:
          return lucus(n)   
        else:
         if (x<y ):
             return n
        
         if (n==x):
             return x
         else:
           return (n + sum(n-1))     
           
    else:
        return "please enter all integer number"
    
        
    
# print(fibonacci(8))