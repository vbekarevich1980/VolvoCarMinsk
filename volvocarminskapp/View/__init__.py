"""
This package exports AccountTab, CarTab, ContactTab, HomeTab, ShopTab packages,
base_screen, base_tab, navigation_tabs modules and main_screen.kv.

AccountTab --
    the package exporting 'AccountTab.components' package and account_tab
    module
CarTab --
    the package exporting 'CarTab.components' package and car_tab module
ContactTab --
    the package exporting 'ContactTab.components' package and contact_tab
    module
HomeTab --
    the package exporting 'HomeTab.components' package and home_tab module
ShopTab --
    the package exporting 'ShopTab.components' package and shop_tab module

base_screen --
    the module exporting the BaseScreenView class which is the parent class
    for view classes implementing visual representation of the application
    data model
base_tab --
    the module exporting MainScreenBottomNavigation, BaseTabView and
    MainScreenNavigationButton classes presenting elements of the application
    main navigation
navigation_tabs --
    the module exporting the screen dictionary containing the objects of the
    models and controllers of the main screens (navigation tabs) of the
    application

main_screen.kv --
    the KV language file defining the rule of the Root Widget - root screen of
    the application

"""
