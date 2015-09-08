#repeat_lyrics()

def repeat_lyrics():
    print_lyrics()
    print_lyrics()

def print_lyrics():
    print "I'm a lumberjack, and I'm okay."
    print "I sleep all night and I work all day."

def right_justify(s):
    rwidth = 70
    print s.rjust(rwidth)

def do_twice(f,val):
    f(val)
    f(val)

def do_four(f,val):
    do_twice(f,val)
    do_twice(f,val)

def print_spam(val):
    print val

def grid(rows,cols):
    for i in range(0,rows):
        print "+",
        for k in range(0,cols):
            for j in range(1,5):
                print "-",
            print "+",
        print
        for a in range(1,5):
            print "/",
            for k in range(0,cols):
                for j in range(1,5):
                    print " ",
                print "/",
            print
    print "+",
    for k in range(0,cols):
        for j in range(1,5):
            print "-",
        print "+",
    print