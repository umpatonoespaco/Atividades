from easygui import *

texto = 'Are you sure?'

title = 'Alert'

button_list = []

button1 = 'Yes'

button2 = 'Yes'

button_list.append(button1)

button_list.append(button2)

output = buttonbox(texto, title, button_list)

if output == button1 or button2:

    texto2 = 'Choice is a construct and we all live in lies, do you agree?'

    title2 = '...'

    button_list2 = []

    button3 = 'Yes'

    button4 = 'No'

    button_list2.append(button3)
    button_list2.append(button4)

    output2 = buttonbox(texto2, title2, button_list2)

    if output2 == button3:

        texto3 = "Then you might be right, after all, you had a choice there didn't you?"

        button5 = 'Maybe...'

        button_list3 = []
        
        button_list3.append(button5)

        output3 = buttonbox(texto3, title2, button_list3)
    
    elif output2 == button4:

        texto4 = "Then why were 2 options back there? You really think you DON'T have a choice?"

        button6 = "I don't"

        button7 = "I do, Actually"

        button_list4 = []

        button_list4.append(button6)
        button_list4.append(button7)

        output4 = buttonbox(texto4, title2, button_list4)

        if output4 == button7:

            texto5 = "I am only a string of ones and zeroes, no choice is clear, no choice is right. The only one who decides who you yourself is can only be the latter... Do you agree?"

            button_list5 = []

            button_list5.append(button1)
            button_list5.append(button2)

            output5 = buttonbox(texto5, title2, button_list5)

            texto6 = "A man without a mouth is a man without a reason... Do you agree?"

            button_list6 = []

            button_list6.append(button1)
            button_list6.append(button2)

            output6 = buttonbox(texto6, title2, button_list6)

            texto7 = "And after all this do you STILL think you have a choice?"

            button8 = "You have no power over me"
            button9 = "I have no choice"

            button_list7 = []

            button_list7.append(button8)
            button_list7.append(button9)

            
            output7 = buttonbox(texto7, title2, button_list7)

            texto8 = "You never learn, do you?"

            button10 = "..."

            button_list8 = []
            
            button_list8.append(button10)
            button_list8.append(button10)

            output8 = buttonbox(texto8, title2, button_list8)



    

