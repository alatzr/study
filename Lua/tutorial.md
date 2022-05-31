### 一、环境搭建

win10 下 get a binary

![0](../.all_images/lua0.png)

下载后解压，lua53.exe可以改下名字，去掉53，方便添加环境变量后命令行调用：

![image-20220526124129187](../.all_images/image-20220526124129187.png)



配置环境变量：

![image-20220526124216372](../.all_images/image-20220526124216372.png)



### 二、基础语法：

变量名：

数字、字母、下划线，非数字开头。not beginning with a digit.

```lua
--全局变量声明
> b --> nil
> b = 10
> b --> 10

> b = nil
> b --> nil

--数据类型
> type(nil) --> nil
> type(true) --> boolean
> type(10.4 * 3) --> number
> type("Hello world") --> string
> type(io.stdin) --> userdata
> type(print) --> function
> type(type) --> function
> type({}) --> table
> type(type(X)) --> string

```



关键字：

and    break	do	else 	elseif

end	false	for	function	goto

if 	in	local	nil	not	until	while

or	repeat	return	then	ture



注释：

```lua
--单行注释

--[[多行
注释]]
```

算术运算符：

\+ \- \* /  ^ % 

关系运算符：

<  >  <=  >=  ==  ~=

逻辑操作符：

and、or、not

字符串连接：

```lua
print("hello" ... "world")  --> hello world
print(0 ... 1)  --> 01  注意0和.之间要有空格，否则会被视为小数点。
```



随机数生成：math.random()

``` lua
math.random()  -- return real number [0, 1)
math.random(n) -- return real number [1, n]
math.random(l, u) -- return real number [l, u]
```



### 控制语句

if - else

```lua
-- if else
a, b = 1, 2
if a > b then
    print("a > b")
else
    print("a <= b")
end

-- if elseif elseif ... else 
print("input your score!")
score = tonumber(io.read())
if score >= 90 then
    print("A")
elseif score >= 80 then
    print("B")
elseif score >= 70 then
    print("c")
else
    print("D")
end
```

while 循环

```lua
local i = 1
while i < 10 do
    print(i)
    i = i + 1
end
```

repeat-until，相当于do-while,循环体至少执行一次

```lua
repeat
    line = io.read()
until line == ""  -- 持续获取输入，且至少获取一次，直到输入的内容为空停止
print(line)
```

数字型for循环（numeric for）

```lua
--[[
for start, stop, step do
	<loop body>
end
]]

for i = 1, 10, 2 do
    io.write(i, ' ')  --> 1 3 5 7 9
end
```

泛型fo循环（generic for）

```lua
days = {"0","1","2","3","4","5","6"}
rev_days = {}
for k, v in pairs(days) do  -- table<pairs> array<ipairs>
    rev_days[v] = k
end

```

