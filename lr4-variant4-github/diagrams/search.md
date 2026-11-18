```mermaid
flowchart TD
A([Старт])-->B[lo=0, hi=n-1]-->C{lo<=hi?}
C--Нет-->D[Вернуть -1]
C--Да-->E[mid=(lo+hi)//2]-->F{A[mid]=q?}
F--Да-->G[Вернуть mid]
F--Нет-->H{A[mid]<q?}
H--Да-->I[lo=mid+1]-->C
H--Нет-->J[hi=mid-1]-->C
```