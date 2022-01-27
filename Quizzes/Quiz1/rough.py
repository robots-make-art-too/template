printline = 6
lineCounter = 0
with open('anyTxtFile.txt','r') as f:
    for line in f:
        lineCounter += 1
        if lineCounter == printline:
            print(line, end='')



import getpass
password = getpass.getpass()
print('The password is', password)


import random

random.seed(37)
print(random.random())

#the generator creates a random number based on the seed value, so if the seed value is 10, you will always get 0.5714025946899135 as the first random number.




# use the name lowercase
# match to file line output
# assign random seed as file line number
# random seed 3x -> extract 3 functions
# html element to affect, javascript (sound or image), EMOTION to portray
# write your code, and explain how your code integrates your emotion.
# document in readme.md (how to use your code) and statement.md (how your emotion is invoked)
# git add, commit, and push to your private repo on class organization
# be sure your TA and prof are your repo's team members.
# add harry as a team member


# https://learningsolutionsmag.com/articles/coding-sound-with-javascript-beginner-s-guide

# https://medium.com/@mitchellwstewart_70614/hearing-code-with-tone-js-9e81ded14916

# tone.js
# p5.js
