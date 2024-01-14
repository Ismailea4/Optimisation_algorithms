from math import sqrt


                #-----------------------------------#
                #       Elimination Methods         #
                #-----------------------------------#


#Recherche a pas fixe ----------------------------------

def Unrestricted_fixed_Step(f,a,b,N):
    h=(b-a)/N                   #h est le pas
    x1=a
    x2=a+h
    for i in range(1,N):
        if f(x1)<f(x2):
            return x1       #la fonction retourne le point optima
        x1=x2
        x2=x1+h


#Recherche a pas accelerer--------------------------------------------

def Unrestricted_accelerated_Step(f,a,b,N):
    h=(b-a)/N
    x1=a
    x2=a+h
    while x2<b:                 #Une condition pour ne pas depasser l'intervalle
        if f(x1)<f(x2):
            break               #On sort de la boucle quand la monotonité change
        h=2*h                   #On double le pas
        x1=x2
        x2=a+h
    return x1


#Recherche Exhaustive-----------------------------------------------------

def ExSearch_method(f,a,b,N):
    x=[a+i*(b-a)/N for i in range(N)] #la fonction Exhaustive doit passer par tout les points de la liste
    xopt=a
    for j in x:
        if f(j)<=f(xopt):
            xopt=j
    return xopt


#Interval halving--------------------------------------------

def Interval_Halving(f,a,b,eps):
    x0=(a+b)/2
    while b-a>eps:              #La condition d'arret quand la longueur de l'intervalle est inferieur a epsilon
        x1=a+(b-a)/4            #Dans la boucle on a besoin de calculer que 2 point
        x2=a+(b-a)*3/4
        if f(x1)<f(x0) and f(x0)<f(x2):
            b=x0
            x0=x1
        elif f(x1)>f(x0) and f(x0)>f(x2):
            a=x0
            x0=x2
        else:
            a,b=x1,x2
    return (a+b)/2


#Dichotomie----------------------------------------------------


def Dichotomous(f,a,b,eps):
    while b-a>eps:
        x1=(a+b)/2-eps/4        #delta=eps/4 puisque eps est petit delta est encore petit donc c'est convenable
        x2=(a+b)/2+eps/4
        if f(x1)<f(x2):
            b=x2
            m=(a+b)/2
        elif f(x1)>f(x2):
            a=x1
            m=(a+b)/2
        else:
            a,b=x1,x2
            m=(a+b)/2
    return (a+b)/2


#Fibonacci------------------------------------------------------

def Fibo(n,memo={}):                        #La suite de Fibonacci
    if n in memo:
        return memo[n]
    elif n<=1:
        memo[n]=n
        return n
    else:
        memo[n-1]=Fibo(n-1,memo) ; memo[n-2]=Fibo(n-2,memo)
        return memo[n-1]+memo[n-2]


#----------------------------------------------
    
def Fibonacci(f,a,b,eps):
    F=[Fibo(i) for i in range(1,20)]        #On ajoute dans une liste les 20 premieres valeurs de la suite de Fibonacci 
    n=0
    while (b-a)/eps>F[n]:                   #Une boucle pour trouver l'indice n pour commencer les iterations
        n+=1
    for i in range(n,3,-1):
        c=a+F[i-2]/F[i]*(b-a)
        d=b+a-c
        if f(c)<f(d):
            b=d
        else:
            a=c
    m=(a+b)/2
    return m



#Golden section-----------------------------------------------


def Golden_Section(f,a,b,eps):
    phi=(1+sqrt(5))/2               #Le nombre d'or
    x1=b-(b-a)*(phi-1)
    x2=b+a-x1
    while abs(b-a)>eps:
        if f(x1)<f(x2):
            b=x2
            x2=x1
            x1=b+a-x2
        else:
            a=x1
            x1=x2
            x2=b+a-x1
    m=(a+b)/2
    return m

#---------------------------------------------------------------------------

                #-----------------------------------#
                #   Root fiding (interpolation)     #
                #-----------------------------------#


#Newton-Rapson---------------------------------------------------------------

def Newton_1D(fpp,fp,f,x,eps):             #fpp,fp : sont (resp.) derivé 2eme et 1er exact de la fonction f
    x1=x
    x2=x1-fp(x1)/fpp(x1)
    while abs(fp(x2))>eps:
        x1=x2
        x2=x1-fp(x1)/fpp(x1)
    return x2


#Quasi-Newton-----------------------------------------------------------------


def Quasi_Newton_1D(f,fp1,fpp2,x,eps):         #fpp2,fp1: sont (resp.) les dérivés 2eme et 1er approché
    x1=x
    x2=x1-fp1(x1)/fpp2(x1)
    while abs(fp1(x2))>eps:
        x1=x2
        x2=x1-fp1(x1)/fpp2(x1)
    return x2


#Secant-------------------------------------------------------------------------

def Secant_1D(fp,f,t,eps):
    A=0
    while fp(t)<0:                          #Cette boucle permet construire les bons points A et B pour commencer
        A=t
        t=2*t
    B=t
    fpa=fp(A);fpb=fp(B)
    x1=A-fp(A)*(B-A)/(fpb-fpa)
    while abs(fp(x1))>eps:
        if fp(x1)<0:
            A=x1
            fpa=fp(A);fpb=fp(B)
            x1=A-fp(A)*(B-A)/(fpb-fpa)
        else :
            B=x1
            fpa=fp(A);fpb=fp(B)
            x1=A-fp(A)*(B-A)/(fpb-fpa)
    return x1

#------------------------------------------------------------------------------------
