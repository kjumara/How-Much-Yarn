from tkinter import *
from tkinter import ttk
import math 

def yarnWeight(e):
        for item in yardagebyweight:
            if weights.get() == item:
                return 0
        print("Not Applicable")

def sampleWeight():
    if sampleWeightBox.get().isdigit():
        res.config(text="Input Accepted.")
    else:
        res.config(text="This is not an integer. Please try again.")

def stitchNum():
        if stitchnum.get().isdigit():
            sres.config(text="Input Accepted.")
        else:
            res.config(text="This is not an integer. Please try again.")
    
def finRes():
    try:
        x = weights.get()
        ybw = yardagebyweight[x]
        stitches = int(stitchnum.get())
        sampleweight = int(sampleWeightBox.get())
        ypg = ybw/100.00 #yards in one gram
        swg = sampleweight/100.00 #grams in one stitch
        totalyards = swg * ypg * stitches #total yards for the project
        skeinsOfYarn = math.ceil(totalyards/ybw) #most skeins are 100 grams, so this will be how many hundred gram skeins 
        endingstring = "You will need approximately " + str(math.ceil(totalyards)) + " yards of yarn.\nThat would be about " + str(skeinsOfYarn) +" 100 gram skeins of yarn"
        finalAnswer.config(text=endingstring)
    except NameError:
        print("One of the data points is not correctly entered. Please fix and try again.")
        
#Note: This is weight per hundred grams so that needs to be taken into account when doing math
yardagebyweight = {
    "Lace" : 500,
    "Fingering" : 500,
    "Sport" : 190,
    "DK" : 190,
    "Worsted" : 190,
    "Aran" : 140,
    "Bulky" : 100,
    "Super Bulky" : 40,
    "Jumbo" : 5
}

#this list makes it easier to later create a dropdown list of yarn weights
yarnWeights = list(yardagebyweight.keys())

#note to print for user to understand
noteAboutWeight = "Each yarn has a range of yards due to different brands.\nThis calculator is using the lower end of the scale.\nFor Example Lace Weight yarn can be between 500 - 1000 yards per hundred grams, we will be assuming 500 yards.\nThis is due to it being better having too much yarn rather than too little."

#create the frame
root = Tk()
root.title("Yardage of Each Yarn")
root.geometry("500x600")

#create the dropdown for yarn weights
weights = ttk.Combobox(root, value=yarnWeights)
weights.current(0)
weights.pack(pady=20)

#save weight
weights.bind("<<ComboboxSelected>>", yarnWeight)

#amount of colors

#amount of stitches in each color

#weight of 10x10 sample
sampleWeightLabel = Label(root, text="Take a 10x10 stitch sample of the project and weigh it in grams.\nInput the closest integer (round up).")
sampleWeightLabel.pack(pady = 20)

sampleWeightBox = Entry(root)
sampleWeightBox.pack(pady=10)

button = Button(root, text="Sample Weight", command=sampleWeight)
button.pack(pady=5)

res = Label(root, text='')
res.pack(pady=20)

#number of stitches of the particulat color you are working on
stitchnum = Entry(root)
stitchnum.pack(pady=10)

sbutton = Button(root, text="Stitches of Color Being Used", command=stitchNum)
sbutton.pack(pady=5)

sres = Label(root, text='')
sres.pack(pady=20)



#The Last Thing The Program Does, put All information together and finds solution
button2= Button(root, text="Click For Answer", command=finRes)
button2.pack(pady=5)

finalAnswer = Label(root, text='')
finalAnswer.pack(pady=20)

#start
root.mainloop()