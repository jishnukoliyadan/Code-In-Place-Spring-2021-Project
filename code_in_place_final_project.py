'''
This program is designed to test the user’s knowledge of the 4 main components
of the Refrigeration Cycle.
The program assumes the user already has a basic knowledge of the Refrigeration
Cycles and also gives a few hits as refresher. This could be useful in the study
of Refrigeration and Air-conditioning.

The program begins with instructions, a refresher to the Refrigeration cycle
and an image of the basic refrigeration cycle diagram with components as colored.
The user is then asked to label the diagram by it’s colour in the image.
If answered correctly, a new image popups highlighting that component with it’s
label, and the user will not be asked again to label that component. If incorrect,
it shows the entry is incorrect and the user will try again with a newrandom
component. Once all the components have been labeled correctly, the program will
end by greeting wishes Or if the user types “Done” at any point.

Ways to improve program:
-----------------------------------
Many things can be added to the highlighting components (using 2 or 3 words,like
for Condenser -- Heat Rejection, Evaporator -- Removed Heat,…)

The program is optimised for the users Case sensitivity:
-------------------------------------------------------------------------
The user input will automatically convert to Title format.
If the user input is “condenser”, the program will automatically convert to
“Condenser” as a standard format used in the program for ease of execution.
'''

from simpleimage import SimpleImage
import random
from PIL import Image, ImageDraw, ImageFont
import sys

R_CYCLE = 'refrigeration_cycle.jpg'

def main():
    print('''\n\nInstructions
------------
1. You will be asked to label a colored region of one of the components.
2. Please enter the name of the Component correctly.
3. If required use the below hits for a refresher or as a reference.
4. OR type "End" at any point of time to stop the program.
          ''')
    print('''Refrigeration Cycle
-------------------
A refrigeration cycle's mission is heat absorption and heat rejection.
This is accomplished by manipulating the pressure of the working
refrigerant (air, water, synthetic refrigerants, etc.) through a
cycle of compression and expansion.

Here are the 4 main components and identfy each one in diagram
--------------------------------------------------------------
1. Compressor :Piece of equipment that increases the pressure of 
                working gas.
2. Condenser : Removes heat from the hot refrigerant vapor gas vapor
                until it condenses into a saturated liquid state.
3. Thermal Expansion Valve : Reduces the temperature of the refrigerant
                as passes through.
4. Evaporator : A device used to turn the liquid form of a refrigerant
                into its gaseous-form.''') # refresher to Refrigeration Cycle
    main_parts = ['Condenser', 'Thermal Expansion Valve','Evaporator','Comperssor']
    colors_ = ['Red','Orange', 'Green','Blue']
    user_input =input('Press Enter after to see the Refrigeration Cycle Diagram.')
    if user_input=='':
        image = SimpleImage(R_CYCLE)
        image.show()  # showing original image for users
    
    while colors_: # loop runs till the colors_ are not empty
        image = SimpleImage(R_CYCLE)
        random_colr =random.choice(colors_)
        user_input = input('Which components the '+random_colr + ' represents ?')
                                                        # asks for user entey
        if user_input.title() == 'End':
            print('\nThanks for participating. Good Day !')
            break # giving user to stopng execution of the program
        if random_colr == 'Red':
            colors_ = colour_is_red(user_input,image,colors_)
        if random_colr == 'Green':
            colors_ = colour_is_green(user_input,image,colors_)
        if random_colr == 'Orange':
            colors_ = colour_is_orange(user_input,image,colors_)
        if random_colr == 'Blue':
            colors_ = colour_is_blue(user_input,image,colors_)
    if not colors_:
        print("\nCongrats! You're mastered components of the refrigeration cycle.")

def colour_is_red(user_input,image,colors_):
    '''
    Function takes inputs user entry, image 'refrigeration_cycle.jpg' and list of colors.
    Checks user input and compoent name is correct or not. If correct calling another
    function 'correct_red(image)' to hithlight the specific part. Saving that returned
    image from 'correct_red(image)' to a specific name.
    Using that edited image for labeling the component's name and shows it to user.
    The function will also remove the color 'Red' from the list of colors_ to ensure
    non-repeating the color once again.
    '''
    correct_anz = 'Condenser'
    if user_input.title()==correct_anz:
        print('Correct')
        red_image = correct_red(image) #Calling ocrrect_red() for editing
        red_image.pil_image.save('condenser_red.jpg') #Saving the edited version of image
        image = Image.open('condenser_red.jpg') #Opening the edited image 
        draw = ImageDraw.Draw(image) #Allows program to add text over edited image
        text = 'Condenser' #Creating a text label to print over the edited image
        font = ImageFont.truetype('Aller_Bd.ttf',25) #Choosing a font and font size
                                            #need ot download ttf font externally
        #draw.text((x,y),text_to-print, font_color, choose_a_font)
        draw.text((350,147), text, fill='black',font=font)
        image.show() #Showing the edited image after labeling
        colors_.remove('Red') #Removes Red color from list of colors_ for not to repeat again
        return colors_
    else:
        print('Incorrect.')
        return colors_

def colour_is_green(user_input,image,colors_):
    '''
    Function takes inputs user entry, image 'refrigeration_cycle.jpg' and list of colors.
    Checks user input and compoent name is correct or not. If correct calling another
    function 'correct_red(image)' to hithlight the specific part. Saving that returned
    image from 'correct_red(image)' to a specific name.
    Using that edited image for labeling the component's name and shows it to user.
    The function will also remove the color 'Green' from the list of colors_ to ensure
    non-repeating the color once again.
    '''
    correct_anz = 'Evaporator'
    if user_input.title()==correct_anz:
        print('Correct')
        green_image = correct_green(image)
        green_image.pil_image.save('evaporator_green.png')
        image = Image.open('evaporator_green.png')
        draw = ImageDraw.Draw(image)
        text = 'Evaporator'
        font = ImageFont.truetype('Aller_Bd.ttf',25)
        draw.text((350,470), text, fill='black',font=font)
        image.show()
        colors_.remove('Green')
        return colors_
    else:
        print('Incorrect.')
        return colors_

