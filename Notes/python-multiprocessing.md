import multiprocessing as mp



t=mp.Process(target=f,argv=(),name='')

t.start()

t.join()

