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


                
def info(name=None,balance=None):
        
        name=input(colored('what is your name \n','red')).strip()
    
        while name=='' or re.findall(r"[\d\W]",name):
            if name=='':
                print("Please don't leave it blank")
            else:
                print("Please type only letters!")    
            name=input(colored('what is your name \n','red'))

        def check():
            balance=input(colored('how much would you like to top up your account \n','red')).strip()
            if balance=='':
                print('please dont leave it blank \n')
                return check()
            
            elif re.findall(r"^[\d]+$",balance):
                balance=int(balance)
                if 199<balance:
                    print(colored(f'Please {name}. Make sure to not excced the limit $200' ,"red"))   
                    return check() 
                elif balance<6:
                    print(colored(f'Please {name}. The top up must be higher than $5' ,"red"))
                    return check()          
            
            else:
                print('please onlt type number \n')
                return check()
            
            return balance                           
                    
        balance=check()
        print(f"\n Good Luck {colored(name.upper(),'red')} - your balance is {balance}$ \n")
        print(colored(f"each line of JackPot cost $2 and 1$ for Strike or Lotto ","red",'on_white'))
        return x(name,balance)
    

def strike(balance):
    which="stike"
    lines= balance
    power=None
    mesg=colored(f"you will #{lines}LINES of STRIKES \n",'red')
    return luck(lines,power,which,mesg)    


def lotto(balance):
    which="lotto"
    power=input(colored(f"are you keen for a jakpot ? yes or no \n",'red')).lower()
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
    which=input(colored('\n do you want lotto or strike ?\n','red').capitalize()).lower()
    
    while re.search(r"[^strikelto]*",which).group() or which=='':
            print(f'please {colored(name.upper(),"red")} either type lotto or strike. thank you :)')    
            which=input(colored('\n do you want lotto or strike ?\n','red').capitalize()).lower()
    
    if which != 'lotto' and which!='strike':           
        like_strike=re.search(r"[strike]{,10}",which).group()
        like_lotto=re.search(r"[lto]{,10}",which).group()    
        answers=['y','yes','ys']
        
        if like_strike  or like_lotto :          
            ask=input(colored(f"do you mean {'strike' if like_strike else 'lotto' } ? yes or no ?\n",'red')).lower()
            while ask=="":
                    print(f'Dear {name.upper()} please make sure to type something...') 
                    ask=input(colored(f"do you mean {'strike' if like_strike else 'lotto' } ? yes or no ?\n",'red')).lower()       
            else:
                if ask not in answers:
                    print(f'\n Hmmmm {colored(name.upper(),"red")}. Let start from begin')
                    return x(name,balance) 
                else:
                    if like_strike: 
                        return strike(balance)
                    else:
                        return lotto(balance)    
        else:
            print(f'I can not understand {name.upper()} that....let us strat from begin!')
            return x(name,balance)                  
        
    else:                     
        if which=="lotto":
            return lotto(balance)
            
        else:
            return strike(balance)            
            
info()