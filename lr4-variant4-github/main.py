"""ЛР4 вариант 4. Булова Екатерина, БИ 2-1."""
import random,time,matplotlib.pyplot as plt
def linear(a,q):
 for i,x in enumerate(a):
  if x==q:return i,i+1
 return -1,len(a)
def binary(a,q):
 l,h,c=0,len(a)-1,0
 while l<=h:
  m=(l+h)//2;c+=1
  if a[m]==q:return m,c
  if a[m]<q:l=m+1
  else:h=m-1
 return -1,c
def interpolation(a,q):
 l,h,c=0,len(a)-1,0
 while l<=h and a[l]<=q<=a[h]:
  if a[l]==a[h]:
   c+=1;return (l,c) if a[l]==q else (-1,c)
  m=l+(q-a[l])*(h-l)//(a[h]-a[l]);c+=1
  if a[m]==q:return m,c
  if a[m]<q:l=m+1
  else:h=m-1
 return -1,c
def lower(a,q):
 l,h=0,len(a)
 while l<h:
  m=(l+h)//2
  if a[m]<q:l=m+1
  else:h=m
 return l
def upper(a,q):
 l,h=0,len(a)
 while l<h:
  m=(l+h)//2
  if a[m]<=q:l=m+1
  else:h=m
 return l
def range_search(a,q):
 x=lower(a,q)
 if x==len(a) or a[x]!=q:return -1,-1,0
 y=upper(a,q)-1
 return x,y,y-x+1
def main():
 sizes=[1000,5000,10000,100000];rng=random.Random(2026);rows=[]
 for n in sizes:
  a=[17+7*i for i in range(n)];qs=[a[rng.randrange(n)] for _ in range(1000)];res={}
  for name,fn in [('Линейный',linear),('Двоичный',binary),('Интерполяционный',interpolation)]:
   t=time.perf_counter();c=0
   for q in qs:c+=fn(a,q)[1]
   res[name]=((time.perf_counter()-t)/len(qs),c/len(qs))
  rows.append(res)
 for n,res in zip(sizes,rows):
  for name,v in res.items():print(n,name,v)
 for q in (2,5,7,3):print('Б4',q,range_search([1,2,2,2,4,5,5,7,7,7,7,9],q))
 for idx,file in [(0,'time.png'),(1,'comparisons.png')]:
  plt.figure()
  for name in ('Линейный','Двоичный','Интерполяционный'):plt.plot(sizes,[x[name][idx] for x in rows],marker='o',label=name)
  plt.xscale('log');plt.yscale('log');plt.grid();plt.legend();plt.savefig(file);plt.close()
if __name__=='__main__':main()
