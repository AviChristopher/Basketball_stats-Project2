from constants import PLAYERS
from constants import TEAMS
from statistics import mean

cleaned_data=[]
exp_player=[]
inexp_player=[]
Panthers=[]
Bandits=[]
Warriors=[]

#print(exp_player)

num_players_team=int(len(PLAYERS)/len(TEAMS))
#print(num_players_team)

def clean_data(PLAYERS):
    #exp_list=[]
    #inexp_list=[]
    for player in PLAYERS:
            # print(player)
            fixed={}
            fixed['name']=player['name']
            split_guardians= player['guardians'].split(' and ')
            fixed['guardians']=split_guardians          
            if player['experience']=='YES':
              fixed['experience'] = True 
              # exp_list.append(player)
              # exp_player.append(exp_list)
            else:
                fixed['experience']=False             
            split_height = player['height'].split()
            split_height = int(split_height[0])
            fixed['height'] = split_height          
            cleaned_data.append(fixed)
    
    # print("cleaned_data>>>>", cleaned_data)
    

def div_list(li):
    for item in li:
        if item['experience']==True:
            exp_player.append(item)
        else:
            inexp_player.append(item)
           
   
def balance_teams():
        
    numExpPerTeam= int(len(exp_player)/len(TEAMS))
    numInexpPerTeam=int(len(exp_player)/len(TEAMS))
    all_players = numExpPerTeam + numInexpPerTeam
                      
    for player in exp_player:
        if len(Panthers) < numExpPerTeam:
            Panthers.append(player)
        elif len(Bandits)< numExpPerTeam:
            Bandits.append(player)
        else:
            Warriors.append(player)
            
    for player in inexp_player:
        if len(Panthers) < all_players:
                          Panthers.append(player)
        elif len(Bandits) < all_players:
              Bandits.append(player)
        else:
              Warriors.append(player)
    # print("Panther>>>",Panthers)
    #print("Bandits>>>",len(Bandits))
    # print("Warriors>>>",len(Warriors))

def start():
  while True:    
    print("\n BASKETBALL TEAM STATS TOOL ")
    print("\n")
    print("----MENU----")
    print("\n")    
    print("\nHere are your choices:\nA) Display Team Stats \nB) Quit \n")
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
      
    else:
      option =='b'
      print("Goodbye!")
      break

    userTeamOption=input("Enter an option A/B/C:  ").lower()
    if userTeamOption == "":
      print("Option can't be left blank!")
      continue
    elif userTeamOption.isnumeric():
      print("Can't be a number!Try again...")
      continue
    elif userTeamOption != "a" and option != "b" != "c":
      print("Not a valid option! Please select from the menu")
      continue
          
    if userTeamOption == "a":
       print("\nTEAM:Panthers Stats" )
       print("\n__________________")
       print(f"\n Total players:{len(Panthers)}")    
       print(f"\n Total experienced:{int(len(Panthers)/2)}")
       print(f"\n Total experienced:{int(len(Panthers) /2)}")
         
       heightList = []
       for player in Panthers:
          for key,value in player.items():
            if key =="height":
               val = value
               heightList.append(val)
       print(f"\n Average height:{mean(heightList)}")
  
       list_players = []
       for player in Panthers:
            for key,value in player.items():
              if key =="name":
                 val = value
                 list_players.append(val)        
                 c = ','.join(list_players)
       print(f"\n Players on the Team: \n  {c} ")
   

       guardians_players = []
       for player in Panthers:
          for key,value in player.items():
            if key =="guardians":
              val = value
              guardians_players.append(val)               
              guardian = ','.join(list_players)              
       print(f"\n Guardians: \n  {guardian}")
  

    elif userTeamOption=="b":
       print("\nTEAM:Bandits Stats" )
       print("\n__________________")
       print(f"\n Total players:{len(Bandits)}")    
       print(f"\n Total experienced:{int(len(Bandits)/2)}")
       print(f"\n Total experienced:{int(len(Bandits) /2)}")
       
    heightList = []
    for player in Bandits:
        for key,value in player.items():
          if key =="height":
             val = value
             heightList.append(val)
    print(f"\n Average height:{mean(heightList)}")

    list_players = []
    for player in Bandits:
        for key,value in player.items():
          if key =="name":
             val = value
             list_players.append(val)        
             c = ','.join(list_players)
    print(f"\n Players on the Team: \n  {c} ")
   
    guardians_players = []
    for player in Bandits:
        for key,value in player.items():
          if key =="guardians":
            val = value
            guardians_players.append(val)                   
            guardian = ','.join(list_players)                  
    print(f"\n Guardians: \n  {guardian}")

  else: 
       print("\nTEAM:Warriors Stats" )
       print("\n__________________")
       print(f"\n Total players:{len(Warriors)}")    
       print(f"\n Total experienced:{int(len(Warriors)/2)}")
       print(f"\n Total experienced:{int(len(Warriors) /2)}")
       
       heightList = []
       for player in Warriors:
        for key,value in player.items():
          if key =="height":
             val = value
             heightList.append(val)
       print(f"\n Average height:{mean(heightList)}")

       list_players = []
       for player in Warriors:
        for key,value in player.items():
          if key =="name":
             val = value
             list_players.append(val)        
             c = ','.join(list_players)
       print(f"\n Players on the Team: \n  {c} ")
   

       guardians_players = []
       for player in Warriors:
        for key,value in player.items():
          if key =="guardians":
            val = value
            guardians_players.append(val)                   
            guardian = ','.join(list_players)                  
       print(f"\n Guardians: \n  {guardian}")

if __name__ == '__main__':
  clean_data(PLAYERS)
  div_list(cleaned_data)
  balance_teams()
  start()
