#XPath
//button[text()='Sign up']
//h1[contains(text(), 'Do more!')]
//p[contains(text(), 'hands-on experience')]
//button[@class='hero-descriptor_btn btn btn-primary']
//a[contains(@href, 'facebook')]
//a[contains(@href, 'instagram')]
//iframe[contains(@src, 'youtube')]
//a[text()='Guest log in']
//p[text()='© 2021 Hillel IT school']
//h2[contains(text(), 'Contacts')]
//a[@class='socials_link']//span[@class='socials_icon icon icon-linkedin']
//app-root//header//nav//button[@appscrollto='contactsSection']
//div[@class='app-wrapper']//app-header//a[@routerlink='/']
//div[@class='hero-video']//iframe[contains(@src, 'embed')]
//div[@class='container']//a[@href='https://ithillel.ua']
//img[@alt='Instructions']
//button[contains(@class, 'btn-outline-white')]
//footer[@class='footer d-flex align-items-center']//div[contains(@class, 'footer_item -left')]
//a[contains(text(), 'Contacts')]
//div[contains(@class, 'about-picture')]//img
//app-footer//footer//div[@class='footer_item -right']//a[@href='/']
//section[@id='contactsSection']//h2[text()='Contacts']
//a[@class='header_logo']
//app-header//nav//button[contains(@appscrollto, 'aboutSection')]
//app-home//section[@id='aboutSection']//img[@alt='Instructions']

#CSS
button.hero-descriptor_btn.btn.btn-primary
h1.hero-descriptor_title
p.hero-descriptor_descr
button.hero-descriptor_btn
a.socials_link[href*='facebook']
a.socials_link[href*='instagram']
iframe[src*='youtube']
button.header-link.-guest
p:contains('© 2021 Hillel IT school')
h2:contains('Contacts')
a.socials_link span.icon-linkedin
nav.header_nav button[appscrollto='contactsSection']
div.header_inner a.header_logo
div.hero-video iframe[src*='embed']
div.container a[href='https://ithillel.ua']
img[alt='Instructions']
button.btn-outline-white
footer.footer div.footer_item.-left
nav.header_nav button:contains('Contacts')
div.about-picture img
footer.footer div.footer_item.-right a[href='/']
section#contactsSection h2:contains('Contacts')
a.header_logo
nav.header_nav button[appscrollto='aboutSection']
section#aboutSection img[alt='Instructions']