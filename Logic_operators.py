# # a = "Colleg iof science and technology"
# # print(a[1:9])
# # # this is called slice or slicing \
    
    
# # # to slice from the start
# # print(a[:10])
 
# # #  slicing till the end 
# # print(a[:20])

# # thr starting of count  will be from 0, -1, -2.....goes on (where as -2 and -5 will not be included only the alphbet within the -2 to -5 will be  given in output)
# b = "   Hello, World!"
# print(b.encode())

class Myclass:
    def __init__ (self, values):
        self.values = values
    def __getitem__(self, index):
        return self.values[index]
obj = Myclass([1, 2, 3])
print(obj[1])