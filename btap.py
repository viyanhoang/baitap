
import webbrowser

class Song:
	def __init__(self, name, singer, url):
		self.name = name
		self.singer = singer
		self.url = url
		self.seen = False

	def open(self):
		webbrowser.open(self.url)
		self.seen = True

class Playlist:
	def __init__(self, name, songs):
		self.name = name
		self.songs = songs
def read_song():
	name = input("Enter song name: ") + "\n"
	singer = input("Enter song singer: ") + "\n"
	url = input("Enter song url: ") + "\n"
	song = Song(name, singer, url)
	return song

def print_song(song):
	print("Song name: ", song.name, end="")
	print("Song singer: ", song.singer, end="")
	print("Song url: ", song.url, end="")
    

def read_songs():
	songs = []
	total_song = int(input("Enter how many songs: "))
	for i in range(total_song):
		print("Enter song ", i+1)
		song = read_song()
		songs.append(song)
	return songs

def print_songs(songs):
	for i in range(len(songs)):
		print("Song " + str(i+1) + ":")
		print_song(songs[i])

def write_song_txt(song, file):
	file.write(song.name)
	file.write(song.singer)
	file.write(song.url)

def write_songs_txt(songs, file):
	total = len(songs)
	file.write(str(total) + "\n")
	for i in range(total):
		write_song_txt(songs[i], file)

def read_song_from_txt(file):
	name = file.readline()
	singer = file.readline()
	url = file.readline()
	song = Song(name, singer, url)
	return song

def read_songs_from_txt(file):
	songs = []
	total = file.readline()		
	for i in range(int(total)):
		song = read_song_from_txt(file)
		songs.append(song)
	return songs

def read_playlist():
	playlist_name = input("Enter playlist name: ") + "\n"
	playlist_songs = read_songs()
	playlist = Playlist(playlist_name, playlist_songs)
	return playlist

def write_playlist_txt(playlist):
	with open("data.txt", "w") as file:
		file.write(playlist.name)
		write_songs_txt(playlist.songs, file)
	print("Successfully write playlist to txt")

def read_playlist_from_txt():
	with open("data.txt", "r") as file:
		playlist_name = file.readline()
		playlist_songs = read_songs_from_txt(file)
	playlist = Playlist(playlist_name, playlist_songs)
	return playlist

def print_playlist(playlist):
	print("-------")
	print("Playlist name:" + playlist.name, end="")
	print_songs(playlist.songs)
	
def play_song(playlist):
	print_songs(playlist.songs)
	total = len(playlist.songs)

	choice = select_in_range("Select a video (1," + str(total) + "): " , 1,total)
	print("Open video: " + playlist.videos[choice-1].title + " - " + playlist.videos[choice-1].link, end ="")
	playlist.videos[choice-1].open()
def add_playlist(playlist):
	print("Enter new playlist information:")
	new_playlist_name = input("Enter new playlist name")+"\n"
	new_playlist = Playlist(new_playlist_name)
	playlist.name.append(new_playlist)
def add_song(playlist):
	print("Enter new song information:")
	new_song_name = input("Enter new song name: ") + "\n"
	new_song_singer = input("Enter new song singer: ") + "\n"
	new_song_url =  input("Enter new song url: ") + "\n"
	new_song = Song(new_song_name, new_song_singer,new_song_url)
	playlist.songs.append(new_song)
	return playlist

def update_playlist(playlist):
	# Update name
	print("Update playlist?")
	print("Playlist name: ")	
	new_playlist_name = input("Enter new name for playlist: ") + "\n"
	playlist.name = new_playlist_name
	print("Updated Successfully !")
	return playlist

def remove_song(playlist):
	print_songs(playlist.songs)
	choice = select_in_range("Enter song you want to delete: ",1,len(playlist.songs))
	new_song_list = []
	# del playlist.songs[choice-1]
	for i in range(len(playlist.songs)):
		if i == choice-1:
			continue
		new_song_list.append(playlist.songs[i])

	playlist.songs = new_song_list

	print("Delete Successfully !!!")
	return playlist
def remove_playlist(playlist):
	print_playlist(playlist.name)
	choice = select_in_range("Enter playlist you want to delete: ",1,len(playlist.name))
	new_playlist=[]
	for i in range (len(playlist.name)):
		if i == choice-1:
			continue
		new_playlist.append(playlist.name[i])
	playlist.name = new_playlist
def show_menu():
	print("Main Menu:")
	print("-----------------------------")
	print("| Option 1: Show playlist    |")
	print("| Option 2: Create playlist  |")
	print("| Option 3: Remove playlist  |")
	print("| Option 4: Update playlist  |")
	print("| Option 5: Add a song       |")
	print("| Option 6: Remove song      |")
	print("| Option 7: Play a song      |")
	print("| Option 8: Save and Exit    |")
	print("-----------------------------")

def select_in_range(prompt, min, max):
	choice = input(prompt)
	while not choice.isdigit() or int(choice) < min or int(choice) > max:
		choice = input(prompt)

	choice = int(choice)
	return choice

def main():
	try:
		playlist = read_playlist_from_txt()
		print("Loaded data Successfully !!!")
	except:
		print("Welcome first user !!!")		

	while True:
		show_menu()
		choice = select_in_range("Select an option (1-8):", 1, 8)
		if choice == 1:
			print_playlist(playlist)
			input("\nPress Enter to continue.\n")
		elif choice == 2:
			playlist = read_playlist()	
			input("\nPress Enter to continue.\n")	
		elif choice == 3:
			playlist = remove_playlist(playlist)	
			input("\nPress Enter to continue.\n")	
		elif choice == 4:
			playlist = update_playlist(playlist)	
			input("\nPress Enter to continue.\n")
		elif choice == 5:
			playlist = add_song(playlist)	
			input("\nPress Enter to continue.\n")
		elif choice == 6:
			playlist = remove_song(playlist)	
			input("\nPress Enter to continue.\n")
		elif choice == 7:
			play_song(playlist)	
			input("\nPress Enter to continue.\n")
		elif choice == 8:
			write_playlist_txt(playlist)
			input("\nPress Enter to continue.\n")	
			break
		else:
			print("Wrong Input, Exist.")
			break
			
main()
