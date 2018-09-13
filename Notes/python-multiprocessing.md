`class multiprocessing.Process(group=None, target=None, name=None, args=(), kwargs={}, *, daemon=None)`

os.getpid()

import multiprocessing as mp

processes  =[]

t=mp.Process(target=f,args=(),name='')

t.start()

t.join()

