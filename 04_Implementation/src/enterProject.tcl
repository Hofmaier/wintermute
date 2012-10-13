package require Tk
label .l1 -text "Projectname"
grid .l1 -column 1 -row 1 
entry .e -textvariable projectname
grid .e -column 2 -row 1
label .l2 -text "projectpath"
grid .l2 -column 1 -row 2
entry .e2 -textvariable projectpath
grid .e2 -column 2 -row 2
button .b1 -text "browse"
grid .b1 -column 3 -row 2
button .b2 -text "cancel"
grid .b2 -column 2 -row 3
button .b3 -text "ok"
grid .b3 -column 3 -row 3