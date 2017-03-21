# 第二次作业

## Mesos组成结构

Mesos主要由以下几部分组成：

### 1.Master

Master是整个系统的核心，负责整个系统资源的管理、分配和调度。Master负责管理各个Agent(Slave)的资源，并分配给在系统上运行的各个Framework。Master实时更新各个Agent(Slave)的资源信息，并负责分配给各个Framework。

Master部分的代码主要在src/master目录下。

### 2.Agent(Slave)

Agent(Slave)负责为系统上运行的任务在本机分配固定的资源，这一过程以容器的方式完成。同时，Agent(Slave)还要实时地将本机的可用资源情况报告给Master。

Agent(Slave)部分的代码主要位于src/slave目录下。

### 3.Framework

Framework是指由用户提供的外部计算框架。

Framework的scheduler模块向Master注册并申请资源，之后，Master向scheduler返回当前系统的最大可用资源。Scheduler接受后，向Master返回要执行的任务和每个任务所需要占用的资源。之后，Master再通知各个Agent分配资源给Framework的executor。

总的来说，Framework分为两部分，即scheduler和executor。Scheduler负责资源的申请、Framework内部资源的分配，Executor负责任务的执行。

### 4.Zookeeper

Zookeeper用于管理多个Master，并保证在Master宕机后启用备用Master，确保了系统的可用性。

这部分代码主要位于src/zookeeper目录下。

## 工作流程

系统中各个Agent(Slave)会实时地将本机可用的资源报告给Master。Master中维护系统可用资源的列表。当用户提交了新的任务给Framework的时候，Framework按Master提供
的资源总数，为每个任务分配一定数量的资源，并返回给Master
