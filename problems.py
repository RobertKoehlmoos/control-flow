"""
Fizzbuzz is a classic programming challenge used to assess whether the person you're interviewing
is just lying about knowing how to code.
The rules are as follows:
As input you will receive a single number.
If that number is divisible by 3 and 5 return the string "FizzBuzz"
If that number is divisible by 3 return the string "Fizz"
If that number is divisible by 5 return the string "Buzz"
Otherwise return the string representation of the number
"""


def fizzbuzz(n: int) -> str:
    pass


"""
Similar to above, but now you return the FizzBuzz result of the numbers from 1 to 100, inclusive
Return a string with number separated by a newline character.
For example, if I wanted the numbers 4 to 6, inclusive, you would need to return "4\nBuzz\nFizz"
If you're clever and want to get a bit ahead you can use the fizzbuzz function you created above.
If you're really clever you realized you can just have it return the right string immediately. Don't do that.
"""


def fizzbuzz_first_100() -> str:
    pass


"""
The Caesar Cipher is an old encryption technique that is often used as an introduction to ciphers.
To encrypt a string of characters, take the original letters and shift them down the alphabet a certain amount
determined by the key.
For example, if you had the letter 'a' and the key was 3, 'a' would be encrypted into 'd'
Decryption occurs in the opposite direction, so you had the letter 'd' and the encryption key 3 then
then it would become 'a'
If a shift would cause a letter to go beyond the edges of the alphabet wrap around to the opposite side of the
alphabet and continue shifting.
For example, with a key of 2 'z' encrypts to 'b' and 'a' decrypts to 'y'

For this problem you will implement an encryption and decryption function, each of which take a string
to be transformed and a key. 
The strings you receive will contain upper and lower case letters, along with non-letter characters.
All letters returned should be uppercase (trust me, this makes it easier), and do not change non-letter characters.
For example, "Hello, World!" with a key of 7 encrypts to "OLSSV, DVYSK!", which would decrypt back to "HELLO, WORLD!"
"""


def encode_caesar(plain_text: str, key: int) -> str:
    pass


def decode_caesar(cipher_text: str, key: int) -> str:
    pass
