集中式和分布式版本控制系统有什么区别；

先说集中式版本控制系统，版本库是集中存放在中央服务器的，而干活的时候，用的都是自己的电脑，所以要先从中央服务器取得最新的版本，
然后开始干活，干完活了，再把自己的活推送给中央服务器。中央服务器就好比是一个图书馆，你要改一本书，必须先从图书馆借出来，然后回到家自己改，
改完了，再放回图书馆。

集中式版本控制系统最大的毛病就是必须联网才能工作，如果在局域网内还好，带宽够大，速度够快，可如果在互联网上，遇到网速慢的话，
可能提交一个10M的文件就需要5分钟，这还不得把人给憋死啊。


那分布式版本控制系统与集中式版本控制系统有何不同呢？首先，分布式版本控制系统根本没有“中央服务器”，每个人的电脑上都是一个完整的版本库，
这样，你工作的时候，就不需要联网了，因为版本库就在你自己的电脑上。既然每个人电脑上都有一个完整的版本库，那多个人如何协作呢？
比方说你在自己电脑上改了文件A，你的同事也在他的电脑上改了文件A，这时，你们俩之间只需把各自的修改推送给对方，就可以互相看到对方的修改了。

和集中式版本控制系统相比，分布式版本控制系统的安全性要高很多，因为每个人电脑里都有完整的版本库，某一个人的电脑坏掉了不要紧，
随便从其他人那里复制一个就可以了。而集中式版本控制系统的中央服务器要是出了问题，所有人都没法干活了。

在实际使用分布式版本控制系统的时候，其实很少在两人之间的电脑上推送版本库的修改，因为可能你们俩不在一个局域网内，
两台电脑互相访问不了，也可能今天你的同事病了，他的电脑压根没有开机。因此，分布式版本控制系统通常也有一台充当“中央服务器”的电脑，
但这个服务器的作用仅仅是用来方便“交换”大家的修改，没有它大家也一样干活，只是交换修改不方便而已。



当然，Git的优势不单是不必联网这么简单，后面我们还会看到Git极其强大的分支管理，把SVN等远远抛在了后面。

CVS作为最早的开源而且免费的集中式版本控制系统，直到现在还有不少人在用。由于CVS自身设计的问题，会造成提交文件不完整，
版本库莫名其妙损坏的情况。同样是开源而且免费的SVN修正了CVS的一些稳定性问题，是目前用得最多的集中式版本库控制系统。

除了免费的外，还有收费的集中式版本控制系统，比如IBM的ClearCase（以前是Rational公司的，被IBM收购了），特点是安装比Windows还大，
运行比蜗牛还慢，能用ClearCase的一般是世界500强，他们有个共同的特点是财大气粗，或者人傻钱多。

微软自己也有一个集中式版本控制系统叫VSS，集成在Visual Studio中。由于其反人类的设计，连微软自己都不好意思用了。

分布式版本控制系统除了Git以及促使Git诞生的BitKeeper外，还有类似Git的Mercurial和Bazaar等。这些分布式版本控制系统各有特点，
但最快、最简单也最流行的依然是Git！

1.创建版本库：

在电脑本地，指定一个你喜欢的文件夹，输入pwd查看文件路径，然后在你喜欢的路径下面输入 git init + pwd显示的路径，
这时电脑会提醒你Initialized empty Git repository in /Users/michael/learngit/.git/
这是一个空仓库，在/Users/michael/learngit/.git/里面
然后touch +文件名创建一个文件，  例： touch readme.txt（创建一个txt文档）
然后vi + 文件名编辑文件，
在文件内输入 ：Git是一个版本控制系统。然后保存。
然后使用命令 git add + 文件名 把文件添加到仓库内（暂存区）。
输入后无任何显示，就说明已经添加进去了
然后输入 git commit -m "" ， ""内添加你这次提交的说明，把内容进行提交，提交到仓库内。
然后显示

[master (root-commit) eaadf4e] wrote a readme file
1 file changed, 2 insertions(+)     1 file changed：1个文件被改动
create mode 100644 readme.txt       1 insertions：插入了一行内容

类似于这样的字段 说明提交成功

为什么需要git add  和 git commit 两个步骤：
因为git commit 可以一次提交多个文件，，所以你可以多次使用git add添加不同的文件，
然后使用git commit 一次性把多个文件一起提交。

输入git add readme.txt，得到错误：fatal: not a git repository (or any of the parent directories)。

Git命令必须在Git仓库目录内执行（git init除外），在仓库目录外执行是没有意义的。

输入git add readme.txt，得到错误fatal: pathspec 'readme.txt' did not match any files。

添加某个文件时，该文件必须在当前目录下存在，用ls或者dir命令查看当前目录的文件，看看文件是否存在，或者是否写错了文件名。

总结： 初始化一个git仓库：git init
      添加文件到git仓库需要两步:1、git add 《文件名》、
                            2、git commit -m "《提交说明》"。

不断的对文件进行修改，不断的提交到版本库内，就相当于玩rpg游戏，每当你游戏进行到一定进度你就可以保存，如果失败了还可以在最近的
的位置重新开始。git也是一样,每当你修改到一定程度的时候，就可以使用"commit"去保存这个进度，一旦你把文件内的内容改乱了，还可以
从最近的一个提交中恢复然后继续工作
在版本控制系统内，可以使用git log这个命令来查看我们的历史操作记录

