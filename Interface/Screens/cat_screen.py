Cat_Screen ='''
<Spacer2@Widget>
    size_hint_y: None
    height: "16sp"
<CatCardItem>
    size_hint_y: None
    height: '120dp'
    image: ""
    text: ""

    MDCard:
        padding: 0, 0, "24dp", "12sp"
        radius: [15,]
        ripple_behavior: True
        on_press: app.labelTextCAT(self)
        MDRelativeLayout:
            # md_bg_color: app.theme_cls.primary_color
            pos_hint: {'x':0.2}
            Image:
                source: root.image
                radius: [20,]

        Spacer2:
        MDBoxLayout:
            orientation: 'vertical'
            Widget:
            MDLabel:
                text: root.text
                # font_name: "fonts/Poppins-medium"
                font_size: "18sp"
            Spacer2:
            Widget:
        



MDScreen:
    name: 'Category'
    container: container
    MDBoxLayout:
        orientation : 'vertical'
        MDFloatLayout:
            size_hint_y: .10
            MDLabel:
                text: "Category"
                pos_hint: {'top':1}
                halign: 'left'
                # font_name: "fonts/Poppins-SemiBold"
                font_size: "18sp"

        MDFloatLayout:
            MDBoxLayout:
                orientation: 'vertical'
                ScrollView:
                    MDList:
                        id: container
        
    Widget:


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