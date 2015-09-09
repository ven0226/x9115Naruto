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

def print_once(s):
    print s

def print_twice(s):
    print s+"\n"+s
    
def do_twice(f,s):
    f(s)
    f(s)
    
def do_four(f,s):
    f(print_once,s)
    f(print_once,s)

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

#print right_justify('bash')
#do_twice(print_twice, 'do_twice_spam')
#do_four(do_twice,'do_four_spam')
#grid(4,4)