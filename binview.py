#!/usr/bin/python

if __name__ == '__main__':
    import array
    import sys
    import getopt

    def print_usage():
        print '''
      Utility for viewing data in binary file
        
      Usage: 
        python /path/to/binview.py [OPTIONS]

      OPTIONS:
        -h --help:    List instructions
        -t DATA_TYPE: DATA_TYPE defines data type as consistent as python array:
                      (https://docs.python.org/2/library/array.html)
                      
                      f=float
                      i=singned int
                      I=unsigned int
                      h=signed short
                      H=unsigned short
                      
        -f BIN_FILE:  BIN_FILE is the binary file path
        -s START:     Starting entry for output (default=0, the first value in data)
        -e END:       Ending entry for output (default=-1, the last value in data)
                      -s 0 -e 100, prints data[0], ..., data[99]
    '''

    options, args = getopt.getopt(sys.argv[1:], "ht:f:s:e:", ["help"])

    if len(options) == 0:
        print_usage()

    myargs = {
        'START': 0,
        'END': -1
    }

    for name, value in options:
        if name in ("-h", "--help"):
            print_usage()
            sys.exit(0)
        elif name in ["-t"]:
            myargs['DATA_TYPE'] = value
        elif name in ["-f"]:
            myargs['BIN_FILE'] = value
        elif name in ["-s"]:
            myargs['START'] = int(value)
        elif name in ["-e"]:
            myargs['END'] = int(value)

    if 'DATA_TYPE' not in myargs:
        print_usage()
        sys.exit(1)

    if 'BIN_FILE' not in myargs:
        print_usage()
        sys.exit(1)

    myarr = array.array(myargs['DATA_TYPE'])
    with open(myargs['BIN_FILE'], 'rb') as fp:
        while 1:
            try:
                myarr.fromfile(fp, 1000)
            except EOFError:
                break

    if myargs['END'] == -1:
        myargs['END'] = len(myarr)

    vmin = float('inf')
    i_vmin = None

    vmax = -float('inf')
    i_vmax = None

    minabs = float('inf')
    i_minabs = None

    maxabs = 0.0
    i_maxabs = None

    for i in xrange(myargs['START'], myargs['END']):
        print '[%d] = '%i, myarr[i]

        if myarr[i] < vmin:
            vmin = myarr[i]
            i_vmin = i

        if myarr[i] > vmax:
            vmax = myarr[i]
            i_vmax = i

        if abs(myarr[i]) < minabs:
            minabs = abs(myarr[i])
            i_minabs = i

        if abs(myarr[i]) > maxabs:
            maxabs = abs(myarr[i])
            i_maxabs = i

    print '-'*72
    print 'min = ', vmin, ', i = ', i_vmin
    print 'max = ', vmax, ', i = ', i_vmax
    print 'minabs = ', minabs, ', i = ', i_minabs
    print 'maxabs = ', maxabs, ', i = ', i_maxabs
