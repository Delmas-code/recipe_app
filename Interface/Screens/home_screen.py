Home_Screen = '''

<MagicButton@MagicBehavior+MDIconButton>

<All_Recipes>
    image: ""
    text1: ""
    text2: ""
    RelativeLayout:

        FitImage:
            source: root.image
            radius: [20,]
        MDBoxLayout:
            orientation:'vertical'

            pos_hint:{'x':(root.width-self.width+dp(10))/root.width,"y":.7}
            adaptive_size:True
            padding:4
            MagicButton:
                id: icon
                icon: "cards-heart"
                user_font_size: "36sp"
                theme_text_color:'Custom'
                text_color:1,0,0,1
                adaptive_height:True
            MDLabel:
                text:  f"[font=Icons][color=#FFFF00] {md_icons['star']}[/color][/font][color=#FFFFFF] [/color]"
                markup:True
                halign:'center'


        MDCard:
            size_hint_y:None
            size_hint_x:None
            width:root.width-dp(20)
            height:dp(85)
            pos_hint:{'center_x':.5,"y":.05}
            spacing: "12dp"
            md_bg_color:.9,.9,.9,.2
            orientation:"vertical"
            padding:dp(10)
            radius:[20]
            on_press: app.labelTextHomeAR(self)

            MDLabel:
                text: root.text1
                font_style: "H6"
                size_hint_y: None
                height: self.texture_size[1]
                pos_hint: {"center_y": .5}
                # font_name: "fonts/Poppins-Medium"
                font_size: "16sp"
                bold: True
                opposite_colors: True
            MDLabel:
                text:  f"[font=Icons][color=#0000FF] {md_icons['clock-outline']}[/color][/font]" + root.text2
                font_style: "Subtitle1"
                markup:True
                size_hint_y: None
                height: self.texture_size[1]
                pos_hint: {"center_y": .5}
                # font_name: "fonts/Poppins-Light"
                opposite_colors: True


<Category>:
    radius:[25]
    image:""
    text: ''
    size_hint_x:None
    width:dp(260)
    spacing:dp(10)
    padding:dp(10)
    elevation:15
    on_press: app.labelTextHomeCAT(self)
    FitImage:
        source: root.image
        radius: [20,]
    MDBoxLayout:
        orientation:'vertical'
        MDLabel:
            text: root.text
            font_style:'H6'



MDScreen:
    name: 'Home'
    ar_card: ar_card
    cat_card: cat_card
    icon_item1: 'moon-waning-crescent'
    icon_item2: "weather-sunny"
    BoxLayout:
        orientation : 'vertical'

        MDFloatLayout:
            MDFloatLayout:
                pX1: .035
                pY1: .45
                MDLabel:
                    text: "All Recipes"
                    pos_hint: {'x': self.parent.pX1,'y':self.parent.pY1}
                    # font_name: "fonts/Poppins-SemiBold"
                    font_size: "18sp"

                     
                MDRectangleFlatButton:
                    text: 'See All'
                    pos_hint: {'x': 0.7,'y': .92}
                    on_press: app.put_recipe_to_screen()
                    # font_name: "fonts/Poppins-Regular"
                    
                MDSwiper:
                    id: ar_card
                    size_hint_y: None
                    # height: root.height  - dp(392)
                    height: root.height*.4
                    y: root.height - self.height  - dp(108)
                    # width_mult: 6


            MDFloatLayout:
                pX2: .035
                pY2: .4
                MDLabel:
                    text: "Categories"
                    pos_hint: {'x': self.parent.pX2,'center_y':self.parent.pY2}
                    # font_name: "fonts/Poppins-SemiBold"
                    font_size: "18sp"

                    
                MDRectangleFlatButton:
                    text: 'See All'
                    pos_hint: {'x': 0.7,'y': .37}
                    on_press: app.put_category_to_screen()
                    # font_name: "fonts/Poppins-Regular"
                

                MDBoxLayout:
                    size_hint_y:None
                    height:dp(110)
                    padding:[dp(5),dp(5),dp(5),dp(10)]
                    y: root.height - self.height  - dp(370)
                    ScrollView:
                        bar_width:0
                        MDBoxLayout:
                            id: cat_card
                            adaptive_width:True
                            spacing:dp(20)
                            padding:dp(5)


        MDBoxLayout:
            size_hint_y:None
            height:dp(60)
            adaptive_width:True
            padding:dp(12)
            spacing:dp(10)
            pos_hint:{'center_x':.5}
            md_bg_color:.9,0.9,0.9,.5
            radius:[50,50,0,0]
            MDIconButton:
                icon:'food'
                size_hint_x:None
                width:root.width*.2
                on_press: app.put_recipe_to_screen()
            MDIconButton:
                icon:'magnify'
                size_hint_x:None
                width:root.width*.2
                on_press: app.searchpopup()
            MDFloatingActionButton:
                icon: "home"
                color: app.theme_cls.primary_color
                size_hint_x:None
                width:root.width*.2
                on_press: app.homeScreen()
            MDIconButton:
                icon: root.icon_item1
                size_hint_x:None
                width:root.width*.2
                on_press: app.mode(self)
                on_release: icon = root.icon_item2
            MDIconButton:
                icon:'group'
                size_hint_x:None
                width:root.width*.2
                on_press: app.put_category_to_screen()



#A class to handle the Search Popup
<SearchPopupMenu>
    id: search
    orientation: 'vertical'
    spacing: "12sp"
    size_hint_y: None
    height: "60dp"
    
    MDTextField:
        id:user_search
        hint_text: "Enter Recipe"
    Widget

        

'''