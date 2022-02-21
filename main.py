from kivy.lang import Builder
from kivy.core.text import LabelBase
import os
from pathlib import Path
os.environ['KIVY_GL_BACKEND'] = 'angle_sdl2'
import random
from kivy import clock
from kivymd.app import MDApp
from kivymd.uix.card import MDCard
from kivy.core.window import Window
from kivymd.uix.label import MDLabel
from kivy.core.text import LabelBase
from kivymd.uix.dialog import MDDialog
from kivymd.uix.button import MDFlatButton
from kivymd.uix.swiper import MDSwiperItem
from kivy.properties import  StringProperty
from kivymd.uix.boxlayout import MDBoxLayout 
from kivy.uix.screenmanager import ScreenManager
from kivymd.uix.floatlayout import MDFloatLayout
from kivy.uix.relativelayout import RelativeLayout
from kivymd.uix.bottomsheet import MDListBottomSheet
from kivymd.uix.button import MDFillRoundFlatIconButton


#Getting the screens
from Interface.Screens.cat_screen import Cat_Screen
from Interface.Screens.home_screen import Home_Screen
from Interface.Screens.start_screen import Start_Screen
from Interface.Screens.recipes_screen import Recipes_Screen 
from Interface.Screens.dynamicRec_screen import DynamicRec_Screen

#Getting the Modules
from Interface.Modules.DB_searcher import *
from Interface.Modules.searchpopupmenu import SearchPopupMenu


Window.size = (350, 550)


#classes interacting with kv

dirname = os.path.dirname(__file__)
logo_bg_dir = os.path.join(dirname, "logo")


class Category(MDCard):
    image = StringProperty('')
    text = StringProperty('')

class Starter(MDFloatLayout):
    img = StringProperty('')
    # pass
class StepsItem(MDBoxLayout):
    stepNum = StringProperty('')
    step = StringProperty('')

class ImageBlock(MDBoxLayout):
    image = StringProperty('')
    recipeName = StringProperty('')
    duration = StringProperty('')
    category = StringProperty('')

class All_Recipes(MDSwiperItem):
    image = StringProperty('')
    text1 = StringProperty('')
    text2 = StringProperty('')

class CatCardItem(RelativeLayout):
    image = StringProperty('')
    text = StringProperty('')

class RecipesCardItem(RelativeLayout):
    image = StringProperty('')
    text = StringProperty('')
    duration =  StringProperty('')




