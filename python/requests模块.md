当使用requests的get下载大文件/数据时，建议使用使用stream模式。
当把get函数的stream参数设置成False时，它会立即开始下载文件并放到内存中，如果文件过大，有可能导致内存不足。
当把get函数的stream参数设置成True时，它不会立即开始下载，当你使用iter_content或iter_lines遍历内容或访问内容属性时才开始下载。需要注意一点：文件没有下载之前，它也需要保持连接。
	* 
iter_content：一块一块的遍历要下载的内容
	* 
iter_lines：一行一行的遍历要下载的内容


使用上面两个函数下载大文件可以防止占用过多的内存，因为每次只下载小部分数据。
示例代码：

r = requests.get(url_file, stream=True)
f = open("file_path", "wb")
for chunk in r.iter_content(chunk_size=512):
    if chunk:
        f.write(chunk)
