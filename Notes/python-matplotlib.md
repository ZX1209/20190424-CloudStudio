## import path...

import matplotlib.pyplot as plt
plt.plot([1,2,3,4])
plt.ylabel('some numbers')
plt.show()



```python

# coding: utf-8
j

# In[3]:


import matplotlib.pyplot as plt
import numpy as np


# In[5]:


x = np.linspace(-10,10,50)
y1 = 2*x+1
y2 = x**2


# In[15]:



plt.figure()
plt.plot(x,y1,label='up')
plt.plot(x,y2,'r--',label='down')

plt.xlim((-1,2))
plt.ylim((-2,3))
plt.xlabel('i am x')
plt.ylabel('i am y')

new_ticks = np.linspace(-1,2,5)
plt.xticks(new_ticks)
'''
plt.yticks(
    [-2,-1.8,-1,1.22,3],
    ['really bad','bad','normal','good','really good']
)
'''

'''
# gca = 'get current axis'
ax = plt.gca()
ax.spines['right'].set_color('none')
ax.spines['top'].set_color('none')
ax.xaxis.set_ticks_position('bottom')
ax.yaxis.set_ticks_position('left')

ax.spines['left'].set_position(('data',0))
ax.spines['bottom'].set_position(('data',0))
'''

plt.show()


# In[17]:


plt.figure()
plt.plot(x,y1,label='up')
plt.plot(x,y2,'r--',label='down')

# 图例
plt.legend()


# In[26]:


# plt.figure()
plt.plot(x,y1,label='up')

x0 = 1
y0 = 2*x0+1

plt.scatter(x0,y0,s=50,color='b')
plt.plot([x0,x0],[y0,10],'k--')

plt.annotate('anotate',xy=(x0,y0))

plt.show()


# In[27]:


n=1024
X = np.random.normal(0,1,n)
Y = np.random.normal(0,1,n)

T = np.arctan2(Y,X)

plt.scatter(X,Y,s=75,c=T,alpha=0.5)

plt.xlim((-1.5,1.5))
plt.ylim((-1.5,1.5))

plt.show()


# In[28]:


'''
for x,y in zip(X,Y):
...pass
'''


# In[36]:


def f(x,y):
    return (1-x/2+x**5+y**3)*np.exp(-x**2-y**2)

n = 256
x = np.linspace(-3,3,n)
y = np.linspace(-3,3,n)

X,Y = np.meshgrid(x,y)

plt.contourf(X,Y,f(X,Y),8,alpha=0.75,cmap=plt.cm.hot)

#C = plt.contourf(X,Y,f(X,Y),8,colors='black',linewidth=0.5)
#plt.clabel(C,inline=True,fontsize=10)
plt.show()


# In[40]:


data = np.linspace(0,1,9)
a = data.reshape(3,3)

plt.imshow(a,interpolation='nearest',cmap='bone',origin='upper')
plt.colorbar()


# In[42]:


from mpl_toolkits.mplot3d import Axes3D

fig = plt.figure()
ax = Axes3D(fig)

X = np.arange(-4,4,0.25)
Y = np.arange(-4,4,0.25)
X,Y = np.meshgrid(X,Y)

R = np.sqrt(X**2+Y**2)

Z = np.sin(R)

ax.plot_surface(X,Y,Z,rstride=1,cstride=1,cmap=plt.get_cmap('rainbow'))
ax.contourf(X,Y,Z,zdir='x',offset=-2,cmap='rainbow')

plt.show()


```











## 动画效果参考

```python
import matplotlib.pyplot as plt
import numpy as np

np.random.seed(19680801)
data = np.random.random((50, 50, 50))

fig, ax = plt.subplots()

for i in range(len(data)):
    ax.cla()
    ax.imshow(data[i])
    ax.set_title("frame {}".format(i))
    # Note that using time.sleep does *not* work here!
    plt.pause(0.1)
```

