'''
#############################
(っ◔◡◔)っ ♥ ＯＳＵ！2 ᴍᴘ3 ♥
#############################
10min script created to listen to doujin music on the go
'''
import os
import sys
import shutil

print('\n(っ◔◡◔)っ ♥ ＯＳＵ！2 ᴍᴘ3 ♥\n')

# Below fill in the path to OSU, you can find this with 'Open current skin folder'
# in OSU options and copying the path to the osu! folder
osu_path = r'C:\Users\ArtoriaPendragon\AppData\Local\osu!'

out_path = r'{}\Music'.format(osu_path)
try:
    mode = 0o666
    os.mkdir(out_path, mode)
except FileExistsError:
    pass
except:
    print("check the osu_path you filled is correct:")
    print(osu_path)
    sys.exit()

map_path = r'{}\Songs'.format(osu_path)
for subdir, dirs, files in os.walk(map_path):
    for filename in files:
        filepath = subdir + os.sep + filename

        if filepath.endswith(".mp3"):
            print(subdir)
            shutil.copy2(filepath, r'{}\{}.mp3'.format(out_path, subdir.split('-')[-1]))

print('\n(っ◔◡◔)っ ♥ ＯＳＵ！2 ᴍᴘ3 ♥')
print("---> your music is available at "+out_path)