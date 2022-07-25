# module
import os
import marshal

os.system("clear")
py = input("File > ")
baca = open(file, "r").read()
com = compile(baca, "", "exec")
encrypt = marshal.dumps(com)
baru = open("enc"+str("py"), "w")
baru.write("import marrshal\n")
baru.write("exec(marshal_loads("+repr(encrypt)+"))")
print("Succes Encrypt | file name save as_ "+str(py))
