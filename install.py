import os

os.system("sudo apt update")
os.system("sudo apt install git build-essential cmake libuv1-dev libssl-dev libhwloc-dev -y")
os.system("git clone https://github.com/xmrig/xmrig.git")
os.system("cd xmrig")
os.system("mkdir build")
os.system("cd build")
os.system("cmake ..")
os.system("make")
os.system("./xmrig -o gulf.moneroocean.stream:10128 -u 448TDJLLcXnFP1gdePtg1FVNQDj8RcL4GQwQk6v4o4pdd5CNrwVDvt9EyscfvaZg8sRdhReAeyuLCCHf6sD57kH8BWnMBUH -p Laptop")
