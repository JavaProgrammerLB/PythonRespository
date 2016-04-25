from verbalexpressions import VerEx
# Create an example of how to test for correctly formed URLs
verbal_expression = VerEx()
tester = (verbal_expression.
            start_of_line().
            find('http').
            maybe('s').
            find('://').
            maybe('www.').
            anything_but(' ').
            end_of_line()
)

# Create an example URL
test_url = "https://www.google.com"

# Test if the URL is valid
if tester.match(test_url):
    print ("Valid URL")

#Print the generated regex
print (tester.source()) # => ^(http)(s)?(\:\/\/)(www\.)?([^\ ]*)$
