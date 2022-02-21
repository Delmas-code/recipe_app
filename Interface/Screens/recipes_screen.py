Recipes_Screen ='''

<Spacer1@Widget>
    size_hint_y: None
    height: "16sp"
<RecipesCardItem>
    size_hint_y: None
    height: '120dp'

    MDCard:
        padding: 0, 0, "24dp", "12sp"
        radius: [15,]
        ripple_behavior: True
        on_press: app.labelTextAR(self)
        MDRelativeLayout:
            # md_bg_color: app.theme_cls.primary_color
            pos_hint: {'x':0.2}
            Image:
                source: root.image
                radius: [20,] 
                


        MDBoxLayout:
            orientation: 'vertical'
            Widget:
            MDLabel:
                text: root.text
                bold: True
                # font_name: "fonts/Poppins-Regular"
                adaptive_height: True

            Spacer1:
            Widget:
        MDBoxLayout: 
            pY: .15
            MDIconButton:
                icon:'clock-outline'
                size_hint_x:None
                width:root.width*.2
                pos_hint_y: .2
            
            MDLabel:
                text: root.duration
                pos_hint: {'center_y':self.parent.pY}
                # font_name: "fonts/Poppins-Light"
        


MDScreen:
    name: 'Recipes'
    container: container
    MDFloatLayout:
        ScrollView:
            MDList:
                id: container


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
            icon:'moon-waning-crescent'
            size_hint_x:None
            width:root.width*.2
            on_press: app.mode(self)
        MDIconButton:
            icon:'group'
            size_hint_x:None
            width:root.width*.2
            on_press: app.put_category_to_screen()



'''