import random,re
from termcolor import colored

def luck(L='',p='',w='',mesg=''):
    luck_st=colored(f"\n******GOOD LUCK******\n","red")
    places=['Albany','Mt Wellington','Mt Eden','Ponsonby','Auckland-CBD','Handerson','New-lynn','Tapu','NewMarket']
    
    if w=="lotto":
        print(luck_st)
        for i in range(int(L)):
            a=" ".join(sorted(str(i).zfill(2) for i in random.sample(range(1,41),6)))
            if p=="yes":
                print(colored(f"{a} \t   {str(random.randint(1,10)).zfill(2)}","cyan"))
            else:
                print(colored(f"{a}","blue"))
        print(luck_st)
        print(colored(f"{mesg} \n Your Ticket has been sold at {places[random.randint(0,len(places)-1)]}","red",'on_white'))
      

    else:        
        print(luck_st)
        for i in range(int(L)):
                a=" ".join(str(i).zfill(2) for i in random.sample(range(1,41),4))
                print(colored(a,"blue"))
        print(luck_st)
        print(colored(f"{mesg} \n Your Ticket has been sold at {places[random.randint(0,len(places)-1)]}","red",'on_white'))


def balance(name_user):

    def check_balance(balance_user,balance_user_not_accept=None):
        if 199<balance_user:
            print(colored(f'\nPlease {name_user}. Make sure to not excced the limit $200\n{"Also we dont accept amounts like"+balance_user_not_accept+"c" if balance_user_not_accept else ""}' ,"red","on_white"))   
            return balance(name_user) 
        
        elif balance_user<6:
            print(colored(f'\nPlease {name_user}. The top up must be higher than $5\n{"Also we do not accept amounts like"+balance_user_not_accept+"c" if balance_user_not_accept else ""}' ,"red","on_white"))
            return balance(name_user)
        
        elif balance_user_not_accept:
            print(colored(f'\nGood Luck {name_user}.But we will only accept {balance_user}$ we do not accept amounts like {balance_user_not_accept+"c" if balance_user_not_accept else ""}' ,"red","on_white"))
            print(colored(f"Each line of JackPot cost $2 and 1$ for Strike or Lotto ","red",'on_white'))
            return x(name_user,balance_user)
        
    balance_user=input(colored('how much would you like to top up your account \n','red')).strip()

    if balance_user=='':
        print(f'\nplease dont leave it blank {name_user}\n ')
        return balance(name_user)
    
    elif re.findall(r"^[\d]+$",balance_user):
        balance_user=int(balance_user)
        check_balance(balance_user)
              
    elif balance_user.find('.') !=-1 and balance_user.count('.')==1:
        balance_user_not_accept=balance_user[balance_user.index('.'):]  
        balance_user=int(balance_user[:balance_user.index('.')])
        check_balance(balance_user,balance_user_not_accept)
        
    else:
        print('\nplease onlt type number')
        return balance(name_user)
    
    print(colored(f"Good Luck {name_user.upper()} - your balance is {balance_user}$",'red','on_white'))
    print(colored(f"Each line of JackPot cost $2 and 1$ for Strike or Lotto ","red",'on_white'))
    return x(name_user,balance_user)             
             
                
def name_user():
    name_user=input(colored('what is your name \n','red')).strip()
    while name_user=='' or re.findall(r"[\d\W]",name_user):
        if name_user=='':
            print(colored("Please don't leave it blank",'red','on_white'))
        else:
            print(colored("Please type only letters!",'red','on_white'))    
        name_user=input(colored('what is your name \n','red',"on_white"))
    return balance(name_user)
            

def strike(balance):
    which="stike"
    lines= balance
    power=None
    mesg=colored(f"you will #{lines}LINES of STRIKES \n",'red')
    return luck(lines,power,which,mesg)    


def lotto(balance):
    which="lotto"
    power=input(colored(f"are you keen for a jakpot ? yes or no \n",'red',"on_white")).lower()
    if power =='yes' or power=='y':
        if balance %2==0:
            lines=int(balance/2)
            mesg=f"you have #{lines} LINES of jackpot draw!"
            return luck(lines,power,which,mesg)     
        else:
            balance-=1
            lines=int(balance/2)
            mesg=f'''you have #{lines} LINES of jackpot draw! 
            please note that your balance now is 1$'''
            return luck(lines,power,which,mesg)      
    else:
        power='no'
        lines= int(balance)
        mesg=f"you have #{lines} LINES of {which} draw!"
        return luck(lines,power,which,mesg)                



def x(name,balance):
    
    which=input(colored('\nDo you want lotto or strike ?\n','red',"on_white").capitalize()).lower()
    
    while which=='' :
            print(colored(f'please {name.upper()} Either type lotto or strike. thank you :)',"red","on_white"))    
            which=input(colored('\n do you want lotto or strike ?\n','red','on_white').capitalize()).lower()
    
    if which != 'lotto' and which!='strike':           
        like_strike=re.search(r"[strike]{,10}",which).group()
        like_lotto=re.search(r"[lto]{,10}",which).group()    
        answers=['y','yes','ys']
        
        if like_strike  or like_lotto :          
            ask=input(colored(f"Do you mean {'strike' if like_strike else 'lotto' } ? Yes or No ?\n",'red','on_white')).lower()
            while ask=="":
                    print(f'Dear {name.upper()} please make sure to type Yes or No...') 
                    ask=input(colored(f"Do you mean {'strike' if like_strike else 'lotto' } ? Yes or No ?\n",'red',"on_white")).lower()       
            else:
                if ask not in answers:
                    print(colored(f'I think you change your mind{name.upper()} ....let us strat from begin!',"red","on_white"))
                    return x(name,balance) 
                else:
                    if like_strike: 
                        return strike(balance)
                    else:
                        return lotto(balance)    
        else:
            print(colored(f'I can not understand that {name.upper()} ....let us strat from begin!',"red","on_white"))
            return x(name,balance)                  
        
    else:                     
        if which=="lotto":
            return lotto(balance)
            
        else:
            return strike(balance)            
            
name_user()
