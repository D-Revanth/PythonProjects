def word_count(text) :
    # Using strip() function eliminates extra spaces
    text = text.strip()


    # Using split() the text is separated on the basis of space between words
    # words is of LIST DataType
    words = text.split() 

    # Using len() function to return the size of the list
    return len(words)


if __name__ == "__main__" :
    # Take input from user.
    input_text = input("Enter your sentence/paragraph : ") 
    # The input stored is a string 

    # Call word_count function to count number of words and store the value in n
    n = word_count(input_text)

    print("\n\n--------------------------------------------------------")

    # Print number of words in the text
    if n :
        print(f"Number of words in the given text: {n}")
    
    else :
        print("You didn't enter anything, please try again.")