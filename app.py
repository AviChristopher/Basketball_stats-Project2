import constants
from constants import TEAMS
from constants import PLAYERS
from copy import deepcopy
from statistics import mean


cleaned_data=[]
exp_player=[]
inexp_player=[]
Panthers1=[]
Bandits1=[]
Warriors1=[]

    
    
    
def clean_data():   
    for player in PLAYERS:            
            fixed={}
            fixed['name']=player['name']
            split_guardians= player['guardians'].split('and')
            fixed['guardians']=split_guardians          
            if player['experience']=='YES':
                fixed['experience'] = True              
            else:
                fixed['experience']=False                
            split_height = player['height'].split()
            split_height = int(split_height[0])
            fixed['height'] = split_height
            cleaned_data.append(fixed)
                       
            


def div_list(arg):
     for item in cleaned_data:
            if item['experience']==True:
                exp_player.append(item)
            else:
                inexp_player.append(item)                          
        
def balance_teams():      
    numExpPerTeam= int(len(exp_player)/len(TEAMS))
    numInexpPerTeam=int(len(exp_player)/len(TEAMS))
    all_players = numExpPerTeam + numInexpPerTeam                      
    for player in exp_player:
        if len(Panthers1) < numExpPerTeam:
            Panthers1.append(player)
        elif len(Bandits1)< numExpPerTeam:
            Bandits1.append(player)
        else:
             Warriors1.append(player)
            
    for player in inexp_player:
        if len(Panthers1) < all_players:
                Panthers1.append(player)
        elif len(Bandits1) < all_players:
                Bandits1.append(player)
        else:
                Warriors1.append(player) 
                
    
def get_options(arg):
    heightList = []
    list_players = []
    guardians_players = []
    
    print(f"\n Total players:{len(arg)}")    
    print(f"\n Total experienced:{int(len(arg)/2)}")
    print(f"\n Total experienced:{int(len(arg)/2)}")
    
    for x in arg:
        for key,value in x.items():
            if key =="height":
                val = value
                heightList.append(val)
    print(f"\n Average height:{mean(heightList)}")
        
    for x in arg:
        for key,value in x.items():
            if key =="name":
                val = value
                list_players.append(val)        
                li = ','.join(list_players)                
    print(f"\n Players on the Team: \n  {li} ")
    
    
    for i in arg:
        for key,value in i.items():
            if key =="guardians":
                val = value
                guardians_players.append(val)                   
                li2 = ','.join(str(guardian) for guardian in guardians_players)                 
    print(f"\n Guardians: \n  {li2}")  
    input("Press Enter to continue...")
    
    




def start(): 
    #while True:
        print("\n BASKETBALL TEAM STATS TOOL ")
        print("\n")
        print("----MENU----")
                
        while True:
            print("\n Here are your choices:\nA) Display Team Stats \nB) Quit \n")
            option=input("\nEnter an option  A/B:  ").lower()
            if option== "":
                print("Option can't be left blank!")
                continue
            elif option.isnumeric():
                print("Can't be a number!Try again...")
                continue
            elif option != "a" and option != "b" :
                print("Not a valid option! Please select from the menu")      
            elif option == "a":
                print("\n A) Panthers")
                print("\n B) Bandits")
                print("\n C) Warriors")      
            elif option =='b':
                print("Goodbye!")
                break
#            while True:
            userTeamOption=input("\nEnter an option A/B/C:  ").lower()
            if userTeamOption == "":
                print("Option can't be left blank!")
                continue
            elif userTeamOption.isnumeric():
                print("Can't be a number!Try again...")
                continue
            elif userTeamOption != "a" and userTeamOption != "b" and userTeamOption != "c":
                print("Not a valid option! Please select from the menu")
                continue                
                break
            elif userTeamOption == "a":
                print("    _-_-TEAM_-_-")
                print("\n===Panthers Stats===" )
                get_options(Panthers1)
                            
            elif userTeamOption=="b":
                print("    _-_-TEAM_-_-")
                print("\n===Bandits Stats===" )
                get_options(Bandits1)                
            else:
                print("    _-_-TEAM_-_-")
                print("\n===Warriors Stats===" )
                get_options(Warriors1)
            
    
        
        
if __name__ == '__main__':        
    clean_data()
    div_list(cleaned_data)
    balance_teams()
    start()


#   my_list = ['[bobby]', '[hadz]', '[com]']
#
#result = [item.replace('[', '').replace(']', '') for item in my_list]
#print(result)  # 👉️ ['bobby', 'hadz', 'com']


