class Selectors:
    SEARCHINPUT = "//header/div[1]/div[1]/div[1]/div[2]/div[1]/div[1]/div[1]/form[1]/div[1]/input[1]"
    SEARCHRESULT = "//body/div[@id='root']/div[1]/div[3]/div[1]/div[1]/main[1]/div[1]/div[3]/div[2]/div[2]/ul[1]"
    SEARCHRESULTHEAD = "//h1[contains(text(),'Results for: EOS Rebel T7 DSLR Camera')]"
    PRODUCT1 = "//body/div[@id='root']/div[1]/div[3]/div[1]/div[1]/main[1]/div[1]/div[3]/div[2]/div[2]/ul[1]/div[1]/" \
               "div[1]/div[1]/a[1]/div[1]/div[1]/div[2]/div[1]"
    PRODUCTIMG = "//body/div[@id='root']/div[1]/div[4]/div[1]/div[2]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/" \
                 "div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]"
    ITEMHEAD = "//h1[contains(text(),'Canon EOS Rebel T7 DSLR Camera with 18-55mm IS Len')]"
    ADDINGTOCART = "//body/div[@id='root']/div[1]/div[4]/div[1]/div[2]/div[2]/div[3]/div[1]/div[1]/div[1]/div[1]" \
                   "/form[1]/button[1]"
    ITEMINCART = "//p[contains(text(),'This item has been added to your cart.')]"
    GOTOCART = "//span[contains(text(),'Go to Cart')]"
    YOURCART = "//h1[contains(text(),'Your Cart')]"
