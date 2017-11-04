# quotations

Various quotations I like or find amusing. I also merge some of the highlights from my Kindle in here, which makes it a bit of a mess.

Quotations should be in this format:

```
This is some quotation. ::: name of author ::: category_1 ::: category_2
```

Each quote can optionally be 'tagged' with one or more categories as shown above.

`make_categories.py` creates a different text file for each category and places each quotation associated with that category in that file. A quotation tagged with more than one category will be copied into more than one file.

`quote_bkg.py` make desktop backgrounds based on the quotations. Currently hard-coded the colors to use as a the background, the font (installed manually), the screen dimensions, and the number of backgrounds to generate by default (30). New lines start after 40 characters.
