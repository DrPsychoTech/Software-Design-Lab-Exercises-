import os
import sys
import fileinput

path = "../public_html"

# construct full file path recursively
file_list = []
for root,d_names,f_names in os.walk(path):
	for f in f_names:
		file_list.append(os.path.join(root, f))

print("file_list : %s" %file_list)

search = ['http://netdna', 'http://fonts', 'http://maxcdn', 'http://getbootstrap', 'http://php',
                'http://tinymce', 'http://wiki.moxiecode', 'http://www.google', 'http://www.apple',
                'http://activex.microsoft', 'http://download.macromedia', 'http://cdn.mathjax'
                'http://code.jquery', 'http://w.sharethis', 'http://s7.addthis',
                'http://ajax.googleapis', 'http://cdn.mathjax', 'http://d3js.org',
                'http://apis.google', 'http://pagead2.googlesyndication']

replace = ['//netdna', '//fonts', '//maxcdn', '//getbootstrap', '//php',
 		'//tinymce', '//wiki.moxiecode', '//www.google', '//www.apple',
 		'//activex.microsoft', '//download.macromedia', '//cdn.mathjax'
 		'//code.jquery','//w.sharethis', '//s7.addthis',
                '//ajax.googleapis','//cdn.mathjax','//d3js.org',
                '//apis.google', '//pagead2.googlesyndication']

if (len(search) != len(replace)) :
	sys.exit("Error: search does not match with replace")

# Loop through files and replace "search" with "replace"
for filename in file_list:
	# exclude img/video files
	if filename.lower().endswith(('.png', '.jpg', '.jpeg', '.gif', '.bak', 
                                      '.mp4', '.ogv', '.mp3', '.ismv', '.ts', '.ismc', '.m3u8', 
                                      '.mov', '.avi', '.dv', '.wmv', '.ogg', '.mkv', '.webm',
                                      '.idx', '.tar', '.gz', '.zip', '.pdf', '.svg', '.bz')):
		continue

	print(filename)
 
	# Read in the file
	with open(filename, 'r') as file :
  		filedata = file.read()

	# Replace the target string
	for i in range(len(search)):
		filedata = filedata.replace(search[i], replace[i])

	# Write the file out again
	with open(filename, 'w') as file:
  		file.write(filedata)