import bcrypt

# hashes a plaintext password using bcrypt with bcrypt the hash
# contains the salt, so no need to store separately.

def hash_password (password):

    salt = bcrypt.gensalt()
    hash = bcrypt.hashpw(password, salt)

    return hash

def check_password (password, hash):

    hashpw = bcrypt.hashpw(password, hash)

    if hashpw == hash:
        return True
    else:
        return False

password = "secret".encode('utf-8')

hash = hash_password (password)
print (hash)


new_pword = "secret!!!".encode('utf-8')

if check_password(new_pword, hash):
    print ("passwords match!")
else:
    print ("passwords DON'T match!")
