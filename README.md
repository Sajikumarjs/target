# target
Create a Scrapy spider, that takes an arbitrary single product URL from www.target.com as command line argument, 
e.g. scrapy crawl target -a url=...

#Sample URLs - 
```https://www.target.com/p/-/A-79344798
https://www.target.com/p/-/A-13493042
https://www.target.com/p/-/A-85781566```


The code is expected to return the output for sample URL in below format :

```{
    "url": "https://www.target.com/p/baby-trend-expedition-race-tec-jogger-travel-system-8211-ultra-gray/-/A-79344798",
    "tcin": "79344798", 
    "upc": "090014028541", 
    "price_amount": 279.99,
    "currency": "USD",
    "description": "Read reviews and buy Baby Trend Expedition Race Tec Jogger Travel System &amp;#8211; Ultra Gray at Target. Choose from Same Day Delivery, Drive Up or Order Pickup. Free standard shipping with $35 orders. Expect More. Pay Less.", 
    "specs": null,
    "ingredients": [], 
    "bullets": "Suggested Age: Newborn to 5 years\nCar Seat Stage: Rear-facing from 4-35 pounds and up to 32 inches\nCar Seat Safety Features: Recline leveling system with dual bubble level indicators, 5-Point Adjustable Harness with one-hand adjustment, 6-position crotch belt adjustment, EPS Energy absorbing foam\nStroller Seat Adjustments: Comfort Cabin with extra-large UPF 50+ canopy with extended sun visor and Peek-A-Boo window.  Enhanced quick release front wheel for improved stability and safety (Upgrade wheel design compared to our Cityscape Jogger, Pathway Jogger, and Expedition Jogger)\nIncludes: RaceTec Jogger Stroller and car seat combination, Ally\u2122 Infant Car Seat and Base, and extra-large basket with rear access to hold parent\u2019s key essentials\nIncludes:  Modern designed parent console with cell phone positioner and 2 deep cup holders.  Swing away child tray with 2 cup holders makes getting child in and out of the stroller easily", 
    "features": [
      "Tire Type: EVA", 
      "Material: Metal, Plastic, Polyester", 
      "Includes: Car Seat Base", 
      "Care &amp; Cleaning: Spot or Wipe Clean", 
      "Suggested Age: 0-5 Years", 
      "Rear Wheel Diameter: 16 Inches", 
      "Warranty: 1 Year Limited Warranty. To obtain a copy of the manufacturer's or supplier's warranty for this item prior to purchasing the item, please call Target Guest Services at 1-800-591-3869", 
      "Min. Carseat Weight Supported: 4 Pounds", 
      "Battery: No Battery Used", 
      "Front Wheel Diameter: 12 Inches", 
      "Features: Infant Car Seat Compatible, Adjustable Handle, LATCH Compatible", 
      "Product Configuration: Single", 
      "Max. Carseat Weight Capacity: 35 Pounds", 
      "Max. Stroller Weight Capacity: 50 Pounds", 
      "Dimensions (Collapsed): 18 Inches (H) x 24 Inches (W) x 36 Inches (D)", 
      "Assembly Details: Adult Assembly Required, Tools Not Provided", 
      "Industry or Government Certifications: JPMA Certified", 
      "Weight: 24.92 Pounds", 
      "Dimensions (Overall): 41 Inches (H) x 24 Inches (W) x 48 Inches (D)"
    ]
    }
}```

If the product is having more than one sku the result will show as array of objects

