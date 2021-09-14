from problems import fizzbuzz, fizzbuzz_first_100, encode_caesar, decode_caesar
import pytest

fizz_buzz_test_nums = (
    -20, -19, -18, -17, -16, -15, -14, -13, -12, -11, -10, -9, -8, -7, -6, -5, -4, -3, -2, -1,
    0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20,
    21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40,
    41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60,
    61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71, 72, 73, 74, 75, 76, 77, 78, 79, 80,
    81, 82, 83, 84, 85, 86, 87, 88, 89, 90, 91, 92, 93, 94, 95, 96, 97, 98, 99)
fizzbuzz_test_answers = (
    "Buzz", "-19", "Fizz", "-17", "-16", "FizzBuzz", "-14", "-13", "Fizz", "-11", "Buzz", "Fizz", "-8",
    "-7", "Fizz", "Buzz", "-4", "Fizz", "-2", "-1", "FizzBuzz", "1", "2", "Fizz", "4", "Buzz", "Fizz",
    "7", "8", "Fizz", "Buzz", "11", "Fizz", "13", "14", "FizzBuzz", "16", "17", "Fizz", "19", "Buzz",
    "Fizz", "22", "23", "Fizz", "Buzz", "26", "Fizz", "28", "29", "FizzBuzz", "31", "32", "Fizz", "34",
    "Buzz", "Fizz", "37", "38", "Fizz", "Buzz", "41", "Fizz", "43", "44", "FizzBuzz", "46", "47",
    "Fizz", "49", "Buzz", "Fizz", "52", "53", "Fizz", "Buzz", "56", "Fizz", "58", "59", "FizzBuzz",
    "61", "62", "Fizz", "64", "Buzz", "Fizz", "67", "68", "Fizz", "Buzz", "71", "Fizz", "73", "74",
    "FizzBuzz", "76", "77", "Fizz", "79", "Buzz", "Fizz", "82", "83", "Fizz", "Buzz", "86", "Fizz",
    "88", "89", "FizzBuzz", "91", "92", "Fizz", "94", "Buzz", "Fizz", "97", "98", "Fizz")


@pytest.mark.parametrize("number,answer", zip(fizz_buzz_test_nums, fizzbuzz_test_answers))
def test_fizzbuzz(number, answer):
    assert fizzbuzz(number) == answer


def test_fizzbuzz_first_100():
    assert fizzbuzz_first_100() == "1\n2\nFizz\n4\nBuzz\nFizz\n7\n8\nFizz\nBuzz\n11\nFizz\n13\n14\nFizzBuzz\n16\n17\nFizz\n19\nBuzz\nFizz\n22\n23\nFizz\nBuzz\n26\nFizz\n28\n29\nFizzBuzz\n31\n32\nFizz\n34\nBuzz\nFizz\n37\n38\nFizz\nBuzz\n41\nFizz\n43\n44\nFizzBuzz\n46\n47\nFizz\n49\nBuzz\nFizz\n52\n53\nFizz\nBuzz\n56\nFizz\n58\n59\nFizzBuzz\n61\n62\nFizz\n64\nBuzz\nFizz\n67\n68\nFizz\nBuzz\n71\nFizz\n73\n74\nFizzBuzz\n76\n77\nFizz\n79\nBuzz\nFizz\n82\n83\nFizz\nBuzz\n86\nFizz\n88\n89\nFizzBuzz\n91\n92\nFizz\n94\nBuzz\nFizz\n97\n98\nFizz\nBuzz"


phrases = ("She has a huge collection of comic books.",
           "Is this a complete collection of baseball cards?",
           "A small collection of people were unhappy with the decision.",
           "These paintings are part of the museum's permanent collection.",
           "Thieves stole the valuable collection of statues.",
           "This museum collection is the best in the world.",
           "You have an impressive CD collection.",
           "She's in charge of debt collection.",
           "These clothes are from the spring collection.",
           "He owns a collection of cars.",
           "The company assembled a smart collection of people.",
           "I've decided to start a collection of souvenirs.",
           "This trading card will complete my collection.",
           "I am editing a collection of her poetry.")
keys = (9, 25, 6, 26, 3, 19, 25, 17, 3, 19, 11, 7, 5, 0)
encoded_phrases = ('BQN QJB J QDPN LXUUNLCRXW XO LXVRL KXXTB.',
                   'HR SGHR Z BNLOKDSD BNKKDBSHNM NE AZRDAZKK BZQCR?',
                   'G YSGRR IURRKIZOUT UL VKUVRK CKXK ATNGVVE COZN ZNK JKIOYOUT.',
                   "THESE PAINTINGS ARE PART OF THE MUSEUM'S PERMANENT COLLECTION.",
                   'WKLHYHV VWROH WKH YDOXDEOH FROOHFWLRQ RI VWDWXHV.',
                   'MABL FNLXNF VHEEXVMBHG BL MAX UXLM BG MAX PHKEW.',
                   'XNT GZUD ZM HLOQDRRHUD BC BNKKDBSHNM.',
                   "JYV'J ZE TYRIXV FW UVSK TFCCVTKZFE.",
                   'WKHVH FORWKHV DUH IURP WKH VSULQJ FROOHFWLRQ.',
                   'AX HPGL T VHEEXVMBHG HY VTKL.',
                   'ESP NZXALYJ LDDPXMWPO L DXLCE NZWWPNETZY ZQ APZAWP.',
                   "P'CL KLJPKLK AV ZAHYA H JVSSLJAPVU VM ZVBCLUPYZ.",
                   'YMNX YWFINSL HFWI BNQQ HTRUQJYJ RD HTQQJHYNTS.',
                   'I AM EDITING A COLLECTION OF HER POETRY.')


@pytest.mark.parametrize("phrase,key,encoded_phrase", zip(phrases, keys, encoded_phrases))
def test_encode_caesar(phrase, key, encoded_phrase):
    assert encode_caesar(phrase, key) == encoded_phrase


decoded_phrases = ("SHE HAS A HUGE COLLECTION OF COMIC BOOKS.",
                   "IS THIS A COMPLETE COLLECTION OF BASEBALL CARDS?",
                   "A SMALL COLLECTION OF PEOPLE WERE UNHAPPY WITH THE DECISION.",
                   "THESE PAINTINGS ARE PART OF THE MUSEUM'S PERMANENT COLLECTION.",
                   "THIEVES STOLE THE VALUABLE COLLECTION OF STATUES.",
                   "THIS MUSEUM COLLECTION IS THE BEST IN THE WORLD.",
                   "YOU HAVE AN IMPRESSIVE CD COLLECTION.",
                   "SHE'S IN CHARGE OF DEBT COLLECTION.",
                   "THESE CLOTHES ARE FROM THE SPRING COLLECTION.",
                   "HE OWNS A COLLECTION OF CARS.",
                   "THE COMPANY ASSEMBLED A SMART COLLECTION OF PEOPLE.",
                   "I'VE DECIDED TO START A COLLECTION OF SOUVENIRS.",
                   "THIS TRADING CARD WILL COMPLETE MY COLLECTION.",
                   "I AM EDITING A COLLECTION OF HER POETRY.")


@pytest.mark.parametrize("encoded_phrase,key,decoded_phrase", zip(encoded_phrases, keys, decoded_phrases))
def test_decode_caesar(encoded_phrase, key, decoded_phrase):
    assert decode_caesar(encoded_phrase, key) == decoded_phrase
