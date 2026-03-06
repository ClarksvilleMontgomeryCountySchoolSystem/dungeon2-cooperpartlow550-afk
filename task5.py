good = r'''
  _______
  /\ o o o\
 /o \ o o o\_______
<    >------>   o /|
 \ o/  o   /_____/o|
  \/______/     |oo|
        |   o   |o/
        |_______|/
            '''

bad = r'''
         ,`',   ,,
    `. ':.   ;,'' ;
   :.`.  :_;`  _.'
`'. ':.__;   ,'
   '._':__,-',_)  _,,,
    __." o     """
 ,7"         )
 )   _    ,;'
 `-./ {{{/  (
       {{{   (
ctr     {{
         {
        '''




from task2 import outcome
escaped = True
if escaped:
   outcome = "Legend: you have escaped."
   print(good)
else:
   outcome = "Doom: you got found."
   print(bad)
print(outcome)
