l1 = [ "Jean" ]
l2 = []
l2.append ( ( "LINFO1101", l1 ) )
l1.append ( "Charles" )
print ( l2 )

"""
l2 : [( "LINFO1101",["Jean","Charles"])]
l1 est un pointeur vers la liste l1 . Au moment de print python évalue l2 en regardant de nouveau
l1
"""