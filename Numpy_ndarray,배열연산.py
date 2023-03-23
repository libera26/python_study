#!/usr/bin/env python
# coding: utf-8

# ### 넘파이 ndarray: 다차원 배열 객체
# - 넘파이의 주요 특징
# - 행렬 연산과 비슷한 연산, 즉 성분별 계산을 할 수 있다.

# In[3]:


import numpy as np
data = np.random.randn(2,3)
data


# In[4]:


10*data


# In[5]:


data+data


# In[6]:


data.dtype


# In[7]:


data.shape


# ### ndarray 만들기
# - numpy.array 메소드로 넘파이 배열을 만들 수 있다.
# - array 메소드는 반복가능 객체를 인자로 받을 수 있으므로 리스트를 배열로 만들 수 있다.

# In[8]:


data1 = [1,2,3.5,4,5]

arr = np.array(data1)
arr


# - 중첩된 리스트도 다차원 배열로 변환할 수 있다.

# In[9]:


data2 = [[1,2,3,4],[5,6,7,8]]

arr2 = np.array(data2)
arr2


# In[12]:


# 변경된 배열의 차원은 ndim으로
arr2.ndim


# In[13]:


arr2.shape


# In[14]:


arr2.dtype


# - 그 외 배열 생성 방법

# In[15]:


np.zeros(10)


# In[16]:


np.ones((2,3))


# In[17]:


# arange 함수의 반환값은 넘파이 배열
np.arange(10)


# In[22]:


np.full((2,3),10)


# In[23]:


np.empty((2,3))


# - 형변환

# <div>
#     <img src="attachment:image.png" width="400"/>
# </div>

# In[4]:


import numpy as np
arr = np.array([1,2,3,4,5])
arr.dtype


# In[5]:


arr_float = arr.astype(np.float64)
arr_float.dtype


# In[6]:


# 부동소수점형을 정수형으로 변경하면 소수점 아래 수들이 사라진다.

arr = np.array([1.2, 3.4, -0.9, -2.1, 100.])
arr_int = arr.astype(np.int32)
arr_int


# In[12]:


# 숫자 문자열로 주어진 배열도 숫자형으로 변경할 수 있다.
# 문자열 객채는 string_ or 'S'
num_str = np.array(['1.234', '-2.29', '1000'], dtype='S') 
num_str = np.array(['1.234', '-2.29', '1000'], dtype=np.string_)
num_str


# In[9]:


num = num_str.astype(np.float)
num.dtype


# ### 넘파이 배열 연산  
#   - 넘파일 배열간의 연산은 반복문을 사용하지 않고서도 내부적으로 연산을 할 수 있다.   
#   - 기본적으로 성분끼리 연산을 하는데 이러한 연산을 벡터화 계산(vectorization)이라고 한다.

# In[13]:


arr = np.array([[1., 2., 3.], [4., 5., 6.]])
arr


# In[14]:


arr*arr


# In[15]:


arr-arr


# In[16]:


1/arr


# In[17]:


arr2 = np.array([[0., 4., 1.], [7., 2., 12.]])
arr2.dtype


# In[18]:


arr<arr2