#Main App Class
class RecipiaApp(MDApp):
    global  name_in_db, ar_name_in_db, cat_name_in_db
    
    search_menu = None
    notify = None

    #Methods to handle the changing and transitions of screen

    def homeScreen(self, name='Home'):
        # if self.root.current == 'Favourites' or self.root.current== 'Category':
        self.root.transition.direction = 'right'
        sm.current = name

    def recScreen(self, name='Recipes'):
        sm.current = name
        self.root.transition.direction = 'left'

    def catScreen(self, name='Category'):
        sm.current = name
        self.root.transition.direction = 'left'

    def dyrecScreen(self, name='DynamicRec'):
        sm.current = name
        self.root.transition.direction = 'left'


    def mode(self, instance):
        if self.theme_cls.theme_style == "Light":
            self.theme_cls.theme_style = "Dark"
            self.theme_cls.bg_normal
            instance.icon = "weather-sunny"
        else:
            self.theme_cls.theme_style = "Light"
            instance.icon = "moon-waning-crescent"

    #Methods to handle the pop up
    def notipopup(self):
        if not self.notify:
            self.notify = MDDialog(
                title = "No Such Recipe Found",
                type = "custom",
                content_cls = MDLabel(text="We are sorry we didn't find a recipe with that name."),
                buttons = [
                        MDFlatButton(
                        text="Ok", text_color= self.theme_cls.primary_color,on_press=lambda *args: self.notify.dismiss()
                    ),
                ],
            )

        self.notify.open()
    def searchpopup(self):
        if not self.search_menu:
            self.search_menu = MDDialog(
                title = "Search For recipes",
                type = "custom",
                content_cls = SearchPopupMenu(),
                buttons = [
                        MDFlatButton(
                        text="Search", text_color= self.theme_cls.primary_color,on_press=lambda *args: self.search_menu.dismiss(), on_release=self.search
                    ),
                ],
            )

        self.search_menu.open()

    #Method for executing the search funvtionalty
    def search(self, *args):
        search_var = f'{self.search_menu.content_cls.ids.user_search.text}'
        out = user_searches(search_var)
        if out:
            try:
                sm.get_screen("Recipes")
                sm.get_screen("Recipes").ids.container.clear_widgets()
            except:
                sm.add_widget(Builder.load_string(Recipes_Screen))

            for i in range(len(name)):
                print(i)
                sm.get_screen("Recipes").ids.container.add_widget(RecipesCardItem(image = f"{image[i]}",text=f'{name[i]}', duration= f':{duration[i]}'))

                self.recScreen()
        else:
            self.search_menu.dismiss()
            self.notipopup()        

        self.search_menu.content_cls.ids.user_search.text = ""



    #Method to put all the recipes in the database on the screen
    def put_recipe_to_screen(self):
        search_recipes()
        try:
            sm.get_screen("Recipes")
            sm.get_screen("Recipes").ids.container.clear_widgets()
        except:
            sm.add_widget(Builder.load_string(Recipes_Screen))

        for i in range(len(recipe_name)):
            sm.get_screen("Recipes").ids.container.add_widget(RecipesCardItem(image = f"{recipe_image[i]}",text=f'{recipe_name[i]}', duration= f':{recipe_duration[i]}'))

            self.recScreen()

    #Methods to put all the category in the database on the screen
    def put_category_to_screen(self):
        search_category()
        try:
            sm.get_screen("Category")
            sm.get_screen("Category").ids.container.clear_widgets()
        except:
            sm.add_widget(Builder.load_string(Cat_Screen))

        for i in range(len(cat_name)):
            sm.get_screen("Category").ids.container.add_widget(CatCardItem(image = f"{cat_image[i]}",text=f'{cat_name[i]}'))

            self.catScreen()

    #Methods to handle the dynamicness ofcards in the home screen
    def put_ar_card_to_screen(self):
        search_recipes()
        sm.get_screen("Home")
        for i in range(2):
            sm.get_screen("Home").ids.ar_card.add_widget(All_Recipes(image = f"{recipe_image[i]}",text1=f'{recipe_name[i]}', text2=f'{recipe_duration[i]}'))
        self.homeScreen()

    def put_cat_card_to_screen(self):
        search_category()
        sm.get_screen("Home")
        for i in range(6):
            sm.get_screen("Home").ids.cat_card.add_widget(Category(image = f"{cat_image[i]}",text=f'{cat_name[i]}'))
            
        self.homeScreen()


    #Methods to get the names of the cards of category or recipes inorder to search its data from the data base
    def labelTextAR(self, instance):
        self.ar_name_in_db = instance.parent.text
        search_labelTextAR(self.ar_name_in_db) 
        self.dynamic_holder()
        self.dyrecScreen()

    def labelTextCAT(self, instance):
        self.cat_name_in_db = instance.parent.text 
        search_labelTextCAT(self.cat_name_in_db)
        if cat_recipe_name:
            try:
                sm.get_screen("Recipes")
                sm.get_screen("Recipes").ids.container.clear_widgets()
            except:
                sm.add_widget(Builder.load_string(Recipes_Screen))

            for i in range(len(cat_recipe_image)):
                print(i)
                sm.get_screen("Recipes").ids.container.add_widget(RecipesCardItem(image = f"{cat_recipe_image[i]}",text=f'{cat_recipe_name[i]}', duration= f':{cat_recipe_duration[i]}'))
                cat_recipe_name.remove(cat_recipe_name[i])
                cat_recipe_image.remove(cat_recipe_image[i])
                cat_recipe_duration.remove(cat_recipe_duration[i])

            self.recScreen()

    def labelTextHomeAR(self, instance):
        self.ar_name_in_db = instance.parent.parent.text1
        search_labelTextAR(self.ar_name_in_db)
        self.dynamic_holder()
        self.dyrecScreen()

    def labelTextHomeCAT(self, instance):
        self.cat_name_in_db  = instance.text
        search_labelTextCAT(self.cat_name_in_db)
        if cat_recipe_name:
            try:
                sm.get_screen("Recipes")
                sm.get_screen("Recipes").ids.container.clear_widgets()
            except:
                sm.add_widget(Builder.load_string(Recipes_Screen))

            for i in range(len(cat_recipe_image)):
                sm.get_screen("Recipes").ids.container.add_widget(RecipesCardItem(image = f"{cat_recipe_image[i]}",text=f'{cat_recipe_name[i]}', duration= f':{cat_recipe_duration[i]}'))
                cat_recipe_name.remove(cat_recipe_name[i])
                cat_recipe_image.remove(cat_recipe_image[i])
                cat_recipe_duration.remove(cat_recipe_duration[i])

            self.recScreen()

    #callback for bottomsheet
    def callback(*args):
        pass

    #Method that adds items to the bottomsheet
    def show_requirements(self, *kwargs):
        req_sheet = MDListBottomSheet()
        for i in range(len(req_list)):
            req_sheet.add_item(
                f'{req_list[i]}',
                lambda x, y=i: self.callback()
            )
        req_sheet.open()

        
    #MEthod handling the dynamic putting of specific recipe components on a dynamic screen
    def dynamic_holder(self):
        sm.get_screen("DynamicRec").ids.topblock.clear_widgets()
        sm.get_screen("DynamicRec").ids.container.clear_widgets()
        basepath = Path(__file__).parents[0]
        font = f'{basepath}/Interface/'
        box = MDBoxLayout(size_hint_y= .10)
        btn = MDFillRoundFlatIconButton(text='Ingredients',
                icon= "food-fork-drink",
                pos_hint= {'center_y': .69, 'center_x':.8},
                font_name= f"{font}fonts/Poppins-Regular",
                on_release= self.show_requirements
                
        )
        label = MDLabel(text=f'No of Steps: {len(steps_list)}', font_name= f"{font}fonts/Poppins-Light")
        box.add_widget(label)
        box.add_widget(btn)

        j =0
        sm.get_screen("DynamicRec").ids.topblock.add_widget(ImageBlock(recipeName = f"{ar_recipe[j]}",image=f'{ar_recipe[j+1]}', duration=f'{ar_recipe[j+2]}', category=f'{ar_recipe[j+3]}'))

        sm.get_screen("DynamicRec").ids.topblock.add_widget(box)

        for i in range(len(steps_list)):
            sm.get_screen("DynamicRec").ids.container.add_widget(StepsItem(stepNum = f"{i+1}",step=f'{steps_list[i]}'))


    
    #Main build func 
    def build(self):
        global sm
        
        #Call the func
        # self.arImagefunc()

        self.theme_cls.primary_palette = 'Green'
        self.theme_cls.primary_hue = "A400"
        self.theme_cls.bg_darkest
        # if self.theme_cls.theme_style = "Dark":
        self.title = "Recipia"
        self.icon = f'{logo_bg_dir}/logo2.png'
        a = f'{logo_bg_dir}/logo2.png'


       #Create an instance of the Screen Manager and add all the screen widgets to it
        sm = ScreenManager()
        
        sm.add_widget(Builder.load_string(Cat_Screen))
        sm.add_widget(Builder.load_string(Home_Screen))
        sm.add_widget(Builder.load_string(Start_Screen))
        sm.add_widget(Builder.load_string(DynamicRec_Screen))

        sm.get_screen("StartScreen").bg_img = f'{logo_bg_dir}/logo2.png'

        return sm

    def launcher(self, *args):
        self.put_ar_card_to_screen()
        self.put_cat_card_to_screen()

    def on_start(self):
        sm.current = "StartScreen"
        sm.get_screen("StartScreen")
        clock.Clock.schedule_once(self.launcher, 4)


if __name__ == "__main__":
    # LabelBase.register(name=)
    RecipiaApp().run() 