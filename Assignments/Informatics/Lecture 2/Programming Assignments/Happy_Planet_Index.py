'''
Created on 2016. 9. 10.

@author: korea
'''
Nation = input()
EW = float(input()) 
LE = float(input())
EF = float(input())

HPI = (EW * LE) / EF

print('The HPI of '+ Nation + ' is ' + ("{:.2f}.".format(HPI))) # "{:.2f}."�� ����/":"�� '���Ǹ� ����'/".2f"�� '.�ڿ� ���ڸ� ������ �Ҽ��� ǥ���ϰڴ�'
