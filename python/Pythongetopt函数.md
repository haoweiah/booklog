getopt函数
opts, args = getopt.getopt(sys.argv[1:], "ho:", ["help", "output="])#"ho:"也可以写成'-h-o:'

python中的getopt.getopt 函数
sys.argv[1:] sys.argv[0]代表的文件的名字
后面的参数ho：也可以写成-h -o这是短格式，后面加：是必须带参数的意思后面的中口号中的是长格式类型，-是短格式，--是长格式，长格式后面加=是必须有参数的意思