#Programming I

####################################
#           Side Quest 3.2         #
#           Caesar Cipher          #
####################################

#Background
#==========
#The encryption of a plaintext by Caesar Cipher is:
#En(Mi) = (Mi + n) mod 26 

#Write a Python program that prompts user to enter a plaintext
#and displays the encrypted result using Caesar Cipher.

#Important Notes
#===============
#1) Comment out ALL input prompts before submitting.
#2) You MUST (at least) use the following variables:
#   - plaintext
#   - n (to represent number of shifts in int)
#   - ciphertext

#START CODING FROM HERE
#======================
# plaintext = input("Enter plaintext:")
# n = input("Enter the number of positions to be shifted: ")

alphabets = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

#Function to perform the encryption of given plaintext
def caesarEncrypt(plaintext, n):
    ciphertext = []
    #Code to do the conversion
    for char in str(plaintext.upper()):
        index = alphabets.index(char)
        new_index = (index + int(n)) % 26
        new_char = alphabets[new_index]
        ciphertext.append(new_char)
    
    ciphertext=''.join(ciphertext)

    return ciphertext #Do not remove this line


#You need only to copy and paste the function into Coursemology for submission
#The rest of code from here onwards are not needed 

#Display output heading


#Prompt user for input of plaintext and number of shifts

   
#Call the function to get the cipher text


#Display the output


#input 'HELLOWORLDTHESECRETISOUT',5 output 'MJQQTBTWQIYMJXJHWJYNXTZY'
