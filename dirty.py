#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Feb 2 09:15:12 2024

@author: administrador

D.6BT.R*VA]_D2P1Bz$7V_+!9[16C37N

"""


# Class for array
class V1:
  # Array initialization with values between 0 and 100
  v1 = [i for i in range(0,100)]
  
# Class for array
class V2:
  # Array initialization with values between 100 and 200
  v2 = [i for i in range(100,200)]

# class vggNet(nn.Module):
#     def __init__(self, pretrained=True):
#         super(vggNet, self).__init__()
#         self.net = models.vgg16(pretrained=True).features.eval()

#     def forward(self, x):


#         out = []
#         for i in range(len(self.net)):
#             #x = self.net[i](x)
#             x = self.net[i](x)
#             #if i in [3, 8, 15, 22, 29]:
#             #if i in [15]: #提取1，1/2，1/4的特征图
#             if i in [8,15,22]: #提取1,1/2,1/4,1/8,1/16
#                 # print(self.net[i])
#                 out.append(x)
#         return out

# Class for array
class V3:
  # Array initialization with values between 200 and 300
  v3 = [i for i in range(200,300)]
  
# We declare a variable of the first class and show the content
klsdfsldfj = V1()
print(klsdfsldfj.v1)

# We declare a variable of the second class and show the content
jajaja = V2()
# We print the content of the second class array
print(jajaja.v2)

# We compute the sum of both arrays in order to show how is the result of the sum of the elements of each on of the arrays' elements
r = [e1+e2 for e1,e2 in zip(V1.v1,V2.v2)]
print(r)

# We compute the difference of both arrays in order to show how is the result of the difference of each on of the elements of each on of the arrays' elements
f = [e2-e1 for e1,e2 in zip(V1.v1,V2.v2)]
print(f)

# We compute the mean value of the first array
a = 0
# We make a loop to make the sume of the elements of the first array
for i in range(100): a = a + klsdfsldfj.v1[i]
  
# We print the result of the mean 
print('Mean of the first array: ', a/100)

# We compute the mean value of the second array
b = 0
for i in range(100): b = b + jajaja.v2[i]
  
# We print the result of the mean of the second array 
print('Mean of the second array: ', b/100)

# We compute the maximum and minimum of the first array by iterating the lists
minv = 99999 #We initialize the value of the minimum
maxv = -1
c = g = 0

for i in range(100):
  if(klsdfsldfj.v1[i]>maxv): maxv = klsdfsldfj.v1[i]
  if(klsdfsldfj.v1[i]<minv): minv = klsdfsldfj.v1[i]
  c = c + r[i]
  g = g + f[i]

# We show the results for the maximum and minimum 
print('First array maximum: ', maxv)
print('First array minimum: ', minv)
print('Mean of the array with the sum: ', c/100)
print('Mean of the array with the difference: ', g/100)

# users = [
# 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:90.0) Gecko/20100101 Firefox/90.0',
# 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:89.0) Gecko/20100101 Firefox/89.0',
# 'Mozilla/5.0 (Windows NT 10.0; rv:88.0) Gecko/20100101 Firefox/88.0',
# 'Mozilla/5.0 (Windows NT 6.2; Win64; x64; rv:89.0) Gecko/20100101 Firefox/89.0',
# 'Mozilla/5.0 (Windows NT 6.1; Win64; x64; rv:89.0) Gecko/20100101 Firefox/89.0',
# 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.15; rv:89.0) Gecko/20100101 Firefox/89.0',
# 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.14; rv:88.0) Gecko/20100101 Firefox/88.0',
# 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.13; rv:88.0) Gecko/20100101 Firefox/88.0',
# 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.15; rv:88.0) Gecko/20100101 Firefox/88.0',
# 'Mozilla/5.0 (Macintosh; Intel Mac OS X 11.3; rv:88.0) Gecko/20100101 Firefox/88.0',
# 'Mozilla/5.0 (X11; Linux x86_64; rv:89.0) Gecko/20100101 Firefox/89.0',
# 'Mozilla/5.0 (X11; Linux i686; rv:88.0) Gecko/20100101 Firefox/88.0',
# 'Mozilla/5.0 (X11; Linux x86_64; rv:88.0) Gecko/20100101 Firefox/88.0',
# 'Mozilla/5.0 (Linux x86_64; rv:88.0) Gecko/20100101 Firefox/88.0',
# 'Mozilla/5.0 (X11; Linux i686; rv:88.0) Gecko/20100101 Firefox/88.0',
# 'Mozilla/5.0 (iPhone; CPU iPhone OS 14_5 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) FxiOS/33.0 Mobile/15E148 Safari/605.1.15',
# 'Mozilla/5.0 (iPhone; CPU iPhone OS 11_3 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) FxiOS/33.0 Mobile/15E148 Safari/605.1.15',
# 'Mozilla/5.0 (iPhone; CPU iPhone OS 10_3_2 like Mac OS X) AppleWebKit/603.2.4 (KHTML, like Gecko) FxiOS/7.5b3349 Mobile/14F89 Safari/603.2.4',
# 'Mozilla/5.0 (iPhone; CPU iPhone OS 10_3_2 like Mac OS X) AppleWebKit/603.2.4 (KHTML, like Gecko) FxiOS/7.5b3349 Mobile/14F89 Safari/603.2.4',
# 'Mozilla/5.0 (iPhone; CPU iPhone OS 10_3_2 like Mac OS X) AppleWebKit/603.2.4 (KHTML, like Gecko) FxiOS/7.5b3349 Mobile/14F89 Safari/603.2.4',
# 'Mozilla/5.0 (Android 11; Mobile; LG-M255; rv:88.0) Gecko/88.0 Firefox/88.0',
# 'Mozilla/5.0 (Android 11; Mobile; rv:68.0) Gecko/68.0 Firefox/88.0',
# 'Mozilla/5.0 (Android 11; Mobile; rv:88.0) Gecko/88.0 Firefox/88.0',
# 'Mozilla/5.0 (Android 11; Mobile; rv:87.0) Gecko/87.0 Firefox/87.0',
# 'Mozilla/5.0 (Android 11; Mobile; rv:85.0) Gecko/85.0 Firefox/85.0'
# 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/99.0.4820.0 Safari/537.36',
# 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.110 Safari/537.36',
# 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:95.0) Gecko/20100101 Firefox/95.0',
# 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.110 Safari/537.36',
# 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/94.0.4606.85 YaBrowser/21.11.4.727 Yowser/2.5 Safari/537.36',
# 'Mozilla/5.0 (X11; CrOS x86_64 14268.67.0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.111 Safari/537.36',
# 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_6) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/13.1.2 Safari/605.1.15',
# 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.110 Safari/537.36 OPR/82.0.4227.50',
# 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/97.0.4692.71 Safari/537.36 Edg/97.0.1072.62'
# ]

# We compute the maximum and minimum of the second array by iterating the lists
minv = 99999
maxv = -1
for i in range(100):
  if(jajaja.v2[i]>maxv): maxv = jajaja.v2[i]
  if(jajaja.v2[i]<minv): minv = jajaja.v2[i]

print('Second array maximum: ', maxv)
print('Second array minimum: ', minv)

#We Compute the maximum and minimum of the array with the sum/difference
minv = mind = 99999
maxv = maxd = -1
for i in range(100):
  if(r[i]>maxv): maxv = r[i]
  if(f[i]>maxd): maxd = f[i]
  if(r[i]<minv): minv = r[i]
  if(f[i]<mind): mind = f[i]

print('Maximum of the array with the sum: ', maxv)
print('Minimum of the array with the sum: ', minv)
print('Maximum of the array with the difference: ', maxd)
print('Minimum of the array with the difference: ', mind)
