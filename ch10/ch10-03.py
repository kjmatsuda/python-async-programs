# Page 186
import subprocess
p = subprocess.Popen(["myscript.bat"], stdout=subprocess.PIPE,
                     stdin=subprocess.PIPE, bufsize=0,
                     universal_newlines=True, text=True)

ans = p.stdout.readline()
print("message", ans)
p.stdin.write("mike\n")

ans = p.stdout.readline()
print("message", ans)
