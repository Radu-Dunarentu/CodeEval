#fizzbuzz

def fb(x,y,n):
	for i in range(1,int(n)+1):            
		print (('' if i%int(x) else 'F') + ('' if i%int(y) else 'B')) or i,
	print

if __name__ == '__main__':
    import sys
    if len(sys.argv) <= 1:
        sys.exit(__doc__)

    dat = None
    try:
        dat = open(sys.argv[1])
        for l in dat.readlines():
            f, b, l = l.split(' ')
            fb(f,b,l)
    except Exception, e:
        sys.exit(e)
    finally:
        if dat:
            dat.close()