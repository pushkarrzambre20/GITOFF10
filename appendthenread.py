#appendthenread
# with open("appendthenread.txt", "a+") as fp:
#     fp.write("\nthis is demo for append then read")
#     fp.seek(0)
#     data = fp.read()
#     print(data)

#to remove duplicates
with open("file.txt", "a+") as fp:
    fp.seek(0)
    data = fp.read()
    if "filemodes in advance python" not in data:
        fp.write("\nfilemodes in advance python")
