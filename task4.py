good = r'''



                       []
                       ||
                       ||
                       ||
                       ||
                       ||
                       ||
                       ||
                       ||
           [:::::::::::||
                       ||
         _._._._       ||
         I.____________||__________/.___
       ..I|""""""""""""  """"""""""``""/
       I I|                           /
      /  ||________........__________/
     |   |         |      |
     |___|         |      |       anolisa
                    \____/
                    '''

bad = r'''
                          .    .
                             )  (
       _ _ _ _ _ _ _ _ _ _ _(.--.)
     {{ { { { { { { { { { { ( '_')
 jgs  >>>>>>>>>>>>>>>>>>>>>>>`--'>
                '''







guard_awake = False
if not guard_awake:
   outcome = "Shadow: sneak past."
   print(good)
else:
   outcome = "Doom: you got caught."
   print(bad)
print(outcome)
