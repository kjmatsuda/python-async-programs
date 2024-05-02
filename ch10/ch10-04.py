# Page 189
import subprocess
import threading


class AsyncReader():
    def __init__(self, stream):
        self._stream = stream
        self._char = ""
        self.t = threading.Thread(target=self._get, daemon=True)
        self.t.start()

    def get(self):
        self.t.join(0.04)
        if self.t.is_alive():
            return ""
        else:
            result = self._char
            self.t = threading.Thread(target=self._get, daemon=True)
            self.t.start()
            return result

    def _get(self):
        self._char = self._stream.read(1)

    def readmessage(self):
        ans = ""
        while True:
            char = self.get()
            if char == "":
                break
            ans += char
        return ans


p = subprocess.Popen(["myscript.bat"],
                     stdout=subprocess.PIPE, stdin=subprocess.PIPE, bufsize=1, universal_newlines=True, text=True)

aRead = AsyncReader(p.stdout)

ans = aRead.readmessage()

print("message", ans)
p.stdin.write("mike\n")

ans = aRead.readmessage()
print("message", ans)
