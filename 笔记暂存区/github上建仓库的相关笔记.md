## 在GitHub上创建一个专门用于保存算法笔记的新分支：

1. **克隆仓库**： 首先，你需要将GitHub上的仓库克隆到本地。打开终端或命令提示符，然后使用以下命令：

   ```
   git clone [仓库URL]
   ```

   将`[仓库URL]`替换为你的GitHub仓库的实际URL。

2. **切换到新分支**： 克隆完成后，进入仓库的本地目录，然后使用`git checkout`命令创建并切换到新分支：

   ```
   cd [仓库名称]
   git checkout -b algorithm-notes
   ```

   这里的`algorithm-notes`是你想要创建的新分支的名称，你可以根据需要更改它。

3. **添加笔记文件**： 在本地仓库中创建或复制你的算法笔记文件到相应的目录。例如，你可以创建一个名为`notes`的文件夹，并在其中添加你的笔记文件。

4. **提交更改**： 当你添加或修改了文件后，使用`git add`命令将它们添加到暂存区，然后使用`git commit`命令提交更改：

   ```
   git add .
   git commit -m "Add algorithm notes"
   ```

5. **推送分支到GitHub**： 最后，使用`git push`命令将你的新分支推送到GitHub上的远程仓库：

   ```
   git push origin algorithm-notes
   ```

6. **创建Pull Request**（可选）： 如果你的仓库是多人协作的，并且你想要将你的算法笔记分支合并到主分支，你可以在GitHub网站上创建一个Pull Request。这通常涉及到从你的新分支创建一个合并请求到你想要更新的分支（例如`main`或`master`）。

7. **保持分支更新**（可选）： 如果你希望算法笔记分支保持与主分支的同步，你可以定期将主分支的更新合并到你的算法笔记分支：

   ```
   git checkout main  # 或你主分支的实际名称
   git pull
   git checkout algorithm-notes
   git merge main
   git push origin algorithm-notes
   ```

按照这些步骤，你就可以在GitHub上创建一个专门用于保存算法笔记的分支了。记得在推送分支之前，确保你的本地仓库与远程仓库同步，避免潜在的合并冲突。



## .gitignore

```bash
# 排除 IntelliJ IDEA 的文件和文件夹
.idea/
*.iml
*.iws
out/
*.log
*.ipr

# 排除 VS Code 的文件和文件夹
.vscode/
.history/

# 排除 Java 编译生成的 class 文件和相关文件夹
*.class
*.jar
*.war
*.ear
*.dll
*.so
*.exe
target/
bin/

# 排除操作系统相关文件
.DS_Store
Thumbs.db
# 排除Python编译生成的文件
*.spec
dist/
build/
```

