#!/usr/bin/env python
# coding: utf-8

# ## 인덱싱, 슬라이싱 기본

# In[19]:


arr = np.arange(10)
arr


# In[20]:


arr[5]


# In[21]:


arr[5:8]


# In[22]:


arr[5:8] = 10
arr


# - 파이썬 리스트와 크게 다른점중의 하나는 배열 슬라이스는 새로운 객체를 만드는 것이 아닌 원래 배열에 대한 뷰(view)이다.  
# - 즉 선택 부분의 값을 변경하면 원래 배열의 같은 위치의 값도 변경이 되는 것이다.

# In[23]:


arr_slice = arr[5:8]
arr_slice


# In[24]:


arr_slice[1] = 1234
arr


# - 시작과 끝이 없는 슬라이싱은 모든 원소 선택

# In[25]:


arr_slice[:] = 500
arr


# - 배열의 일부분을 복사해서 사용하려면 copy 메소드 이용

# In[26]:


arr_copy = arr[5:8].copy()
arr_copy


# In[29]:


arr_copy[:] = -100
arr_copy


# In[30]:


arr
#변경되지 않음


# - 고차원 배열

# In[31]:


arr2d = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
arr2d[0]


# In[32]:


arr2d[:2]


# In[33]:


arr2d[:2,1:]


# In[34]:


arr2d[1,1:]


# In[35]:


arr2d[:2,2]


# In[36]:


arr2d[:,:1]


# In[37]:


arr2d[:2,1:] = 0
arr2d


# ### 논리 인덱싱

# In[38]:


names = np.array(['Bob', 'Joe', 'Will', 'Bob', 'Will', 'Joe', 'Joe'])

np.random.seed(0)

data = np.random.randn(7, 4)
data


# In[39]:


names == 'Bob'


# In[40]:


data[names == "Bob"]


# In[41]:


data[names == 'Bob', 2:]


# In[42]:


data[names != 'Bob']


# In[43]:


data[~(names == 'Bob')]


# - 여러 개의 조건을 결합하려면 &(and) 또는 |(or) 연산자를 사용하면 된다. 
# - 주의해야 할 것은 넘파이 논리 연산자로 파이썬 논리 연산자 and와 or를 사용할 수 없다. 반드시 &와 |만 사용해야 한다.

# In[44]:


mask = (names == 'Bob') | (names == 'Will')
mask


# In[45]:


arr_m = data[mask]
arr_m


# - 또한 논리 인덱스를 이용해서 반환된 배열을 **원래 배열의 복사본**이기때문에 반환된 배열값이 바뀌어도 원본값은 변하지 않는다.

# In[46]:


arr_m[:, :2] = 0
arr_m


# In[47]:


data


# In[48]:


data[data < 0] = 0
data


# In[49]:


data[names != 'Joe'] = 7
data


# ### 정수 배열을 이용한 인덱싱

# In[4]:


import numpy as np
arr = np.empty((8,4))

for i in range(8):
    arr[i] = i

arr


# In[5]:


arr[[4,3,0,6]]


# In[7]:


arr[[-4,-3,0,6]]


# #### np.range와 np.arange 의 차이
# 1. range 함수에는 정수 단위만 지원하나, np.arange는 실수 단위도 표현 가능하다.
# 2. range 메소드는 range iterator 자료형을 반환하고, np.arange 메소드는 numpy array 자료형을 반환. 따라서, np.arange 메소드 결과는 넘파이에서 수행하는 연산 연계가 가능
# 3. for 문 등에서 순회하고 싶은 수열이 정수로 구성되어 있다면, range 메소드로 순회하는 것이 수행시간에 있어 조금 더 유리

# In[8]:


arr = np.range(32).reshape(8,4) ## range는 넘파이 연산 연계 불가능
arr


# In[9]:


arr = np.arange(32).reshape(8,4)
arr


# In[10]:


arr[[1,5,7,2], [0,3,1,2]]


# In[11]:


arr[[1, 5, 7, 2]][:, [0, 3, 1, 2]]


# ### 배열 전치 및 축 교환

# In[13]:


arr = np.arange(15).reshape((3,5))
arr


# In[14]:


arr = np.arange(15).reshape(3,5)
arr


# In[15]:


arr.T


# In[16]:


arr.dot(arr.T)


# In[17]:


arr3d = np.arange(2*3*4).reshape((2,3,4))
arr3d


# In[18]:


arr3d.T


# ## 범용함수

# In[19]:


arr = np.arange(10)
arr


# In[20]:


np.sqrt(arr)


# In[21]:


np.exp(arr)


# In[22]:


np.add(arr,arr)


# In[23]:


rng = np.random.RandomState(0)

x = rng.randn(10)
y = rng.randn(10)
x


# In[24]:


y


# In[25]:


np.maximum(x,y)


# In[26]:


arr = rng.randn(7) * 5
arr


# -  modf라는 함수는 정수와 소수부분을 각각 반환한다.

# In[27]:


rem_part, int_part = np.modf(arr)
rem_part


# In[28]:


int_part


# In[29]:


np.sqrt(arr, out=arr)


# In[31]:


arr


# ## 배열 지향 프로그래밍

# - 1차원 자료를 이용해 이차원 계산을 쉽게 할 수 있다. meshgrid 함수를 이용하면 모든 격자점의 x, y 좌표를 계산할 수 있다.

# In[33]:


points = np.arange(-5, 5, 0.01)


# In[34]:


xs, ys = np.meshgrid(points,points)
ys


# In[35]:


xs


# In[36]:


z = np.sqrt(xs**2 + ys**2)
z


# In[37]:


get_ipython().run_line_magic('matplotlib', 'inline')
import matplotlib.pyplot as plt

plt.imshow(z, cmap=plt.cm.gray)
plt.colorbar()
plt.title("Image plot of $\sqrt{x^2 + y^2}$ for a grid of values")

