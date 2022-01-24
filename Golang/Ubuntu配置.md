虚拟机情况：

桌面一台：alatzr

Server2台：

> ssh ala@192.168.0.102
>
> ssh ala1@192.168.0.104



#### 1.安装网络插件

> sudo apt-get install net-tools

查看ip地址：

> ifconfig -a
>
> ssh server_name @ip

 

#### 2.修改时区

> cp /usr/share/zoneinfo/Asia/Shanghai /etc/localtime

 

#### 3.安装docker

> sudo apt-get install docker.io -y

添加sudo权限到docker：

> sudo usermod -aG docker $USER

 

#### 4.添加阿里源安装kubeadm

> sudo vim /etc/apt/sources.list 

进去后添加下面的阿里源：

> deb https://mirrors.aliyun.com/kubernetes/apt kubernetes-xenial main

保存退出再添加key：

> curl https://mirrors.aliyun.com/kubernetes/apt/doc/apt-key.gpg | sudo apt-key add

先update再安装kubeadm：

> sudo apt-get update
>
> sudo apt-get install kubeadm -y

 

#### 5.初始化kubeadm init

 

 

 

 