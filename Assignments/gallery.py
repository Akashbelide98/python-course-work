gallery ={
    1 : "beach.png",
    2 : "birthday.png",
    3 : "selfie.png",
    4 : "party1.png",
    5 : "birthday.png",
    6 : "concert.png",
    7 : "sunset.png",
    8 : "trip1.png"
}
for i in gallery:
   # print(key, value)
   print(f'{i}.{gallery[i]}')

selected_photos=set(map(int,input("Select photos to share:").split(" ")))

print("Sharing the following photos:")
for i in selected_photos:
   if 1<=i<=8:
       print(gallery[i])
   else:
      print(f"Unable to fetch the image{i}")      