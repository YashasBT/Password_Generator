import random

# KEY CHANGE 1: The function now accepts the 'length' from the Flask app
def passworder(length): 
    a=[]
    for j in range(65,91):
        a.append(j)
    smallalp=[]
    for q in range(97,123):
        smallalp.append(q)
    spesal=[]
    for w in range(33,48):
        spesal.append(w)
    numb=[]
    for v in range(48,58):
        numb.append(v)
    
    # KEY CHANGE 2: Removed these lines, since 'length' now comes from the app
    # n=[8,9,10,11,12,13,14,15,16]
    # c=random.choice(n)
    
    PassW=[]
    
    # KEY CHANGE 3: Use the 'length' argument in the loop
    for i in range(length): 
        # Line 26: Invisible character removed and indentation fixed
        b=random.choice(a) 
        d=random.choice(smallalp)
        e=random.choice(spesal)
        f=random.choice(numb)
        u=chr(b)
        x=chr(d)
        y=chr(e)
        z=chr(f)
        met=[u,x,y,z]
        dem=random.choice(met)
        PassW.append(dem)
        
        # KEY CHANGE 4: Moved this line OUTSIDE the loop
        # jest=''.join(PassW) 
    
    # This now runs only ONCE, after the loop is finished
    jest=''.join(PassW) 
    
    # KEY CHANGE 5: Return the password to Flask, instead of printing
    return jest 

# KEY CHANGE 6: Removed the call at the end. The server (app.py) will call it.
# passworder()