# Page 185
for Linux:
#!/bin/sh
echo "user name: "
read name
echo $name

for Windows:
@echo off
echo "User name:"
set /p id=
echo %id%

Top of Page
import subprocess

p = subprocess.Popen(["myscript.bat"],
                     stdout=subprocess.PIPE, stdin=subprocess.PIPE, text=True)
ans = p.stdout.readline()
print("message", ans)
p.stdin.write("mike\n")
ans = p.stdout.readline()
print("message", ans)
as modified at bottom of page
import subprocess

p = subprocess.Popen(["myscript.bat"],
                     stdout=subprocess.PIPE, stdin=subprocess.PIPE, text=True)
ans = p.stdout.readline()
print("message",ans)
p.stdin.write("mike\n")
p.stdin.flush()
ans = p.stdout.readline()
print("message",ans)
