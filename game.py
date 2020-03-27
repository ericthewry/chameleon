from argparse import ArgumentParser
import random
import getpass
import smtplib
import ssl





def main():
    parser = ArgumentParser(description="The Chameleon Game")
    parser.add_argument('players_file', type=str,
                        help="the file containing player names")
    args = parser.parse_args()
    
    players = []
    with open(args.players_file, 'r') as fp:
        players = [row.strip().split(',') for row in fp.readlines()]

    
    chameleon = random.choice(players)[0]
    # print (chameleon, "is the chameleon")
    column = random.choice(['A', 'B', 'C', 'D'])
    row = random.choice(['1','2','3','4'])

    port = 465
    memail = "chameleonappmachine@gmail.com"
    password = getpass.getpass(prompt="type your password and press enter: ")
    context = ssl.create_default_context()
    
    
    with smtplib.SMTP_SSL("smtp.gmail.com", port, context=context) as server:

        server.login(memail, password)
        
        for (player, pemail) in players:
            message = player + "Something went wrong, ask Eric for help"
            if player == chameleon:
                message = "Subject: " + player.capitalize() + ", you are the Chameleon!\n"
            else:
                message = "Subject: " + player.capitalize() + ", Examine " + column + row + "\n"
                
            server.sendmail(memail, [pemail], message)
            print("sent to", player)
        return


if __name__ == "__main__": main()