Author: 小刘 <acheng@achengdeMacBook-Pro.local>
Date:   Thu Jun 3 09:01:05 2021 +0800

    list over

commit c16a7acd75879769a8206de642183e7f4f7c4787
Author: 小刘 <acheng@achengdeMacBook-Pro.local>
Date:   Thu Jun 3 08:53:57 2021 +0800

    list over

commit 0d629289f1d24e31440274217bfb314400feca27
Author: 小刘 <acheng@achengdeMacBook-Pro.local>
Date:   Wed Jun 2 16:47:58 2021 +0800

    git介绍&创建本本库

commit 6d98932954a18080be5af5929dd732df0d203155
Author: 小刘 <acheng@achengdeMacBook-Pro.local>
Date:   Tue Jun 1 22:07:12 2021 +0800

git log命令显示从最近到最远的提交日志，我们可以看到3次提交，最近的一次是"list over"，上一次也是"list over"，
最早的一次是  "git介绍&创建本本库"。

如果嫌弃输出信息太多，看的眼花缭乱的，可以试试加上--pretty=oneline参数：

75be0cfcc7d7d784ea092e74e953a7ad25d781ac (HEAD -> master, origin/master) list over  # 这是向github版本库的提交。
c16a7acd75879769a8206de642183e7f4f7c4787 list over
0d629289f1d24e31440274217bfb314400feca27 git介绍&创建本本库

需要注意的是在你看到类似于 75be0cf... 的内容时，这是版本号，和svn不同的是git的版本号不是从1，2，3，递增的数字，而是SHA1计算出来的
一个非常大的16进制的数字，因为git可以同事多人在一个版本库内工作，大家都使用1，2，3这样递增的版本号，那就冲突了

在git里我们可以使用命令来把一个文件回退到上一个版本，
首先我们必须要知道git当前是在哪个版本，如上  我们可以使用git log来查看最近的版本为75be0cf
在git里面用HEAD^来表示回退上一个版本，HEAD^^就是前两个版本，

现在我们使用命令 git reset 来回退版本

git reset --hard HEAD^
会出现一个类似于这样的提示：
HEAD is now at e475afc add distributed

这样我们再使用git log就会发现最新的那个版本已经看不到了，

我们再打开编辑的文件你就会发现，最新更改的文件内容已经不见了；

如果我们还想恢复回去的话，使用命令 git reflog 来查看我们移除的版本号，然后使用 git reset --hard +版本号来进行回滚

总结：
HEAD指向的版本就是当前版本，因此，Git允许我们在版本的历史之间穿梭，
使用命令git reset --hard HEAD^，来回退到上一个版本
使用命令git reset --hard + 版本号，再回到指定的版本
穿梭前，用git log可以查看提交历史，以便确定要回退到哪个版本。
要重返未来，用git reflog查看命令历史，以便确定要回到未来的哪个版本。

版本库（Repository）
工作区有一个隐藏目录.git，这个不算工作区，而是Git的版本库。

Git的版本库里存了很多东西，其中最重要的就是称为stage（或者叫index）的暂存区，还有Git为我们自动创建的第一个分支master，以及指向master的一个指针叫HEAD。

工作区和暂存区：
之前使用了git add  和git commit命令
就是你在电脑里能看到的目录，比如我的git文件夹就是一个工作区：
前面讲了我们把文件往Git版本库里添加的时候，是分两步执行的：

第一步是用git add把文件添加进去，实际上就是把文件修改添加到暂存区；

第二步是用git commit提交更改，实际上就是把暂存区的所有内容提交到当前分支。

因为我们创建Git版本库时，Git自动为我们创建了唯一一个master分支，所以，现在，git commit就是往master分支上提交更改。

你可以简单理解为，需要提交的文件修改通通放到暂存区，然后，一次性提交暂存区的所有修改。

我们可以创建一个新的txt文档随便进行命名。然后修改readme.txt里面的内容
然后使用命令git status来查看当前的状态。
$ git status
On branch master
Changes not staged for commit:
  (use "git add <file>..." to update what will be committed)
  (use "git checkout -- <file>..." to discard changes in working directory)

	modified:   readme.txt

Untracked files:
  (use "git add <file>..." to include in what will be committed)

	LICENSE

no changes added to commit (use "git add" and/or "git commit -a")

Git非常清楚地告诉我们，readme.txt被修改了，而LICENSE还从来没有被添加过，所以它的状态是Untracked。
现在，使用两次命令git add，把readme.txt和LICENSE都添加后，用git status再查看一下：

On branch master
Changes to be committed:
  (use "git reset HEAD <file>..." to unstage)

	new file:   LICENSE
	modified:   readme.txt
现在，暂存区内既有readme.txt 也有LICENSE，这两个文件
所以，git add命令实际上就是把要提交的所有修改放到暂存区（Stage），然后，执行git commit就可以一次性把暂存区的所有修改提交到分支。

一旦提交后，如果你又没有对工作区做任何修改，那么工作区就是“干净”的：
On branch master
nothing to commit, working tree clean


创建分支与合并分支：
git branch +分支名     创建分支
git checkout + 分支名   切换分支
git checkout -b + 分支名  创建一个分支并切换到那个分支
git branch  查看当前分支

* dev
  master
前面有*号的为当前分支
如果我们再dev这个分支里面修改文件内容想要同步到master这个分支里面
使用git merge dev 命令       ==     合并某分支到当前分支
git branch -d + 分支名，为删除分支。
