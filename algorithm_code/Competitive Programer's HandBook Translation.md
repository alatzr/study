
# 一、基础知识

### 编程语言
主流竞赛语言为C++，Python和Java。其中C++占比80%左右，Python占比15%左右，而Java占比只有5%左右。

CSP-J/S 和 NOIP均使用C++语言，竞赛环境为C++14标准。

C++ 模板：
```cpp
#include<bits/stdc++.h>
using namespace std;

int main()
{
	// solution code
	// 程序代码
}
```

### 输入和输出
C++使用标准输入输出流 cin 和 cout 进行输入和输出，C语言风格的 scanf 和 printf 也允许在 C++ 中使用。

输入和输出经常包含数字、字符串、空格和换行符等，例如：
```cpp
int a, b;
string x;
cin >> a >> b >> x;
cout << a << " " << b << "\n" << x;
/*
in:
123 456 hello
out:
123 456
hello
*/
```
当数据量很大时（1e5），输入输出有时会成为影响整个代码运行效率的瓶颈，将下面的两行代码写到程序前面可以大大加快输入输出运行效率：
```cpp
int main()
{
	ios::sync_with_stdio(0);
	cin.tie(0);
	// solution code
}
```
换行符 "\n" 的效率要高于 endl，因为 endl 总是会刷新输出缓冲区。另外一种提高输入输出效率的办法是使用 scanf 和 printf，格式如下：
```cpp
int a, b;
scanf("%d%d", &a, &b);
printf("%d %d", a, b);
```
很多时候，程序需要读入包含空格的一整行数据，此时我们可以使用getline函数：
```cpp
string s;
getline(cin, s);
```
若是给定多组数据却没有指明具体数据量，可以使用while循环来读入：
```cpp
while (cin >> x) // 当数据读完即停
{
	// code
}
```
CSP-J/S 和 NOIP 均要求使用文件读写方式进行代码评测，这需要我们掌握下面的文件读写代码，只需将它加入道主函数开头位置：
```cpp
freopen("input.in", "r", stdin);
freopen("output.out", "w", stdout);
```

### 计算机中的数
**整数**
竞赛中用的最多的整数类型是 int，也叫32位整型，值域范围是 $-2^{31}...2^{31}-1$，简单记作$-2·10^9...2·10^9$。很多时候int 不足以存储足够大的数，我们需要使用64位整型 long long，它的值域范围是 $-2^{63}...2^{63}-1$，简单记作$-9·10^{18}...9·10^{18}$。
下面定义了一个long long 类型变量：
```cpp
long long x = 123456789123456789LL;
// LL后缀表示这个数是LL类型
```
注意使用long long 时容易犯的错误：
```cpp
int a = 123456789;
long long b = a*a; // a是int，a*a也默认是int，赋值给b之前就溢出了
cout << b << "\n"; // -1757895751

/*
正确写法：
long long b = (long long)a*a;
*/
```

**取余运算**
我们定义 x mod m 表示 x 除以 m 所得的余数，比如 17 mod 5 = 2，因为 17 = 3·5+2。
很多时候程序要计算的答案 ans 是一个非常大的数，此时一般会要求我们输出 ans % m 作为结果。下面介绍取余运算在加、减和乘法中的变形：
$$
(a+b)\ mod \ m = (a\ mod\ m\ +\ b\ mod\ m)\ mod\ m
$$

$$
(a-b)\ mod \ m = (a\ mod\ m\ -\ b\ mod\ m)\ mod\ m
$$

$$
(a·b)\ mod \ m = (a\ mod\ m\ ·\ b\ mod\ m)\ mod\ m
$$

比如计算n的阶乘取余m的结果：
```cpp
long long x = 1;
for (int i = 2; i <= n; i++)
	x = (x*i) % m;
cout << x % m << "\n";
```
很多时候我们希望余数总是在 0 ~ m-1 之间，但是大多数编程语言（包括c++）在对负数进行取余运算时，得到的结果也是负的，此时需要我们进行额外的操作，以使得余数结果符合我们的需求：
```cpp
x = x % m;
if (x < 0) x += m;
// 正负数通用写法
x = ((x % m) + m) % m; 
```

