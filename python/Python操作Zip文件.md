 Python操作Zip文件
Python操作Zip文件

需要使用到zipfile模块
读取Zip文件

随便一个zip文件，我这里用了bb.zip，就是一个文件夹bb，里面有个文件aa.txt。

```
import zipfile

# 默认模式r,读
azip = zipfile.ZipFile('bb.zip')  # ['bb/', 'bb/aa.txt']
# 返回所有文件夹和文件
print(azip.namelist())
# # 返回该zip的文件名
print(azip.filename)

# 压缩文件里bb文件夹下的aa.txt
azip_info = azip.getinfo('bb/aa.txt')
# 原来文件大小
print(azip_info.file_size)
# 压缩后大小
print(azip_info.compress_size)

# 这样可以求得压缩率，保留小数点后两位
print('压缩率为{:.2f}'.format(azip_info.file_size/azip_info.compress_size))
```
可以看到打开方式并不是想象中的open，而是ZipFile。用namelist()可以返回里面所有的文件夹和文件路径。getinfo可以获得某路径下文件的信息，如上。

还能直接读取压缩包里文件的内容，下面两种方法得到的结果是一样的。需要注意的是，读取出来的数据好像是字节形式的，解码成utf-8就好。
```
# 可以直接读取里面的内容, 不过貌似是字节形式.需要解码回utf-8.参数也可以传ZiInfo, 如b
a = azip.read('bb/cc.txt').decode('utf-8')
print(a)
# 打开文件再读取，好像比上面麻烦
b = azip.open(azip_info)
print(b.read().decode('utf-8'))
azip.close()
```
用完资源后记得主动close。
解压Zip

最为关键的功能，一句搞定。默认解压在当前工作目录，可以指定解压目录。

`azip.extractall()`

新建Zip文件

不仅能读还能写。新建压缩包的时候，可以选择压缩算法，比如DEFLATED和LZMA
```
# 新建压缩包，放文件进去,若压缩包已经存在，将覆盖。可选择用a模式，追加
azip = zipfile.ZipFile('bb.zip', 'w')
# 必须保证路径存在,将bb件夹（及其下aa.txt）添加到压缩包,压缩算法LZMA
azip.write('D:/bb/aa.txt', compress_type=zipfile.ZIP_LZMA)
# 写入一个新文件到压缩包中，data是该文件的具体内容，可以是str或者是byte。
# 这里是新建一个bb文件夹，其下再新建一个cc.txt,将hello world写入到文本中
azip.writestr('bb/cc.txt', data='Hello World', compress_type=zipfile.ZIP_DEFLATED)
# 关闭资源
azip.close()
```
上面有两个方法比较类似，注意区分。

    write指的是将已经存在的文件复制到压缩包，包括路径中的所有文件夹河其下的文件。
    writestr是直接在压缩包里新建文件夹和文件，data参数是往该文件中写入的内容。

最终压缩包里会被添加bb文件夹，其下有aa.txt和cc.txt
将整个文件夹添加到压缩包中

如果我们这样写，想象着能添加bb文件夹下所有内容到压缩包中，那就不对了。这样添加，只会把bb文件夹复制过去，也仅仅如此，里面的文件不会添加到压缩包。最后得到的只是一个空文件夹。

azip.write(r'D:/bb', compress_type=zipfile.ZIP_LZMA)

那怎么办呢？只好递归查找添加了，os.walk刚好可以帮助我们。
```
for current_path, subfolders, filesname in os.walk(r'D:\bb'):
    print(current_path, subfolders, filesname)
    #  filesname是一个列表，我们需要里面的每个文件名和当前路径组合
    for file in filesname:
        # 将当前路径与当前路径下的文件名组合，就是当前文件的绝对路径
        azip.write(os.path.join(current_path, file))
# 关闭资源
azip.close()
```
正确选用变量，元组中第一个是当前路径，而第三个是当前路径下的文件，两者一组合刚好就是文件的绝对路径。

这样就可以实现添加整个文件夹添加到压缩包了。而且是这些路径下所有的文件夹和其下的文件全部添加。也就是说，保留了原文件夹的结构层次。
shutil添加压缩包和解压缩

shuitl模块有个函数，可以方便地添加整个整个文件夹到压缩包。
```
# 第一个参数是归档文件名称，第二个参数是指定的格式，不仅是支持zip，第三个参数是要压缩文件/文件夹的路径
shutil.make_archive('archive_name', 'zip', r'F:\IDE Setting')
# shutil.get_archive_formats() 可以查看支持的格式
```
当然也可以解压缩，可指定解压目录，否则默认解压到当前工作目录。

`shutil.unpack_archive(r'D:\bb.zip')`
