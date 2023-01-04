

with open("/Users/Cook/Documents/VS Code/Day 20/MailMerge/Input/Letters/starting_letter.txt") as letter_file:

    the_letter = letter_file.read()

with open("/Users/Cook/Documents/VS Code/Day 20/MailMerge/Input/Names/invited_names.txt") as names_file:
    
    names = names_file.readlines()
    

for recipient in names:
    stripped_name = recipient.strip()
    new_letter = the_letter.replace("[name]", stripped_name)
    
    with open(f"/Users/Cook/Documents/VS Code/Day 20/MailMerge/Output/ReadyToSend/Letter to {stripped_name}.txt", "w") as completed_letter:
        completed_letter.write(new_letter)

   
            
    

            
            
            
                
                