**浮点数**
竞赛中主要使用64位浮点类型 double，涉及浮点类型的答案计算，都会指定计算精度，比如下面的代码可以保留9位小数：`printf("%.9lf", x)`。
由于浮点数在计算机中是以指数阶码的形式存储，在一些特殊情况下是无法精确表示的，比如下面这段代码：
```cpp
double x = 0.3*3+0.1;
printf("%.20lf", x); //0.99999999999999988898
```
所以在进行浮点数比较的时候，要谨慎使用 `==` 进行比较，更好的办法是设定一个精度 `eps = 1e-9`：
```cpp
const double eps = 1e-9;
if (abs(a-b) < eps)
{
	// a 和 b 相等
}
```

### 精简代码
在竞赛中编写一份精简的代码是必要的，一是可以节省时间，二是增加代码逻辑条理和可读性。

**typedef 类型重命名**

long long 的重命名
```cpp
typedef long long ll;
ll a, b;  // 等同于 long long a, b;
```

一些复杂类型的重命名
```cpp
typedef vector<int> vi;
typedef pair<int,int> pii;
```

**宏定义 define**
宏定义实际上就是字符替换
```cpp
#define x first; // 当代码中遇到x时，被替换为first
#define y second;
```

### 数学知识与符号
数学在竞赛中扮演着十分重要的角色，了解常用的数学公式和数学符号是十分必要的。

**幂指数和对数**

幂指数的运算
$$a^m·a^n = a^{m+n}$$

$$a^{-b} = \frac{1}{a^b}$$

对数的概念和对数运算
设 $a^x = N$，则有 $x = log_a(N)$，读作 log 以 a 为底 N 的对数。比如 $log_2(64) = 6$
在算法竞赛中，一般省略底数2，若无特殊说明，$log(n)$ 均默认底数为2。

对数的运算：
$$log(1) = 0$$

$$log_a(a) = 1$$

$$a^{log_aN} = N$$

$$log_a(b)×log_b(a) = 1$$

$$log_a(a^N) = N$$

$$log_a(MN) = log_aM + log_aN$$

$$log_a(M÷N) = log_aM-log_aN$$

$$log_aM^N = Nlog_aM$$

$$换底公式：log_ax=\frac{log_bx}{log_ba}$$


**求和**

求和符号 $\sum$ ：
$$\sum_{x=1}^{n}x = 1+2+3+...+n = \frac{n(n+1)}{2}
$$

$$\sum_{x=1}^{n}x^2 = 1^2+2^2+3^2+...+n^2 = \frac{n(n+1)(2n+1)}{6}
$$

等差数列的和：
$$S_n = a_1+a_2+...+a_n = \frac{(a_1+a_n)n}{2}
$$

等比数列的和：
$$S_n = a_1+a_2+...+a_n = \frac{a_n·q-a_1}{q-1}
$$

特殊的等比数列：
$$\sum_{x=0}^{n-1}2^x = 1 + 2 + 4 + 8 + ... + 2^{n-1}=2^n-1
$$ 
调和级数的和：
$$\sum_{x=1}^{n}\frac{1}{x}=1+\frac{1}{2}+\frac{1}{3}+...+\frac{1}{n} \le log_2n+1
$$

证明：
$$1+\frac{1}{2}+\frac{1}{3}+\frac{1}{4}+\frac{1}{5}+\frac{1}{6}+\frac{1}{7} \le 1+\frac{1}{2}+\frac{1}{2}+\frac{1}{4}+\frac{1}{4}+\frac{1}{4}+\frac{1}{4}
$$

而 $log_2(n)+1 = 1 + 2·\frac{1}{2} + 4·\frac{1}{4} + ...$   


