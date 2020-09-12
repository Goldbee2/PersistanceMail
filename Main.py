import Email

class terminal_colors:
    DARK_BLUE = '\033[34m'
    LIGHT_BLUE = '\033[94m'
    LIGHT_GREEN = '\033[92m'
    END = '\033[0m'
    # BOLD = '\033[1m'
    # UNDERLINE = '\033[4m'

def main():
    inbox = Email.EmailQueue
    inbox.set_username_and_password(inbox)
    inbox.login(inbox)
    print('logged in successfully')
    inbox.select_inbox(inbox)
    print('selected inbox successfully')
    inbox.initialize_queue(inbox, 20)
    print('initialized queue successfully')
    for i in range(len(inbox.email_queue)):
        email_number_formatted = terminal_colors.LIGHT_GREEN + '{:>8}' + terminal_colors.END
        print(email_number_formatted.format('[' + str(i+1) + ']  '), end='')
        if i % 2 == 0:
            dark_blue_subject_line = terminal_colors.DARK_BLUE + '{:60.60}' + terminal_colors.END
            print(dark_blue_subject_line.format(inbox.email_queue.pop()))
        else:
            light_blue_subject_line = terminal_colors.LIGHT_BLUE + '{:60.60}' + terminal_colors.END
            print(light_blue_subject_line.format(inbox.email_queue.pop()))

main()


#open window
#fade out, google login
#loading screen
#pop in email tabs

#while loop