def colour_is_blue(user_input,image,colors_):
    '''
    Function takes inputs user entry, image 'refrigeration_cycle.jpg' and list of colors.
    Checks user input and compoent name is correct or not. If correct calling another
    function 'correct_red(image)' to hithlight the specific part. Saving that returned
    image from 'correct_red(image)' to a specific name.
    Using that edited image for labeling the component's name and shows it to user.
    The function will also remove the color 'Blue' from the list of colors_ to ensure
    non-repeating the color once again.
    '''
    correct_anz = 'Thermal Expansion Valve'
    if user_input.title()==correct_anz:
        print('Correct')
        blue_image = correct_blue(image)
        blue_image.pil_image.save('thermalEV_blue.png')
        image = Image.open('thermalEV_blue.png')
        draw = ImageDraw.Draw(image)
        text = 'Thermal\nExpansion\nValve'
        font = ImageFont.truetype('Aller_Bd.ttf',25)
        draw.text((175,275), text, fill='black',font=font)
        image.show()
        colors_.remove('Blue')
        return colors_
    else:
        print('Incorrect.')
        return colors_

def colour_is_orange(user_input,image,colors_):
    '''
    Function takes inputs user entry, image 'refrigeration_cycle.jpg' and list of colors.
    Checks user input and compoent name is correct or not. If correct calling another
    function 'correct_red(image)' to hithlight the specific part. Saving that returned
    image from 'correct_red(image)' to a specific name.
    Using that edited image for labeling the component's name and shows it to user.
    The function will also remove the color 'Orange' from the list of colors_ to ensure
    non-repeating the color once again.
    '''
    correct_anz = 'Compressor'
    if user_input.title()==correct_anz:
        print('Correct')
        orange_image = correct_orange(image)
        orange_image.pil_image.save('compressor_orange.png')
        image = Image.open('compressor_orange.png')
        draw = ImageDraw.Draw(image)
        text = 'Compressor'
        font = ImageFont.truetype('Aller_Bd.ttf',25)
        draw.text((670,300), text, fill='black',font=font)
        image.show()
        colors_.remove('Orange')
        return colors_
    else:
        print('Incorrect.')
        return colors_

def correct_red(image):
    '''
    Function takes the refrigeration_cycle.jpg as a input. 
    This function calculates the average strength of ecah pixel colors(Red,Green,Blue) and
    stores the value in Average. Using  the RBG color value of Red, finds the red areas in
    the image and keeps as red,and converting the other pixels to Grey scale.
    The function returns a image as Red highlighted.
    '''
    for pixel in image:
        average = (pixel.red + pixel.green + pixel.blue)//3 #Finding average of all pixels 
        if pixel.red >=185 and pixel.green<=85 and pixel.blue <= 90: #Finding boady of REd
            pixel.red = 191
            pixel.blue = 78
            pixel.green = 80
        else: #makes every other Grey Scale
            pixel.red = average
            pixel.green = average
            pixel.blue = average
    return image

def correct_blue(image):
    '''
    Function takes the refrigeration_cycle.jpg as a input. 
    This function calculates the average strength of ecah pixel colors(Red,Green,Blue) and
    stores the value in Average. Using  the RBG color value of Blue, finds the red areas in
    the image and keeps as Blue,and converting the other pixels to Grey scale.
    The function returns a image as Blue highlighted.
    '''
    for pixel in image:
        average = (pixel.red + pixel.green + pixel.blue)//3 #Finding average of all pixels 
        if pixel.red <=85 and pixel.green<= 175 and pixel.blue >= 190: #Finding boady of Blue
            pixel.red = 79
            pixel.blue = 199
            pixel.green = 173
        else: #makes every other Grey Scale
            pixel.red = average
            pixel.green = average
            pixel.blue = average
    return image

def correct_green(image):
    '''
    Function takes the refrigeration_cycle.jpg as a input. 
    This function calculates the average strength of ecah pixel colors(Red,Green,Blue) and
    stores the value in Average. Using  the RBG color value of Green, finds the Green areas in
    the image and keeps as Blue,and converting the other pixels to Grey scale.
    The function returns a image as Green Shade highlighted.
    '''
    for pixel in image:
        average = (pixel.red + pixel.green + pixel.blue)//3 #Finding average of all pixels 
        if pixel.red <=165 and pixel.green>=180 and pixel.blue <= 100: #Finding boady of Green
            pixel.red = 156
            pixel.blue = 94
            pixel.green = 187
        else: #makes every other Grey Scale
            pixel.red = average
            pixel.green = average
            pixel.blue = average
    return image

def correct_orange(image):
    '''
    Function takes the refrigeration_cycle.jpg as a input. 
    This function calculates the average strength of ecah pixel colors(Red,Green,Blue) and
    stores the value in Average. Using  the RBG color value of Orange shade, finds the red areas in
    the image and keeps as Orange,and converting the other pixels to Grey scale.
    The function returns a image as Orange shade highlighted.
    '''
    for pixel in image:
        average = (pixel.red + pixel.green + pixel.blue)//3 #Finding average of all pixels 
        if pixel.red >=240 and pixel.green>=140 and pixel.blue <= 80: #Finding boady of Orange
            pixel.red = 245
            pixel.blue = 77
            pixel.green = 148
        else: #makes every other Grey Scale
            pixel.red = average
            pixel.green = average
            pixel.blue = average
    return image

if __name__ == '__main__':
    main()