**数学中的集合概念**
集合是一堆确定的元素，数学中习惯用大写字母和花括号来表示集合：
$$X = \{2,3,5\}$$
没有任何元素的集合叫空集，用 $\emptyset$ 表示，$|S|$ 表示集合 $S$ 的元素个数，比如上述集合 $|X|=3$。

集合之间的关系：

1.属于
若集合 $S$ 包含元素 $x$，写作 $x ∈ S$，否则写作 $x \notin S$，比如对于上面的集合 $X$，有如下关系：
$$
2 \in X \ and\  4  \notin X
$$

2.交集 $A ∩ B$，表示即属于A也属于B的元素的集合
$A=\{1,2,5\}, \ B = \{2,4\}$  则有 $A ∩ B = \{2\}$

3.并集 $A ∪ B$，表示属于A或者属于B的元素的集合
$A=\{1,2,5\}, \ B = \{2,4\}$  则有 $A ∩ B = \{1,2,4,5\}$

4.补集 $\overline{A}$
补集是相对于全集的概念，设全集 $S=\{1,2,3,4,5,6\}, A=\{1,2,3\}$ 则A的补集$\overline{A}=\{4,5,6\}$

5.差集 $A-B$，表示属于A但不属于B的元素的集合
$A=\{1,2,5\}, \ B = \{2,4\}$  则有 $A - B = \{1，5\}$

6.子集
若每个属于$A$ 的元素也属于$S$，则称$A$是$S$的子集，记作$A\subset S$，对于任意集合$S$，$S$有 $2^{|S|}$个子集，比如 $S = \{2,4,7\}$的子集有$2^3$个，分别是：

$$\emptyset,\{2\},\{4\},\{7\},\{2,4\},\{2,7\},\{2,4,7\}$$

**逻辑运算**
逻辑运算的值要么为 true(1)，要么为 false(0)。数学中的逻辑运算符有与（$\wedge$）、或（$\vee$ ）、非（$\neg$）和异或（$\oplus$）。

> 注意C++中的逻辑运算符号与数学中有所区别：与（&&）、或（||）、非（!）、异或（^）。

真值表如下：

| $A$ | $B$ | $\neg$ | $\neg$ | $A\wedge B$ | $A \vee B$ | $A\oplus B$ |
| --- | --- | ------ | ------ | ----------- | ---------- | ----------- |
| 0   | 0   | 1      | 1      | 0           | 0          | 0           |
| 0   | 1   | 1      | 0      | 0           | 1          | 1           |
| 1   | 0   | 0      | 1      | 0           | 1          | 1           |
| 1   | 1   | 0      | 0      | 1           | 1          | 0           |

**函数**
设A和B是两个非空集合，如果存在某种对应关系$f$，对于集合A中的任意一个元素x，在集合B中都存在唯一的一个元素y与之对应，这样的对应关系叫做集合A到集合B的映射，记作：$f:A\to B$ 。我们把非空集之间的映射称为函数，记作$y = f(x), x \in A$。

如 $f(x) = x^2 + 2x + 1$ 就是一个函数。当$x=1$时，$y=f(x)=4$。

$\left \lfloor x \right \rfloor$表示x向下取整，$\left \lfloor 3/2 \right \rfloor=1$

$\left \lceil x \right \rceil$表示x向上取整，$\left \lceil 3/2 \right \rceil=2$

$min(x_1,x_2,...,x_n)$表示求最小值函数，$min(1,2,3)=1$

$max(x_1,x_2,...,x_n)$表示求最大值函数，$max(1,2,3)=3$

> 注意，C++中max和min函数默认传两个参数，若要求多个元素的最大、最小值，需要将所有元素用花括号包起来，如`int min_num = min({1,2,3,4,5});`

## 二、时间复杂度



## 三、排序



## 四、数据结构



## 五、完全搜索 



## 六、贪心



## 七、DP
