from constants import PLAYERS
from constants import TEAMS
cleaned_data=[]
# print(cleaned_data)

num_players_team=int(len(PLAYERS)/len(TEAMS))
#print(num_players_team)

def clean_data(PLAYERS):
        cleaned=[]
        for player in PLAYERS:
            # print(player)
            fixed={}
            fixed['name']=player['name']
            split_guardians= player['guardians'].split(' and ')
            fixed['guardians']=split_guardians          
            if player['experience']=='YES':
                fixed['experiece'] = True
            else:
                fixed['experience']=False
            split_height = player['height'].split()
            split_height = int(split_height[0])
            fixed['height'] = split_height          
            cleaned.append(fixed)
            cleaned_data.append(cleaned)
            # print(cleaned_data)
            return(cleaned)
clean_data(PLAYERS)
          
           

def balance_teams():
   
  start = 0
  end = len(PLAYERS)    
  step =num_players_team
  for i in range(start, end, step):
    x = i
  div_list=(cleaned_data[x:x+step]) 
  
  print([[*item1, item2,] for item1, item2, in zip(TEAMS, div_list)])



# new_data = []      #optional
# for i,div_list in enumerate(div_list):
#     div_list.append(Teams[i])
#     new_data.append(div_list)

# print(new_data)

    

    


    
    #insert dunder main
#wrap below in a function
    
# while True:    
#     print("BASKETBALL TEAM STATS TOOL ")
#     print("\n")
#     print("----MENU----")
#     print("\n")    
#     print(" Here are your choices:\nA) Display Team Stats \nB) Quit \n")
#     option=input("\nEnter an option  A/B:  ").lower()
#     try:
#         if option=='a':
#             continue             
#             print("\n A) Panthers \n B) Bandits \n C) Warriors")
#             userTeamOption=input("Enter an option A/B/C:  ").lower()
#             try:
#                 if userTeamOption== 'a':
#                     balance_teams()
                   
# #Team: Panthers Stats
# #            --------------------
# #            Total players: 6
# #            Total experienced: 3
# #            Total inexperienced: 3
# #            Average height: 42.5
#     elif option =='b':
#             print("Goodbye!")
#             break
#     except ValueError:
#         print('Oops....choose A or B')
#         continue
           
    
     