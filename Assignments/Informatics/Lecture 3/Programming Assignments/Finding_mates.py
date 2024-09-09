'''
Created on 2016. 9. 14.

@author: korea
'''
Fs = str(input())
Fv = str(input())
Ss = str(input())
Sv = str(input())

Rs = {'diamonds', 'hearts'}
Bs = {'spades', 'clubs'}

if ([Fs, Fv] != [Ss, Sv]) and (Fv==Sv) and (((Fs in Rs) and (Ss in Rs)) or ((Fs in Bs) and (Ss in Bs))) : 
    #I can't handle Fs and SS!
    print('the '+ Fv +' of '+ Fs + ' and the ' + Sv + ' of ' + Ss + ' are mates')
else:
    print('the '+ Fv +' of '+ Fs + ' and the ' + Sv + ' of ' + Ss + ' are not mates')