






while 1==1 :     # Program runs indefinitely

   

    def startScreen():         # Start screen is displayed

        'CLEAR SCREEN HERE'  # Clear the screen to focus

        print(
        '''
        ##################################################################


            Cybersecurity Basics Suite
                  
                  Aidan Afshar


        ##################################################################

        1   Password Strength Guage
        2   Text Encryption
        3   Ransomware Generator
        4   Keylogger Generator
        5   Bruteforce Cracker
        6   Exit

        '''
        )

       

    startScreen(); # Main menu display function is called

    selectedOption = "";          
    selectedOption = input("Select an option: ");

       



    ####################### Password Strength Guage #######################
    if selectedOption == "1":

        def passwordStrengthGuage():
            'CLEAR SCREEN HERE'

            print("-------------Password Strength Guage-------------")

            enteredPassword = input("Enter a password: "); # User enters a password

            # Strong 
                # Has >= 12 characters
                # Contains >= 2 uppercase characters
                # Contains >= 2 lowercase characters
                # Contains >= 5 unique characters
                # Is not found on RockYou
            # Medium
                # Has 8-11 characters
                # Has 1 uppercase
                # Has 1 lowercase
                # Has 1 unique character
                # Is not found on RockYou
            # Weak
                # Has < 8 characters
                # Is found on RockYou

            

            strengthRating = "strong"; # Password strength is calculated (Remove later)

            print("Your password (" + enteredPassword + ") is a " + strengthRating + " password."); # Password strength is told to the user

            if input("Enter 1 to retry. Press enter to return to main menu") == "1": # Ask the user if they want to retry or go to main menu

                passwordStrengthGuage();

        passwordStrengthGuage();
      
    ####################### END PASSWORD STRENGTH GUAGE #######################


















    ####################### TEXT ENCRYPTION #######################
    
    elif selectedOption == "2":
        def textEncryption():
            print("-------------Text Encryptor-------------")

        textEncryption();

    ####################### END TEXT ENCRYPTION #######################







    else:
        startScreen();

            

        



