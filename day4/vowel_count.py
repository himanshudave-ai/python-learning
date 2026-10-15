while True: 
 text=input("enter your sentence:")
 count=0
 for ch in text.lower():
  if ch in 'aeiou':
    count +=1
    print("vowel:", count)


 