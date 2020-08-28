"""If you don’t have a current code sample you can share, please write a small web application 
in one of the above languages (Python/Ruby/Node). The application only needs to do the following:
Accept a POST request to the route “/test”, which accepts one argument “string_to_cut”
Return a JSON object with the key “return_string” and a string containing every third letter from the original string
(e.g.) If you POST {"string_to_cut": "iamyourlyftdriver"}, it will return: {"return_string": "muydv"}.

Note: To see expected behavior you can test against a current working example with the command: 
curl -X POST https://lyft-interview-test.glitch.me/test --data '{"string_to_cut": "iamyourlyftdriver"}' -H 'Content-Type: application/json'
"""

def make_every_third_str(string_dict):
    """make a new string from every third letter

        >>> make_every_third_str({"string_to_cut": "iamyourlyftdriver"})
        {'return_string': 'muydv'}

    """

    #make a dictionary that will contain the new string at key "return_string"
    return_dict = {"return_string":""}

    #loop though string indexes using range and len
    #this assumes that the key will always be "string_to_cut"
    for i in range(len(string_dict["string_to_cut"])-1):
        #if an index + 1 is divisible by 3 with no remainder then it is a multiple of 3 
        #so the letter at that index can be added to the "return_string"
        if (i + 1) % 3 == 0:
            #add ltr at i to "return_string"
            return_dict["return_string"]  =  return_dict["return_string"]  + string_dict["string_to_cut"][i]
    
    return return_dict

#if the fuction is being called from this file run the doctest
if __name__ == '__main__':
    import doctest
    if doctest.testmod().failed == 0:
        print("\n*** ALL TEST PASSED!")

