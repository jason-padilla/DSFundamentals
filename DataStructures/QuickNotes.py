* PRE-IN-POST TRAVERSAL
  - Pre 
    - root, left, right 
    - The parent node gets added first then move left then move right 
  - In 
    - left, root, right 
    - Go to the far left and and begin adding left then root then go right and keep adding left to finally add right 
  - Post 
    - left, right, root 
    - Go to the far left and begin adding left then go right and add right on the way up add root 
  - modified Pre to root, right, left and then reverse is equal to Post. 
  