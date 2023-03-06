import time, sys, os
os.system('clear')
os.system('cd config')
verde = '\033[0;30;32m'
nulo = '\033[0;30;0m'
vermelho = '\033[0;30;31m'
azul = '\033[0;30;34m'
rosa = '\033[0;30;35m'

print(f'''
{verde}██████╗░░█████╗░██████╗░████████╗{nulo}  {vermelho}░██████╗░█████╗░░█████╗░███╗░░░███╗{nulo}
{verde}██╔══██╗██╔══██╗██╔══██╗╚══██╔══╝{nulo}  {vermelho}██╔════╝██╔══██╗██╔══██╗████╗░████║{nulo}
{verde}██████╔╝██║░░██║██████╔╝░░░██║░░░{nulo}  {vermelho}╚█████╗░██║░░╚═╝███████║██╔████╔██║{nulo}
{verde}██╔═══╝░██║░░██║██╔══██╗░░░██║░░░{nulo}  {vermelho}░╚═══██╗██║░░██╗██╔══██║██║╚██╔╝██║{nulo}
{verde}██║░░░░░╚█████╔╝██║░░██║░░░██║░░░{nulo}  {vermelho}██████╔╝╚█████╔╝██║░░██║██║░╚═╝░██║{nulo}
{verde}╚═╝░░░░░░╚════╝░╚═╝░░╚═╝░░░╚═╝░░░{nulo}  {vermelho}╚═════╝░░╚════╝░╚═╝░░╚═╝╚═╝░░░░░╚═╝{nulo}''')
z = '''BY: SLAYER
creator's github: https://github.com/slayerkk'''
for c in z:
    sys.stdout.write(c)
    sys.stdout.flush()
    time.sleep(0.05)
print('')
escolha = -1

while escolha < 1 or escolha > 5:
    escolha = int(input(f"""
{verde}┌┬┬┬┬┬┬┬┬┬┬┬┬┬┬┬┬┬┬┬┬┬┬┬┬┬┬┬┬{rosa}┬┬┬┬┬┬┬┬┬┬┬┬┬┬┐{nulo}
{verde}├{nulo}{vermelho}[{azul}1{vermelho}] {nulo}{azul}top ports{nulo}               {rosa}|ATUALIZAÇÕES!┤
{verde}├{nulo}{vermelho}[{azul}2{vermelho}] {nulo}{azul}todas as portas{nulo}         {rosa}|Aqui não tem ┤
{verde}├{nulo}{vermelho}[{azul}3{vermelho}] {nulo}{azul}top ports (fast){nulo}        {rosa}|nada, por enq┤
{verde}├{nulo}{vermelho}[{azul}4{vermelho}] {nulo}{azul}todas as portas (fast){nulo}  {rosa}|uanto.       ┤
{verde}├{nulo}{vermelho}[{azul}5{vermelho}] {nulo}{vermelho}sair                   {nulo} {rosa}|             ┤
{verde}└┴┴┴┴┴┴┴┴┴┴┴┴┴┴┴┴┴┴┴┴┴┴┴┴┴┴┴┴{rosa}┴┴┴┴┴┴┴┴┴┴┴┴┴┴┘
\033[0;30;34m┌──(PORT㉿SCAM!)-[~]
└─>\033[0;30;0m """))
    print(''' ''')
    print('')
    print('')

if escolha == 1:
    exec(open('topPort.py', encoding="utf-8").read(), globals())

if escolha == 2:
    exec(open('todasPorts2.py', encoding="utf-8").read(), globals())

if escolha == 3:
    exec(open('ScamPort.py', encoding="utf-8").read(), globals())

if escolha == 4:
    exec(open('todasPorts.py', encoding="utf-8").read(), globals())

if escolha == 5:
    (exit)