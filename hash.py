import bcrypt 
  
def hashing(password):
    bytes = password.encode('utf-8') 
    salt = bcrypt.gensalt() 
    hash = bcrypt.hashpw(bytes, salt) 
    return hash

def verify(hash,userPassword):
    userBytes = userPassword.encode('utf-8') 
    hash = hash.encode('utf-8')
    return bcrypt.checkpw(userBytes, hash) 

if "__main__"==__name__:
    hash = hashing("karthik")
    userPassword =  'karthik'
  
    # encoding user password 
    userBytes = userPassword.encode('utf-8') 
    
    # checking password 
    result = bcrypt.checkpw(userBytes, hash) 
    
    print(result)